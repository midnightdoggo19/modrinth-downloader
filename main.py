import json
import os
import requests

url = "https://api.modrinth.com/v2/"
config = "config.json"

# gets the latest version of minecraft
def getLatestVersion():
    versions = requests.get(f"{url}tag/game_version").json()
    for version in versions:
        if version["major"]:
            return version["version"]

# goes and gets the mods
def md(id):
    name = requests.get(f"{url}v2/project/{id}").json()["title"]
    e = requests.get(f"{url}/project/{id}/version").json()
    thing = None
    for item in e:
        if versionWanted in item["game_versions"] and loaderWanted in item["loaders"]:
            for file in item["files"]:
                if file["primary"]:
                    thing = file
                    break
            break
    if thing is not None:
        with requests.get(thing["url"], stream=True) as r:
            with open(f"{location}/{thing["filename"]}", "wb") as f:
                f.write(r.content)
                print(thing["filename"])
    else:
        print(f"Cannot find \"{name}\" for version {versionWanted} and loader \"{loaderWanted}\"")

if __name__ == "__main__":
    with open(config, "r") as r:
        config = json.load(r)
        modrinthIds = config["modrinth"]
        loaderWanted = config.get("loader", "fabric").lower()
        versionWanted = config.get("version", getLatestVersion())
        location = config.get("location", "output")
        delete = config.get("delete", False)

    if not os.path.isdir(location):
        os.mkdir(location)
    elif delete:
        for file in os.listdir(location):
            if file.endswith(".jar"):
                os.remove(f"{location}/{file}")
    for id in modrinthIds:
        if id is not None:
            md(id)