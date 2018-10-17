"""
Sort files from a selected folder into selected subfolders depending on the extension

File Extension Sorter. Created by Ciaran Gruber - 28/09/18
"""

import os
import shutil

FOLDER_PATH = '.\FilesToSortV2'


def sort_files(folder_path, extension_to_folder):
    """Add folders depending on file extension and sort all files into the selected folders"""
    files = os.listdir(folder_path)
    for folder in extension_to_folder.values():
        try:
            os.mkdir(os.path.join(folder_path, folder))
        except FileExistsError:
            pass
    for file in files:
        shutil.move(os.path.join(folder_path, file), os.path.join(
            os.path.join(folder_path, extension_to_folder[os.path.splitext(file)[1]]), file))


def main():
    """Ask for folders depending on extension and sort files"""
    extension_to_folder = {}
    extensions = []
    for file in os.listdir(FOLDER_PATH):
        if not os.path.splitext(file)[1] in extensions:
            extensions.append(os.path.splitext(file)[1])
    for extension in extensions:
        extension_to_folder[extension] = input('What category would you like to sort {} files into? '
                                               .format(extension[1:]))
        while extension_to_folder[extension].strip() == '' or \
                any(elem in extension_to_folder[extension] for elem in ['\\', '/', ':']):
            extension_to_folder[extension] = input('What category would you like to sort {} files into? '
                                                   .format(extension[1:]))
    sort_files(FOLDER_PATH, extension_to_folder)


if __name__ == '__main__':
    main()
