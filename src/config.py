import os
import json


class Config:

    DIRECTORY = "directory"
    SUCCEEDED = "succeeded"

    def __init__(self, name):
        self._name = name
        self._data = dict()

        # Properties that reside in _data
        self.directory = "./"
        self.succeeded = 0b0  # List of downloaded comics stored as binary 

        if not os.path.isfile(self._name):
            with open(self._name, "w") as _file:
                _dir = os.getcwd()
                _changed_dir = input("(This can be changed later in {}/{}) Enter the path to ".format(_dir, self._name) + "download to (default: {}): ".format(_dir))

                self.directory = _changed_dir if _changed_dir else self.directory
                json.dump(self.data, _file, indent=4)

        self.data = json.loads(open(self._name).read())  # Load old config file

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def directory(self):
        return self._data[self.DIRECTORY]
 
    @directory.setter
    def directory(self, directory):
        self._data[self.DIRECTORY] = directory

    @property
    def succeeded(self):
        return self._data[self.SUCCEEDED]

    @succeeded.setter
    def succeeded(self, succeeded):
        self._data[self.SUCCEEDED] = succeeded

    def get_succeeded_list(self, end, start=0):
        return [comic for comic in range(end) if self.succeeded & (0b1 << comic)]
        
    def set_succeeded_list(self, succeeded_list):
        pass
