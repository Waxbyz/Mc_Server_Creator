import subprocess, requests
from abc import ABC, abstractmethod
from utils import create_directory, delete_directory

class Downloader(ABC):
    HEADERS = {'User-Agent': "MinecraftServerCreator/1.0 (https://github.com/Waxbyz/Mc_Server_Creator)"}

    def __init__(self, version: str, name: str, direction: str):
        self.version = version
        self.name = name
        self.direction = direction
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

class PapermcDownloader(Downloader):
    def __init__(self, version, name, direction):
        super().__init__(version, name, direction)
        self.base_url = "https://api.papermc.io/v2/projects/paper"

    def get_latest_build(self):
        versions_url = f"{self.base_url}/versions"
        builds = list(requests.get(f"{versions_url}/{self.version}/builds", headers=self.HEADERS).json()['builds'])[-1]
        latest_build = builds['build']
        self.filename = f"paper-{self.version}-{latest_build}.jar"
        self.download_url = f"{self.base_url}/versions/{self.version}/builds/{latest_build}/downloads/{self.filename}"

    def prepare_save_path(self):
        save_path = create_directory(f"{self.direction}/{self.name}")
        self.save_dir = save_path / self.filename

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

class SpigotDownloader(Downloader):
    def __init__(self, version, name, direction):
        super().__init__(version, name, direction)
        self.base_url = "https://hub.spigotmc.org/jenkins/job/BuildTools"
        self.save_path = None

    def get_latest_build(self):
        self.download_url = f"{self.base_url}/lastSuccessfulBuild/artifact/target/BuildTools.jar"
        self.filename = "BuildTools.jar"

    def prepare_save_path(self):
        self.save_path = create_directory(f"{self.direction}/{self.name}")
        self.save_dir = self.save_path / self.filename

    def download(self):
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


paper = PapermcDownloader(version="1.21.1", name="paper-1.21.1", direction="C:/Users/User/AppData/Roaming/.mc_server_creator/servers")
paper.run()
spigot = SpigotDownloader(version="1.21.1", name="spigot-1.21.1", direction="C:/Users/User/AppData/Roaming/.mc_server_creator/servers")
spigot.run()
