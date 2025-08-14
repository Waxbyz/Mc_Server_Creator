import subprocess, requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

from utils import create_directory, delete_directory, neoforge_version_detection

class Downloader(ABC):
    HEADERS = {'User-Agent': "MinecraftServerCreator/1.0 (https://github.com/Waxbyz/Mc_Server_Creator)"}

    def __init__(self, version: str, name: str, directory: str):
        self.version = version
        self.name = name
        self.directory = directory
        self.latest_build = None
        self.filename = None
        self.save_dir = None
        self.download_url = None

    @abstractmethod
    def get_latest_build(self):
        pass

    @abstractmethod
    def prepare_save_path(self):
        pass

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def return_directory(self):
        return self.directory

class VanillaDownloader(Downloader):
    def __init__(self, version, name, directory):
        super().__init__(version, name, directory)
        self.manifest = "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"
        self.base_url = "https://piston-data.mojang.com/v1/objects"
        self.save_path = None

    def get_latest_build(self):
        builds = requests.get(f"{self.manifest}").json()
        self.download_url = [v for v in builds['versions'] if v['id'] == self.version][0]['url']
        self.filename = "server.jar"

    def prepare_save_path(self):
        self.save_path = create_directory(f"{self.directory}/{self.name}")
        self.save_dir = self.save_path / self.filename

    def download(self):
        print(f"Downloading {self.name} from {self.download_url}")
        jar_response = requests.get(self.download_url, headers=self.HEADERS)
        jar_response.raise_for_status()
        with open(self.save_dir, "wb") as f:
            f.write(jar_response.content)
        print(f"Saved {self.save_dir}")

    def run(self):
        self.get_latest_build()
        self.prepare_save_path()
        self.download()

    def return_directory(self):
        return self.directory

class PapermcDownloader(Downloader):
    def __init__(self, version, name, directory):
        super().__init__(version, name, directory)
        self.base_url = "https://api.papermc.io/v2/projects/paper"
        self.save_path = None

    def get_latest_build(self):
        versions_url = f"{self.base_url}/versions"
        builds = list(requests.get(f"{versions_url}/{self.version}/builds", headers=self.HEADERS).json()['builds'])[-1]
        latest_build = builds['build']
        self.filename = f"paper-{self.version}-{latest_build}.jar"
        self.download_url = f"{self.base_url}/versions/{self.version}/builds/{latest_build}/downloads/{self.filename}"

    def prepare_save_path(self):
        self.save_path = create_directory(f"{self.directory}/{self.name}")
        self.save_dir = self.save_path / self.filename

    def download(self):
        print(f"Downloading {self.name} from {self.download_url}")
        jar_response = requests.get(self.download_url, headers=self.HEADERS)
        jar_response.raise_for_status()
        with open(self.save_dir, "wb") as f:
            f.write(jar_response.content)
        print(f"Saved {self.save_dir}")

    def run(self):
        self.get_latest_build()
        self.prepare_save_path()
        self.download()

    def return_directory(self):
        return self.directory

class PurpurmcDownloader(Downloader):
    def __init__(self, version, name, directory):
        super().__init__(version, name, directory)
        self.base_url = "https://api.purpurmc.org/v2/purpur"
        self.save_path = None

    def get_latest_build(self):
        builds_url = f"{self.base_url}/{self.version}"
        builds = requests.get(builds_url, headers=self.HEADERS).json()['builds']
        self.latest_build = builds['latest']
        self.filename = f"purpur-{self.version}-{self.latest_build}.jar"
        self.download_url = f"{self.base_url}/{self.version}/{self.latest_build}/download"

    def prepare_save_path(self):
        self.save_path = create_directory(f"{self.directory}/{self.name}")
        self.save_dir = self.save_path / self.filename

    def download(self):
        print(f"Downloading {self.name} from {self.download_url}")
        jar_response = requests.get(self.download_url, headers=self.HEADERS)
        jar_response.raise_for_status()
        with open(self.save_dir, "wb") as f:
            f.write(jar_response.content)
        print(f"Saved {self.save_dir}")

    def run(self):
        self.get_latest_build()
        self.prepare_save_path()
        self.download()

    def return_directory(self):
        return self.directory

