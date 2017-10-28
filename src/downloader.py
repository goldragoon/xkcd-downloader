#!/usr/bin/env python3

import json
import os
import os.path
import re
import requests
import urllib.request

if __name__ == "__main__":
    config = "config.json"
    if not os.path.isfile(config):
        with open(config, "w") as f:
            dir_ = os.getcwd()
            inputted = input("(This can be changed later in "
                             + "{}/{}) Enter the path to ".format(dir_, config)
                             + "download to (default: {}): ".format(dir_))
            # <"last"> corresponds to the last comic downloaded.
            data = {"directory": inputted if inputted else dir_, "last": 0}
            json.dump(data, f, indent = 4)
    configFile = json.loads(open(config).read())
    directory = configFile["directory"]
    if not os.path.isdir(directory):
        os.makedirs(directory)
    # http://xkcd.com/info.0.json is the link to the latest comic.
    data = requests.get("http://xkcd.com/info.0.json").json()
    numOfComics = data["num"]
    start = configFile["last"] + 1
    for comic in range(start, numOfComics + 1):
        if numOfComics - start == 0:
            percentage = 100
        else:
            percentage = ((comic - start) / (numOfComics - start)) * 100
        print("Progress: {}% ".format(round(percentage, 2)), end = "\r")
        site = "http://xkcd.com/{}/info.0.json".format(comic)
        data = requests.get(site)
        if data.status_code != 200:
            continue
        data = data.json()
        if not re.search(r".jpg|.png$", data["img"]):
            continue
        months = {1: "January", 2: "February", 3: "March", 4: "April",
                  5: "May", 6: "June", 7: "July", 8: "August", 9: "September",
                  10: "October", 11: "November", 12: "December"}
        m = months[int(data["month"])]
        m = "{}-{}".format(data["month"], m)
        newDir = "{}/{}/{}".format(directory, data["year"], m)
        if not os.path.isdir(newDir):
            os.makedirs(newDir)
        title = re.sub(r"/|\\|\:|\*|\?|\"|<|>|\|", "", data["safe_title"])
        ext = data["img"][len(data["img"]) - 4:]
        name = "{}/{}-{}{}".format(newDir, comic, title, ext)
        urllib.request.urlretrieve(data["img"], name)
        data = json.loads(open(config).read())
        data["last"] = comic
        with open(config, "w") as f:
            json.dump(data, f, indent = 4)
