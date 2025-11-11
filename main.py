import json
import os
import requests

url = "https://api.modrinth.com/v2/"
config = "config.json"

# gets the latest version of minecraft
def getLatestVersion():
    try:
        versions = requests.get(f"{url}tag/game_version").json()
    except:
        print("Failed to get latest version!")
    for version in versions:
        if version["major"]:
            return version["version"]

# goes and gets the mods
def download(id):
    name = requests.get(f"{url}project/{id}").json()["title"]
    versions = requests.get(f"{url}project/{id}/version").json()
    fileToGet = None

    for item in versions:
        if versionWanted in item["game_versions"] and loaderWanted in item["loaders"]:
            for file in item["files"]:
                if file["primary"]:
                    fileToGet = file
                    break
            break
    if fileToGet is not None:
        with requests.get(fileToGet["url"], stream=True) as r:
            with open(f"{location}/{fileToGet["filename"]}", "wb") as f:
                f.write(r.content)
                print(fileToGet["filename"])
    else:
        print(f"Cannot find \"{name}\" for version {versionWanted} and loader \"{loaderWanted}\"")

if __name__ == "__main__":
    try:
        with open(config, "r") as r:
            config = json.load(r)
            modrinthIds = config["modrinth"]
            loaderWanted = config.get("loader", "fabric").lower()
            versionWanted = config.get("version", getLatestVersion())
            location = config.get("location", "output")
            delete = config.get("delete", False)
    except:
        print("We failed to get some values; is the config file correct?")

    if not os.path.isdir(location):
        os.mkdir(location)
    elif delete:
        for file in os.listdir(location):
            if file.endswith(".jar"):
                os.remove(f"{location}/{file}")
    for id in modrinthIds:
        if id is not None:
            try:
                download(id)
            except:
                print(f"Cannot find \"{id}\" for version {versionWanted} and loader \"{loaderWanted}\"")