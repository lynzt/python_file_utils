import os
import json
from urlparse import urlparse
from shutil import copyfile

def get_files_in_directory_skip_hidden(path):
    dirs = get_files_in_directory(path)
    return filter(lambda f: not f.startswith('.'), dirs) # remove files names starting w/ dot

def get_files_in_directory(path):
    return next(os.walk(path))[2]

def get_folders_in_directory(path):
    return next(os.walk(path))[1]

def check_file_or_folder_exists(name_and_path):
    return os.path.exists(name_and_path)

def move_file(source, target):
    os.rename(source, target)

def copy_file(source, target):
    copyfile(source, target)

def touch_file(filename_and_path):
    open(filename_and_path, 'a').close()

def remove_file(file_to_remove):
    os.remove(file_to_remove)

def check_file_exists(filename_and_path):
    return os.path.isfile(filename_and_path)

def get_file_size(filename_and_path):
    return os.path.getsize(filename_and_path)
    # return os.stat(filename_and_path).st_size

def split_filename_extension(file): # pass in filename or uri
    url_parsed = urlparse(file)
    filename, extension = os.path.splitext(url_parsed.path)
    return {'filename': filename, 'extension': extension}

def truncate_file(filename_and_path):
    open(filename_and_path, 'w').close()

def open_file_to_append(filename_and_path):
    return open(filename_and_path, 'a')

def write_string_to_file(file_handle, str):
    file_handle.write("%s\n" % (str))

def write_dict_to_file(file_handle, dict):
    file_handle.write(json.dumps(dict) + "\n")

def close_file(file_handle):
    file_handle.close()
