#!/usr/bin/env python3

import json
import os
import os.path
import re
import requests
import urllib.request


if __name__ == "__main__":
    directory = input(
        "Enter the path to save the comics to (if you don't enter a path, "
        + "they will be saved to a directory named \"comics\" in the "
        + "directory of this program):")
    if not directory:
        directory = "comics"
    if not os.path.isdir(directory):
        os.makedirs(directory)
    dataFile = "{}/DO_NOT_DELETE.json".format(directory)
    if not os.path.isfile(dataFile):
        with open(dataFile, "w") as f:
            json.dump({"last": 0}, f, indent = 4)
    data = requests.get("http://xkcd.com/info.0.json").json()
    numOfComics = data["num"]
    f = json.loads(open(dataFile).read())
    start = f["last"] + 1
    for comic in range(start, numOfComics + 1):
        percentage = ((comic - start) / (numOfComics - start)) * 100
        print("Progress: {}% ".format(round(percentage, 2)), end = "\r")
        site = "http://xkcd.com/{}/info.0.json".format(comic)
        data = requests.get(site).json()
        months = {1: "January", 2: "February", 3: "March", 4: "April",
                  5: "May", 6: "June", 7: "July", 8: "August", 9: "September",
                  10: "October", 11: "November", 12: "December"}
        m = months[int(data["month"])]
        newDir = "{}/{}/{}".format(directory, data["year"], m)
        if not os.path.isdir(newDir):
            os.makedirs(newDir)
        title = re.sub(r"/|\\|\:|\*|\?|\"|<|>|\|", "", data["safe_title"])
        name = "{}/{}-{}.png".format(newDir, comic, title)
        urllib.request.urlretrieve(data["img"], name)
        with open(dataFile, "w") as f:
            json.dump({"last": comic}, f, indent = 4)
