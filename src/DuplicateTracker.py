from FileHasher import FileHasher
import os
from typing import Set


class DuplicateTracker(object):
    def __init__(self):
        self.all_files = dict()  # key: file, value: hash
        self.duplicate_files = set()

    def consume_files(self, files: Set[str], file_root: str) -> None:
        pass

    def is_duplicate(self, file: str) -> bool:
        pass

    def get_duplicates(self) -> Set[str]:
        pass
