import os
import time
from pprint import pprint
from colorama import Fore

def main():

    print(Fore.CYAN + "Enter '1' to execute scripts in stages with input values or Enter '2' to execute scripts by time: ")
    choice = input()

    while ('1' in choice and '2' in choice) or ('1' not in choice and '2' not in choice):
        print(
            Fore.CYAN + "Enter '1' to execute scripts in stages with input values or Enter '2' to execute scripts by time: ")
        choice = input()

    if '1' in choice:
        input_function()
    else:
        timed_function()

def timed_function():

    os.system('python create_files_downloads_folder.py')
    print(Fore.GREEN + "Dummy files created in downloads folder.")
    time.sleep(3)

    os.system('python file_organizer.py')
    print(Fore.BLUE + 'Organized all files into folders within the ~/organized-downloads directory.'
          )
    time.sleep(3)

    os.system('python determine_size.py')
    print(Fore.MAGENTA + 'Determined all files sizes and creation times.')
    time.sleep(3)

    os.system('python delete_files_from_folders.py')
    print(Fore.WHITE + 'Deleted all files from subdirectories of ~/organized-downloads directory.')

def input_function():
# STEP 1 Create Files in Downloads Folder
    print(Fore.GREEN + "Enter '1' to create dummy files: ")
    x = input()
    while '1' not in x:
        print(Fore.GREEN + "Enter '1' to create dummy files: ")
    os.system('python create_files_downloads_folder.py')

# STEP 2 organize files by file extension in an array of other folders
    print(Fore.BLUE + "Enter '1' to organize files into folders by file extension: ")
    y = input()
    while '1' not in y:
        print(Fore.BLUE + "Enter '1' to organize files into folders by file extension: ")
    os.system('python file_organizer.py')

# STEP 3 determine the size and time of creation of all files in all folders recursively starting with a base path
    print(Fore.MAGENTA + "Enter '1' to determine the size and creation time of all files in all directories from base path: ")
    z = input()
    while '1' not in z:
        print(Fore.MAGENTA + "Enter '1' to determine the size and creation time of all files in all directories from base path: ")
    os.system('python determine_size.py')

# STEP 4 delete all files from organized-downloads and sub directories within
    print(Fore.WHITE + "Enter '1' to delete all files from the organized-downloads folder and sub directories within: ")
    w = input()
    while '1' not in w:
        print(Fore.WHITE + "Enter '1' to delete all files from the organized-downloads folder and sub directories within: ")
    os.system('python delete_files_from_folders.py')

main()