from FileHasher import FileHasher
import os
from typing import Set


class DuplicateTracker(object):
    def __init__(self):
        self.all_files = dict()  # key: file, value: hash
        self.duplicate_files = set()

    def consume_files(self, files: Set[str], file_root: str) -> None:
        """
            Hash and keep track of all files, separate out duplicates into their
            own container.
        """
        for f in files:
            file_path = os.path.join(file_root, f)
            file_hasher = FileHasher(file_path)
            hash_value = file_hasher.generate_hash()
            if self.is_duplicate(hash_value): self.duplicate_files.add(f)
            self.all_files.update({f: hash_value})

    def is_duplicate(self, hash_value: str) -> bool:
        """
            Return True if the given file is considered a duplicate.
        """
        pass

    def get_duplicates(self) -> Set[str]:
        """
            Return the list of duplicate files.
        """
        pass
