# This script will delete all files in folders quickly to show example of automation

import os
from pprint import pprint

BASE_PATH = os.path.expanduser('~')
DEST_DIRS = ['organized-downloads/Music', 'organized-downloads/Movies', 'organized-downloads/Pictures', 'organized-downloads/Documents', 'organized-downloads/Applications', 'organized-downloads/Other']


for d in DEST_DIRS:
    files_list = os.listdir(os.path.join(BASE_PATH, d))
    # pprint(files_list)
    for file in files_list:
        os.remove(os.path.join(BASE_PATH, d, file))
        # pprint(os.path.join(BASE_PATH, d, file))
