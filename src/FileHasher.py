import hashlib

class FileHasher(object):
    MAX_BLOCK_SIZE = 65536

    def __init__(self, new_filename):
        self.filename = new_filename

    def generate_hash(self):
        """
            Read the given file and generate its hash value using md5 hashing algorithm
        """
        file_hash = hashlib.md5()
        with open(self.filename, "rb") as open_file:
            buf = open_file.read(FileHasher.MAX_BLOCK_SIZE)
            while len(buf) > 0:
                file_hash.update(buf)
                buf = open_file.read(FileHasher.MAX_BLOCK_SIZE)

        return file_hash.hexdigest()


