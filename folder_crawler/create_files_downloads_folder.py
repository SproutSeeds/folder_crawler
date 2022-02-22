import os
import random

EXTENSIONS = ['mp3', 'wav', 'raw', 'wma', 'mid', 'midi',
'mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'mwv', 'm4v', 'h264',
'png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'psd', 'svg', 'tiff', 'tif',
'txt', 'pdf', 'csv', 'xls', 'xlsx', 'ods', 'doc', 'docx', 'html', 'odt', 'tex', 'ppt', 'pptx', 'log',
'zip', 'z', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb',
'dmg', 'exe', 'iso']
SIZES = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000, 3000000]

BASE_PATH = os.path.expanduser('~')
DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')

def touch(fname, times=None):
    with open(fname, 'wb') as f:
        f.seek(random.choice(SIZES)-1)
        f.write(b"\0")
        f.close()
        os.utime(fname, times)

if os.path.isdir(DOWNLOADS_PATH) and os.path.isdir(os.path.join(BASE_PATH, 'organized-downloads')):
    for f_ext in EXTENSIONS:
        touch(os.path.join(DOWNLOADS_PATH, 'a.' + f_ext))
else:
    os.mkdir('Downloads')
    os.mkdir('organized-downloads')

print("Created dummy files of different sizes in Downloads Folder.")

# with open('log_file.txt','a') as f:
#     f.write("Created dummy files of different sizes in Downloads Folder")
