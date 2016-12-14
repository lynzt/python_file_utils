import os
import unittest
# from freezegun import freeze_time
# import datetime
from file_utils import file_utils

class UtilsTests(unittest.TestCase):

    def test_get_files_in_directory_skip_hidden(self):
        files = file_utils.get_files_in_directory_skip_hidden('tests/data')
        self.assertEqual(len(files), 3)

    def test_get_files_in_directory(self):
        files = file_utils.get_files_in_directory('tests/data')
        self.assertEqual(len(files), 5)

    def test_get_folders_in_directory(self):
        dirs = file_utils.get_folders_in_directory('tests/data')
        self.assertEqual(len(dirs), 3)

    def test_check_file_or_folder_exists(self):
        self.assertTrue(file_utils.check_file_or_folder_exists('tests/data/folder1'))
        self.assertFalse(file_utils.check_file_or_folder_exists('tests/data/folder5'))
        self.assertFalse(file_utils.check_file_or_folder_exists('tests/nofolder/folder1'))

    def test_move_file(self):
        path1 = 'tests/data/folder2/'
        path2 = 'tests/data/folder3/'
        file_utils.move_file(path1 + 'file3.txt', path2 + 'file3.txt')
        self.assertTrue(file_utils.check_file_exists(path2 + 'file3.txt'))
        file_utils.move_file(path2 + 'file3.txt', path1 + 'file3.txt')
        self.assertTrue(file_utils.check_file_exists(path1 + 'file3.txt'))

    def test_add_and_remove_file(self):
        filename = 'tests/data/file10.txt'
        file_utils.touch_file(filename)
        self.assertTrue(file_utils.check_file_exists(filename))
        file_utils.remove_file(filename)
        self.assertFalse(file_utils.check_file_exists(filename))

    def test_check_file_exists(self):
        self.assertTrue(file_utils.check_file_exists('tests/data/file1.txt'))
        self.assertFalse(file_utils.check_file_exists('tests/data/folder1'))
        self.assertFalse(file_utils.check_file_exists('tests/data/file5.txt'))

    def test_check_file_exists(self):
        self.assertTrue(file_utils.check_file_exists('tests/data/file1.txt'))
        self.assertFalse(file_utils.check_file_exists('tests/data/folder1'))
        self.assertFalse(file_utils.check_file_exists('tests/data/file5.txt'))

    def test_get_file_size(self):
        self.assertEqual(file_utils.get_file_size('tests/data/file1.txt'), 0)
        self.assertEqual(file_utils.get_file_size('tests/data/cabelas-inc.png'), 7710)





# APIKEY=key_here python -m unittest discover -s tests -p "*_tests.py"
