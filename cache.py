import os
from sys import path, platform
import pathlib
import json

class Cache():


    def __init__(self, capacity):
        self.capacity = capacity
        self.priority = []
        self.cache = {}
        self.load_cache()
        self.load_order()

    def __del__(self):
        self.write_to_cache()
        self.write_to_order()

    def load_cache(self):
        my_cache = os.getcwd()
        file_path = str(my_cache) + '\\cache.txt'

        if platform == "win32":
            my_cache = pathlib.PureWindowsPath(file_path)
        else:
            my_cache = pathlib.Path(file_path)

        my_cache = pathlib.Path(str(my_cache))

        if my_cache.is_file():
            with open(my_cache, 'r') as f:
                content = f.read()
                if len(content) > 2:
                    self.cache = json.loads(content)
        else:
            my_cache.touch(exist_ok=True)

    def load_order(self):
        my_priority = os.getcwd()
        file_path = str(my_priority) + '\\priority.txt'

        if platform == "win32":
            my_priority = pathlib.PureWindowsPath(file_path)
        else:
            my_priority = pathlib.Path(file_path)

        my_priority = pathlib.Path(str(my_priority))
        if my_priority.is_file():
            with open(my_priority, 'r') as f:
                content = f.read()
                self.priority = content.splitlines()
        else:
            my_priority.touch(exist_ok=True)

        return self.cache

    def get(self, key):
        if self.cache.get(key) != None:
            self.order_cache(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        self.load_cache()
        if self.cache_not_full():
            if self.cache.get(key) != None:
                self.order_cache(key)
                self.cache[key] = value
            else:
                self.order_cache(key)
                self.cache[key] = value

        else:
            if self.cache.get(key) != None:
                self.order_cache(key)
                self.cache[key] = value
            else:
                self.remove_oldest()
                self.order_cache(key)
                self.cache[key] = value

    def order_cache(self, key):
        if self.cache.get(key) != None:
            self.priority.remove(key)
        self.priority.insert(0, key)

    def remove_oldest(self):
        last = len(self.priority)-1
        self.cache.remove(self.priority[last])
        self.priority.pop()

    def cache_not_full(self):
        return len(self.cache) < self.capacity

    def write_to_cache(self):
        my_cache = os.getcwd()
        file_path = str(my_cache) + '\\cache.txt'

        if platform == "win32":
            my_cache = pathlib.PureWindowsPath(file_path)
        else:
            my_cache = pathlib.Path(file_path)

        with open(my_cache, 'w') as f:
                json.dump(self.cache, f)

    def write_to_order(self):
        my_priority = os.getcwd()
        file_path = str(my_priority) + '\\priority.txt'

        if platform == "win32":
            my_priority = pathlib.PureWindowsPath(file_path)
        else:
            my_priority = pathlib.Path(file_path)

        my_priority = pathlib.Path(str(my_priority))

        with open(my_priority, 'w') as f:
            for line in self.priority:
                f.write(line + "\n")
