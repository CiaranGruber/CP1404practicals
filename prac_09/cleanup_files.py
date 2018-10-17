"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os

LYRICS_FOLDER = 'Lyrics'


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    for i, letter in enumerate(filename):
        if letter == '.':
            new_name += '.' + filename.split('.')[1]
            break
        if letter.isupper() and i != 0 and new_name[-1] not in ['(', ')', '_']:
            new_name += '_'
        if letter == ' ':
            new_name += '_'
        else:
            new_name += letter
    new_name = new_name.title().replace('.Txt', '.txt')
    return new_name


def main():
    """Process all subdirectories using os.walk()."""
    os.chdir(LYRICS_FOLDER)
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            os.rename(os.path.join(directory_name, filename),
                      os.path.join(directory_name, get_fixed_filename(filename)))


main()
