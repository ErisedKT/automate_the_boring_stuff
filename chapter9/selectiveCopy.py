#! /usr/bin/python3
# selectiveCopy.py - Copies files in a folder with a certain file
# extension into another folder

import zipfile, os, shutil

def selectiveCopy(folder, ext, location):

    # Make sure folder and locations are absolute paths.

    folder = os.path.abspath(folder)
    location = os.path.abspath(location) 

    # Create destination folder to place files in.

    newFoldername = os.path.basename(folder) + '_' + ext[1:]
    newFolderPath = os.path.join(location, newFoldername)
    os.makedirs(newFolderPath)

    # Walk through source folder.

    for foldername, subfolders, filenames in os.walk(folder):
        print('Looking inside %s...' % (foldername))

        for filename in filenames:

             # Check if any files in the current folder have the required extension.

            if filename.endswith(ext):

                # Copy files with the required extension to the destination folder.

                shutil.copy(os.path.join(foldername, filename), newFolderPath)

selectiveCopy('/home/sanya/Desktop/Everything\'s_in_here', '.pdf', '/home/sanya/atbswp/chapter9')
