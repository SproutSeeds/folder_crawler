# look into the seek method
# https://stackoverflow.com/questions/8816059/create-file-of-particular-size-in-python

import os, time, glob
from pprint import pprint

directory_name = BASE_PATH = os.path.expanduser('~/organized-downloads')
list_of_files = filter(os.path.isfile, glob.glob(directory_name + '/**/*', recursive=True))
file_dictionary = dict()

for f in list_of_files:
    filename = f.split('/')[-1]
    file_dictionary[filename] = dict(size = os.stat(f).st_size, creation_time=time.ctime(os.stat(f).st_ctime))
    # file_dictionary[f'{f.split("/").pop()}'] = dict(size = os.stat(f).st_size, creation_time=time.ctime(os.stat(f).st_ctime))
pprint(file_dictionary)