class SpigotDownloader(Downloader):
    def __init__(self, version, name, directory):
        super().__init__(version, name, directory)
        self.base_url = "https://hub.spigotmc.org/jenkins/job/BuildTools"
        self.save_path = None

    def get_latest_build(self):
        self.download_url = f"{self.base_url}/lastSuccessfulBuild/artifact/target/BuildTools.jar"
        self.filename = "BuildTools.jar"

    def prepare_save_path(self):
        self.save_path = create_directory(f"{self.directory}/{self.name}")
        self.save_dir = self.save_path / self.filename

    def download(self):
        print(f"Downloading {self.name} from {self.download_url}")
        jar_response = requests.get(self.download_url, headers=self.HEADERS)
        jar_response.raise_for_status()
        with open(self.save_dir, "wb") as f:
            f.write(jar_response.content)

        cmd = ["java", "-jar", str(self.save_dir), "--rev", self.version]
        subprocess.run(cmd, cwd=self.save_path, check=True)

    def delete(self):
        try:
            delete_directory(f"{self.save_dir.parent}",
                             f"spigot-{self.version}.jar")
        except FileNotFoundError as e:
            print(f"[!] Folder is not found {e}")

    def run(self):
        self.get_latest_build()
        self.prepare_save_path()
        self.download()
        self.delete()

    def return_directory(self):
        return self.directory

class FabricDownloader(Downloader):
    def __init__(self, version, name, directory):
        super().__init__(version, name, directory)
        self.base_url = "https://meta.fabricmc.net/v2/versions"
        self.save_path = None

    def get_latest_build(self):
        builds_url = f"{self.base_url}/loader/{self.version}"
        builds = requests.get(builds_url).json()[:1]
        self.latest_build = builds[0]['loader']['version']

        installer_versions = requests.get("https://meta.fabricmc.net/v2/versions/installer").json()
        latest_installer_version = installer_versions[0]['version']

        self.download_url = f"{self.base_url}/loader/{self.version}/{self.latest_build}/{latest_installer_version}/server/jar"
        self.filename = f"fabric-server-mc.{self.version}-loader.{self.latest_build}-launcher.{latest_installer_version}.jar"

    def prepare_save_path(self):
        self.save_path = create_directory(f"{self.directory}/{self.name}")
        self.save_dir = self.save_path / self.filename

    def download(self):
        print(f"Downloading {self.name} from {self.download_url}")
        jar_response = requests.get(self.download_url, headers=self.HEADERS)
        jar_response.raise_for_status()
        with open(self.save_dir, "wb") as f:
            f.write(jar_response.content)

    def run(self):
        self.get_latest_build()
        self.prepare_save_path()
        self.download()

    def return_directory(self):
        return self.directory

class ForgeDownloader(Downloader):
    def __init__(self, version, name, directory):
        super().__init__(version, name, directory)
        self.base_url = "https://mc-versions-api.net/api/forge"
        self.maven_url ="https://maven.minecraftforge.net/net/minecraftforge/forge"
        self.save_path = None

    def get_latest_build(self):
        builds_url = f"{self.base_url}?version={self.version}"
        builds = requests.get(builds_url).json()
        self.latest_build = builds['result'][0]

        self.download_url = f"{self.maven_url}/{self.version}-{self.latest_build}/forge-{self.version}-{self.latest_build}-installer.jar"
        self.filename = f"forge-{self.version}-{self.latest_build}-installer.jar"

    def prepare_save_path(self):
        self.save_path = create_directory(f"{self.directory}/{self.name}")
        self.save_dir = self.save_path / self.filename

    def download(self):
        print(f"Downloading {self.name} from {self.download_url}")
        jar_response = requests.get(self.download_url, headers=self.HEADERS)
        jar_response.raise_for_status()
        with open(self.save_dir, "wb") as f:
            f.write(jar_response.content)

    def run(self):
        self.get_latest_build()
        self.prepare_save_path()
        self.download()

    def return_directory(self):
        return self.directory

class NeoForgeDownloader(Downloader):
    def __init__(self, version, name, directory):
        super().__init__(version, name, directory)
        self.base_url = "https://maven.neoforged.net/releases/net/neoforged/neoforge"
        self.save_path = None

    def get_latest_build(self):
        response = requests.get(self.base_url, headers=self.HEADERS)
        response.raise_for_status()

        data = BeautifulSoup(response.text, "lxml")
        all_builds = []
        try:
            builds = data.find_all("li", class_="directory")
            for i in builds:
                build = i.find("a")
                all_builds.append(build.text.replace("/", ""))
        except AttributeError as e:
            print(f"[!] No builds found {e}")

        self.latest_build = neoforge_version_detection(version=self.version, builds_to_sort=all_builds)
        self.filename = f"neoforge-{self.latest_build}-installer.jar"
        self.download_url = f"{self.base_url}/{self.latest_build}/{self.filename}"

    def prepare_save_path(self):
        self.save_path = create_directory(f"{self.directory}/{self.name}")
        self.save_dir = self.save_path / self.filename

    def download(self):
        print(f"Downloading {self.name} from {self.download_url}")
        jar_response = requests.get(self.download_url, headers=self.HEADERS)
        jar_response.raise_for_status()
        with open(self.save_dir, "wb") as f:
            f.write(jar_response.content)

    def run(self):
        self.get_latest_build()
        self.prepare_save_path()
        self.download()

    def return_directory(self):
        return self.directory