import os
import unittest
from file_utils import file_utils

class UtilsTests(unittest.TestCase):

    def test_get_files_in_directory_skip_hidden(self):
        files = file_utils.get_files_in_directory_skip_hidden('tests/data')
        self.assertEqual(len(files), 5)

    def test_get_files_in_directory(self):
        files = file_utils.get_files_in_directory('tests/data')
        self.assertEqual(len(files), 7)

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
        file_utils.move_file(path1 + 'file4.txt', path2 + 'file4.txt')
        self.assertTrue(file_utils.check_file_exists(path2 + 'file4.txt'))
        file_utils.move_file(path2 + 'file4.txt', path1 + 'file4.txt')
        self.assertTrue(file_utils.check_file_exists(path1 + 'file4.txt'))

    def test_copy_file(self):
        file1 = 'tests/data/file3.txt'
        file2 = 'tests/data/file3_copy.txt'
        file_utils.copy_file(file1, file2)
        self.assertTrue(file_utils.check_file_exists(file1))
        self.assertTrue(file_utils.check_file_exists(file2))
        file_utils.remove_file(file2)
        self.assertFalse(file_utils.check_file_exists(file2))

    def test_add_and_remove_file(self):
        filename = 'tests/data/file10.txt'
        file_utils.touch_file(filename)
        self.assertTrue(file_utils.check_file_exists(filename))
        file_utils.remove_file(filename)
        self.assertFalse(file_utils.check_file_exists(filename))

    def test_touch_directory(self):
        path1 = 'tests/data/folder3'
        path2 = 'tests/data/folder4'
        self.assertTrue(file_utils.check_directory_exists(path1))
        file_utils.touch_directory(path1)
        self.assertTrue(file_utils.check_directory_exists(path1))

        self.assertFalse(file_utils.check_directory_exists(path2))
        file_utils.touch_directory(path2)
        self.assertTrue(file_utils.check_directory_exists(path2))
        file_utils.remove_directory(path2)
        self.assertFalse(file_utils.check_directory_exists(path2))

    def test_check_file_exists(self):
        self.assertTrue(file_utils.check_file_exists('tests/data/file1.txt'))
        self.assertFalse(file_utils.check_file_exists('tests/data/folder1'))
        self.assertFalse(file_utils.check_file_exists('tests/data/file5.txt'))

    def test_get_file_size(self):
        self.assertEqual(file_utils.get_file_size('tests/data/file1.txt'), 0)
        self.assertEqual(file_utils.get_file_size('tests/data/cabelas-inc.png'), 7710)

    def test_split_filename_extension(self):
        uri = "https://yt3.ggpht.com/-p-K2HbhiCfE/AAAAAAAAAAI/AAAAAAAAAAA/k4V1tvBNygo/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"
        file = file_utils.split_filename_extension(uri)
        self.assertEqual(file['extension'], '.jpg')

        filename = "a_file.csv"
        file = file_utils.split_filename_extension(filename)
        self.assertEqual(file['extension'], '.csv')
    #
    # def test_writing_to_file(self):
    #     filename_and_path = 'tests/data/manipulation_file.txt'
    #     file_handle = file_utils.open_file_to_append(filename_and_path)
    #     file_utils.write_string_to_file(file_handle, 'abc123')
    #     file_utils.write_dict_to_file(file_handle, {'hello': 'world'})
    #     file_utils.write_dict_to_file(file_handle, {'harry': 'potter'})
    #     file_utils.close_file(file_handle)

    # def test_truncating_file(self):
    #     filename_and_path = 'tests/data/manipulation_file.txt'
    #     file_utils.truncate_file(filename_and_path)

