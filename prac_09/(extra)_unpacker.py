"""
Unpack all subfolders from in chosen folder

Folder unpacker. Created by Ciaran Gruber - 28/09/18
"""

import os
import shutil

FOLDER_PATH = './FilesToSort'


def unpack(folder_path):
    """Unpack the selected folder"""
    for folder in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, folder)):
            for file in os.listdir(os.path.join(folder_path, folder)):
                shutil.move(os.path.join(os.path.join(folder_path, folder), file), os.path.join(folder_path, file))
            try:
                os.remove(os.path.join(folder_path, folder))
            except PermissionError:
                pass


if __name__ == '__main__':
    unpack(FOLDER_PATH)
