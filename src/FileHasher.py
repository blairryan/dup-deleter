import hashlib

class FileHasher(object):
    MAX_BLOCK_SIZE = 65536

    def __init__(self, new_file_path):
        self.file_path = new_file_path

    def generate_hash(self) -> str:
        """
            Read the given file and generate its hash value using md5 hashing algorithm
        """
        file_hash = hashlib.md5()
        with open(self.file_path, "rb") as open_file:
            buf = open_file.read(FileHasher.MAX_BLOCK_SIZE)
            while len(buf) > 0:
                file_hash.update(buf)
                buf = open_file.read(FileHasher.MAX_BLOCK_SIZE)

        return file_hash.hexdigest()


