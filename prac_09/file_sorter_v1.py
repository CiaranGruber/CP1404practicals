"""
Sort files from a selected folder into subfolders for each extension

File Extension Sorter. Created by Ciaran Gruber - 28/09/18
"""

import os
import shutil


def sort_files(folder_path):
    """Add folders depending on file extensions and sort all files into these folders"""
    files = os.listdir(folder_path)
    extensions = []
    for file in os.listdir(folder_path):
        if not os.path.splitext(file)[1] in extensions:
            extensions.append(os.path.splitext(file)[1])
    for extension in extensions:
        os.mkdir(os.path.join(folder_path, extension[1:]))
    for file in files:
        shutil.move(os.path.join(folder_path, file), os.path.join(os.path.join(folder_path,
                                                                               os.path.splitext(file)[1][1:]), file))


if __name__ == '__main__':
    sort_files('.\FilesToSort')
