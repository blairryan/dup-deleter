import unittest
from unittest import mock
from DuplicateTracker import DuplicateTracker
from FileHasher import FileHasher


class TestDuplicateTracker(unittest.TestCase):
    def setUp(self):
        self.duplicate_tracker = DuplicateTracker()

# DuplicateTracker.consume_files tests

    @mock.patch.object(FileHasher, "generate_hash", return_value="fake_hash")
    def test_consume_files_calls_generate_hash(self, mock_gen_hash):
        files = {"file1", "file2"}
        path = "fake dir path"
        self.duplicate_tracker.consume_files(files, path)

        mock_gen_hash.assert_called()

    @mock.patch.object(FileHasher, "generate_hash", return_value="fake_hash")
    def test_consume_files_adds_to_all_files(self, mock_gen_hash):
        files = {"file1", "file2"}
        path = "fake dir path"
        expected_all_files = {f:mock_gen_hash.return_value for f in files}
        self.duplicate_tracker.consume_files(files, path)

        assert self.duplicate_tracker.all_files == expected_all_files 


    @mock.patch.object(FileHasher, "generate_hash", return_value="fake_hash")
    @mock.patch.object(DuplicateTracker, "is_duplicate", return_value=True)
    def test_consume_files_adds_duplicates(self, mock_is_duplicate, mock_gen_hash):
        files = {"file1", "file2"}
        path = "fake dir path"
        self.duplicate_tracker.consume_files(files, path)

        assert self.duplicate_tracker.duplicate_files == files
        
# DuplicateTracker.is_duplicate tests
    
    def test_is_duplicate_true(self):
        """
            Ensure is_duplicate returns True when the given 
            file is a duplicate.
        """
        self.duplicate_tracker.all_files = {"file1": "hash1", "file2": "hash2"}
        is_dup = self.duplicate_tracker.is_duplicate("hash2")
        self.duplicate_tracker.all_files = dict()  # clean up
        
        self.assertTrue(is_dup)

    def test_is_duplicate_false(self):
        """
            Ensure is_duplicate returns False when the given 
            file is not yet considered a duplicate.
        """
        is_dup = self.duplicate_tracker.is_duplicate("fake_hash")

        self.assertFalse(is_dup)