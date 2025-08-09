import requests
from utils import create_directory

HEADERS = {'User-Agent': "MinecraftServerCreator/1.0 (https://github.com/Waxbyz/Mc_Server_Creator)"}

def papermc_downloader(version, name):
    base_url = "https://api.papermc.io/v2/projects/paper"
    versions_url = f"{base_url}/versions"

    # versions = requests.get(base_url, headers=HEADERS).json()['versions']
    builds = list(requests.get(f"{versions_url}/{version}/builds", headers=HEADERS).json()['builds'])[-1]
    latest_build = builds['build']
    filename = f"paper-{version}-{latest_build}.jar"
    download_url = f"{base_url}/versions/{version}/builds/{latest_build}/downloads/{filename}"

    save_dir = create_directory(f"C:/Users/User/AppData/Roaming/.mc_server_creator/servers/{name}")
    save_dir = save_dir / filename

    print(f"Downloading {filename} to {save_dir}")

    jar_response = requests.get(download_url, headers=HEADERS)
    jar_response.raise_for_status()

    with open(save_dir, "wb") as f:
        f.write(jar_response.content)

def spigot_downloader(version, name):
    pass

def fabric_downloader(version, name):
    pass

def forge_downloader(version, name):
    pass

def neoforge_downloader(version, name):
    pass

papermc_downloader(version="1.12.2", name="paper-1.12.2")
