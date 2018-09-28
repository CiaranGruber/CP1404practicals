"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace('.TXT', '.txt')
    new_name = ""
    for i, letter in enumerate(filename):
        if letter.isupper() and i != 0:
            new_name += '_'
        if letter == ' ':
            new_name += '_'
        else:
            new_name += letter
    new_name = '_'.join([name.title() for name in new_name.split('_')])
    new_name = new_name.replace('.Txt', '.txt')
    return new_name


def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            os.rename(os.path.join(directory_name, filename),
                      os.path.join(directory_name, get_fixed_filename(filename)))


main()
