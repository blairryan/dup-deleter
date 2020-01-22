from FileHasher import FileHasher
import os
from typing import Set


class DuplicateTracker(object):
    def __init__(self):
        self.all_files = dict()  # key: file, value: hash
        self.duplicate_files = set()

    def consume_files(self, files: Set[str], file_root: str) -> None:
        for f in files:
            file_path = os.path.join(file_root, f)
            file_hasher = FileHasher(file_path)
            hash_value = file_hasher.generate_hash()
            self.all_files.update({f: hash_value})
            if self.is_duplicate(f): self.duplicate_files.add(f)

    def is_duplicate(self, file: str) -> bool:
        pass

    def get_duplicates(self) -> Set[str]:
        pass