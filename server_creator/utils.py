from pathlib import Path
import shutil
import os
import stat

def create_directory(directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    return directory

def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def delete_directory(directory, *filenames_to_keep):
    directory = Path(directory)

    if not directory.exists():
        raise FileNotFoundError(f"Directory {directory} does not exist")

    if not directory.is_dir():
        raise NotADirectoryError(f"{directory} is not a directory")

    for item in directory.iterdir():
        if item.name in filenames_to_keep:
            continue

        if item.is_dir():
            shutil.rmtree(item, onerror=remove_readonly)
        else:
            item.unlink()

def neoforge_version_detection(version: str,builds_to_sort: list ) -> str | None:
    modded_builds = []
    for v in builds_to_sort:
        if "1." + v[:4] == version:
            modded_builds.append(v.replace("-beta", ""))

    int_modded_builds = [int(i[5:]) for i in modded_builds]
    return f"{version[2:]}." + str(max(int_modded_builds))