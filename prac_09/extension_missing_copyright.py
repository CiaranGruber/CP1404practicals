"""
Check for any files from a lyrics folder that is missing the '.i' copyright info

Missing Copyright Checker. Created by Ciaran Gruber - 29/09/18
"""

import os

FOLDER_PATH = '.\\Lyrics'


def get_files_without_copyright(folder_path):
    """Get the path of any files without copyright info"""
    new_stuff = ['/' + os.path.basename(folder_path)]
    for thing in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, thing)):
            new_stuff.append(get_files_without_copyright(os.path.join(folder_path, thing)))
        else:
            has_copyright_line = False
            with open(os.path.join(folder_path, thing)) as file:
                for file_line in file:
                    if file_line.startswith('.i '):
                        has_copyright_line = True
                        break
            if not has_copyright_line:
                new_stuff.append([thing, 'Path: ' + os.path.join(folder_path, thing)])
    return new_stuff


def print_indented_list(bad_files, level=1):
    """Print an nested list using indents"""
    if level == 1:
        print(bad_files[0])
        del bad_files[0]
    for thing in bad_files:
        if isinstance(thing, list):
            print('\t' * level + thing[0])
            print_indented_list(thing[1:], level + 1)
        else:
            print('\t' * level + thing)


def main():
    """Get files without copyright and print to screen"""
    bad_files = get_files_without_copyright(FOLDER_PATH)
    print_indented_list(bad_files)


if __name__ == '__main__':
    main()
