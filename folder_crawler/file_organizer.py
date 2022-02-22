# STEP 1
# Import os to get access to our operating system module to access our file system commands
import os
# To create a data structure to map all files within the downloads folder we use the collections module
import collections
# pretty print to make things more visually pleasant
from pprint import pprint

# defining all file extensions in their own list
EXT_AUDIO = ['mp3', 'wav', 'raw', 'wma', 'mid', 'midi']
EXT_VIDEO = ['mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'mwv', 'm4v', 'h264']
EXT_IMGS  = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'psd', 'svg', 'tiff', 'tif']
EXT_DOCS  = ['txt', 'pdf', 'csv', 'xls', 'xlsx', 'ods', 'doc', 'docx', 'html', 'odt', 'tex', 'ppt', 'pptx', 'log']
EXT_COMPR = ['zip', 'z', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb']
EXT_INSTL = ['dmg', 'exe', 'iso']

# Defining the base path using attributes off of the OS module
BASE_PATH = os.path.expanduser('~')
# defining the destination directories
DEST_DIRS = ['organized-downloads/Music', 'organized-downloads/Movies', 'organized-downloads/Pictures', 'organized-downloads/Documents', 'organized-downloads/Applications', 'organized-downloads/Other']

# loops through the destination directory list
# the direct path to the destination directory is created by joining the base path constant we created
# with the destination directory portion
for d in DEST_DIRS:
    dir_path = os.path.join(BASE_PATH, d)
    # This will check to see if this direct path exists, if it doesn't the mkdir method will create it.
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
######################################################
# STEP 2
DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')
# creates a dictionary data structure we can map all our files to
files_mapping = collections.defaultdict(list)
# collects all file names and puts it into a list
files_list = os.listdir(DOWNLOADS_PATH)

# Loops through the file names in the files_list, splits them at the '.' and extracts the fie extension
# Defines the key as the extension type and the value as an appended value of
# the full file name that has that extension type.
for file_name in files_list:
    if file_name[0] != '.':
        file_ext = file_name.split('.')[-1]
        files_mapping[file_ext].append(file_name)

# Prints out the mapped files to a dictionary of key/list-values
# pprint(files_mapping)

# Step 3
# Loops through the key/values in the files_mapping dictionary
for f_ext, f_list in files_mapping.items():
    # checks to see if this extension is in this list, if so, then we loop through all files of this
    # extension type and rename them to the destination folder with the os.rename() method
    if f_ext in EXT_VIDEO:
        for file in f_list:
            # rename() method takes two arguments, path of file currently and the destination path
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'organized-downloads/Movies', file))

    elif f_ext in EXT_INSTL:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'organized-downloads/Applications', file))

    elif f_ext in EXT_AUDIO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'organized-downloads/Music', file))

    elif f_ext in EXT_IMGS:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'organized-downloads/Pictures', file))

    elif f_ext in EXT_DOCS or f_ext in EXT_COMPR:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'organized-downloads/Documents', file))

    else:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'organized-downloads/Other', file))

print("Organized all files into the ~/organized-downloads folder.")