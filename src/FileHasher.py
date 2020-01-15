import hashlib

class FileHasher(object):
    MAX_BLOCK_SIZE = 65536

    def __init__(self, new_filename):
        self.filename = new_filename

    def generate_hash(self):
        """
            Read the given file and generate its hash value using md5 hashing algorithm
        """
        pass

