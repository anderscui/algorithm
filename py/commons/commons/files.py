# coding=utf-8
from pathlib import PurePath


class FileInfo:
    def __init__(self, raw_path):
        self.raw_path = raw_path

        p = PurePath(self.raw_path)
        self.name = p.name
        self.size = file_size(self.raw_path)
