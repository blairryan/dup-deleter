import unittest
from test_FileHasher import TestFileHasher
from test_DirectoryHandler import TestDirectoryHandler


def test_suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestFileHasher))
    test_suite.addTest(unittest.makeSuite(TestDirectoryHandler))
    return test_suite

if __name__ == "__main__":
    my_test_suite = test_suite()
    runner=unittest.TextTestRunner()
    runner.run(my_test_suite)