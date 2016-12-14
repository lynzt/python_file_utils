import json
import unidecode
import requests
import datetime
import time
import os
import urllib
from slugify import slugify
from bs4 import BeautifulSoup

def get_files_in_directory_skip_hidden(path):
    dirs = get_files_in_directory(path)
    return filter(lambda f: not f.startswith('.'), dirs) # remove files names starting w/ dot

def get_files_in_directory(path):
    return next(os.walk(path))[2]

def get_folders_in_directory(path):
    return next(os.walk(path))[1]

def check_file_or_folder_exists(name_and_path):
    return os.path.exists(name_and_path)

def move_file(from_path, to_path):
    os.rename(from_path, to_path)

def touch_file(filename_and_path):
    open(filename_and_path, 'a').close()

def remove_file(file_to_remove):
    os.remove(file_to_remove)

def check_file_exists(filename_and_path):
    return os.path.isfile(filename_and_path)

def get_file_size(filename_and_path):
    return os.path.getsize(filename_and_path)
    # return os.stat(filename_and_path).st_size 