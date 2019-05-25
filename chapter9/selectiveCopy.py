#! /usr/bin/python3
# selectiveCopy.py - Copies files in a folder with a certain file
# extension into another folder

import zipfile, os, shutil

def selectiveCopy(folder, ext, location):
    folder = os.path.abspath(folder)
    location = os.path.abspath(location) 

    newFoldername = os.path.basename(folder) + '_' + ext[1:]
    newFolderPath = os.path.join(location, newFoldername)
    os.makedirs(newFolderPath)

    for foldername, subfolders, filenames in os.walk(folder):
        print('Looking inside %s...' % (foldername))
        for filename in filenames:
            if filename.endswith(ext):
                shutil.copy(os.path.join(foldername, filename), newFolderPath)

selectiveCopy('/home/sanya/Desktop/Everything\'s_in_here', '.pdf', '/home/sanya/atbswp/chapter9')
