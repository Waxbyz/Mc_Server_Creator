import requests
from bs4 import *
from abc import ABC, abstractmethod

class VersionsGetter(ABC):
    HEADERS = {'User-Agent': "MinecraftServerCreator/1.0 (https://github.com/Waxbyz/Mc_Server_Creator)"}

    def __init__(self, versions_list: list) -> None:
        self.base_url = None
        self.versions_list = versions_list

    @abstractmethod
    def get_version(self) -> list:
        pass

class VanillaVersionsGetter(VersionsGetter):
    def __init__(self, versions_list: list) -> None:
        super().__init__(versions_list)
        self.base_url = "https://mc-versions-api.net/api/java"

    def get_version(self) -> list:
        response = requests.get(self.base_url, headers=VanillaVersionsGetter.HEADERS)
        response.raise_for_status()
        self.versions_list = response.json()['result']

        return self.versions_list

class PaperVersionsGetter(VersionsGetter):
    def __init__(self, versions_list: list) -> None:
        super().__init__(versions_list)
        self.base_url = "https://api.papermc.io/v2/projects/paper"

    def get_version(self) -> list:
        response = requests.get(self.base_url, headers=VanillaVersionsGetter.HEADERS)
        response.raise_for_status()
        self.versions_list = response.json()['versions']
        for i in self.versions_list:
            if 'pre' in i:
                self.versions_list.remove(i)
            else:
                continue

        return self.versions_list

class PurpurVersionsGetter(VersionsGetter):
    def __init__(self, versions_list: list) -> None:
        super().__init__(versions_list)
        self.base_url = "https://api.purpurmc.org/v2/purpur"

    def get_version(self) -> list:
        response = requests.get(self.base_url, headers=VanillaVersionsGetter.HEADERS)
        response.raise_for_status()
        self.versions_list = sorted(response.json()['versions'], reverse=True)

        return self.versions_list

class SpigotVersionsGetter(VersionsGetter):
    def __init__(self, versions_list: list) -> None:
        super().__init__(versions_list)
        self.base_url = "https://hub.spigotmc.org/versions/"

    def get_version(self) -> list:
        response = requests.get(self.base_url, headers=VanillaVersionsGetter.HEADERS)
        response.raise_for_status()

        data = BeautifulSoup(response.text, 'lxml')
        try:
            for link in data.find_all("a", href=True):
                href = link['href']
                if href.endswith(".json") and href.startswith("1."):
                    version = href.replace(".json", "").strip("/")
                    if "pre" in version.lower() or "rc" in version.lower():
                        continue
                    self.versions_list.append(version)
        except AttributeError as e:
            print(f"[!] No versions found: {e}")

        def version_key(v):
            return [int(part) for part in v.split(".")]

        self.versions_list = sorted(self.versions_list, key=version_key, reverse=True)

        return self.versions_list

class FabricVersionsGetter(VersionsGetter):
    def __init__(self, versions_list: list) -> None:
        super().__init__(versions_list)
        self.base_url = "https://meta.fabricmc.net/v2/versions"

    def get_version(self) -> list:
        response = requests.get(self.base_url, headers=VanillaVersionsGetter.HEADERS)
        response.raise_for_status()
        data = response.json()
        for item in data['game']:
            if item.get("stable") == True:
                self.versions_list.append(item["version"])

        return self.versions_list

class ForgeVersionsGetter(VersionsGetter):
    def __init__(self, versions_list: list) -> None:
        super().__init__(versions_list)
        self.base_url = "https://mc-versions-api.net/api/forge"

    def get_version(self) -> list:
        response = requests.get(self.base_url, headers=VanillaVersionsGetter.HEADERS)
        response.raise_for_status()
        data = response.json()
        for item in data['result']:
            for key, _ in item.items():
                self.versions_list.append(key)

        return self.versions_list

class NeoForgeVersionsGetter(VersionsGetter):
    def __init__(self, versions_list: list) -> None:
        super().__init__(versions_list)
        self.base_url = "https://maven.neoforged.net/releases/net/neoforged/neoforge"
        self.new_versions_list = []

    def get_version(self) -> list:
        response = requests.get(self.base_url, headers=VanillaVersionsGetter.HEADERS)
        response.raise_for_status()

        data = BeautifulSoup(response.text, 'lxml')
        try:
            builds = data.find_all("li", class_="directory")
            for i in builds:
                build = i.find("a")
                self.versions_list.append("1." + build.text.replace("/", "")[:4])
            for i in range(3):
                self.versions_list.pop(0)
            self.versions_list = list(set(self.versions_list))
            for version in self.versions_list:
                parts = version.split(".")
                if len(parts) == 3 and parts[2] == "0":
                    self.new_versions_list.append(".".join(parts[:2]))
                else:
                    self.new_versions_list.append(version)
        except AttributeError as e:
            print(f"[!] No builds found {e}")

        def version_key(v):
            return [int(part) for part in v.split(".")]

        self.versions_list = list(reversed(sorted(self.new_versions_list, key=version_key)))

        return self.versions_list

def get_loaders(loaders_list: list) -> list:
    loaders_list.append("Vanilla")
    loaders_list.append("Paper")
    loaders_list.append("Purpur")
    loaders_list.append("Spigot")
    loaders_list.append("Fabric")
    loaders_list.append("Forge")
    loaders_list.append("NeoForge")

    return loaders_list