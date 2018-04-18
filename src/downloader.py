#!/usr/bin/env python3

import json
import os
import os.path
import re
import requests
import urllib.request
import multiprocessing
import threading
from threading import Thread, Lock 

if __name__ == "__main__":

    num_cores = multiprocessing.cpu_count()   
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
    global_start = configFile["last"] + 1
    num_downloaded = global_start

    def download_comic(worker_start, worker_end, mutex):
        global num_downloaded
        for comic in range(worker_start, worker_end):

            mutex.acquire()
            if numOfComics - global_start == 0:
                percentage = 100
            else:
                num_downloaded = num_downloaded + 1
                percentage = ((num_downloaded - global_start) / (numOfComics - global_start)) * 100
            print("Progress: {}% ".format(round(percentage, 2)), end = "\r")
            mutex.release()

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

    percentage_mutex = Lock()
    chunk = (numOfComics - global_start) // num_cores 
    for i in range(num_cores):
        t = Thread(target=download_comic, args=(global_start + chunk * i, global_start + chunk * (i + 1), percentage_mutex))
        t.start()

    for thread in threading.enumerate():
        if t is not threading.currentThread():
            t.join()


    
