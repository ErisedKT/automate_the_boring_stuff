#! /usr/bin/python3
# fillingInTheGaps.py - Finds all files with a given prefix in a folder
# and renames later files to close gaps in the numbering

import os, shutil, re

def fillGaps(folder, prefix):

    # Make sure folder is an absolute path.

    folder = os.path.abspath(folder)

    # Obtain contents of folder.

    contents = os.listdir(folder)
    prefixedFiles = []

    # Put files with prefix in a separate sorted list.

    for item in contents:
        itemPath = os.path.join(folder, item)
        if not os.path.isfile(itemPath) or not item.startswith(prefix):
            continue
        prefixedFiles.append(item)
    prefixedFiles.sort()

    # Create regex to find numbers and trailing text in filenames.

    numberRegex = re.compile(r'(0*)(\d+)(.*)$')
    mo = numberRegex.search(prefixedFiles[0])


    index = int(mo.group(2)) + 1  # index to track numbered files
    leadingZeroes = len(mo.group(1))
    # Loop through numbered files.

    for numFile in prefixedFiles[1:]:
        mo = numberRegex.search(numFile)
        number = int(mo.group(2))   # numbered part of file

        # Fill in missing indices for gaps in numbered files.

        if number != index:
            zeroes = mo.group(1)

            # Find number of trailing zeroes to include in new filename.

            if len(mo.group(1)) < leadingZeroes and len(str(index)) < len(str(number)):
                zeroes += '0' * (len(str(number)) - len(str(index))) 

            # Find new filename with corrected index.

            newName = prefix + zeroes + str(index) + \
                mo.group(3)
            newPath = os.path.join(folder, newName)

            # Rename file with corrected filename.

            shutil.move(os.path.join(folder, numFile), newPath)
        
        index += 1   # increment index

def insertGaps(folder, prefix, index):

    # Make sure folder is an absolute path.

    folder = os.path.abspath(folder)

    # Obtain contents of folder.

    contents = os.listdir(folder)
    prefixedFiles = []

    # Put files with prefix in a separate sorted list.

    for item in contents:
        itemPath = os.path.join(folder, item)
        if not os.path.isfile(itemPath) or not item.startswith(prefix):
            continue
        prefixedFiles.append(item)
    prefixedFiles.sort(reverse=True)

    numberRegex = re.compile(r'(0*)(\d+)(.*)$')
    mo = numberRegex.search(prefixedFiles[0])
    listIndex = int(mo.group(2)) - int(index.lstrip('0'))

    for numFile in prefixedFiles[:listIndex+1]:
        mo = numberRegex.search(numFile)
        index = mo.group(1) + str(int(mo.group(2)) + 1)
        newName = prefix + index + mo.group(3)
        newPath = os.path.join(folder, newName)
        shutil.move(os.path.join(folder, numFile), newPath)
        
insertGaps('/home/sanya/atbswp/chapter9/spam', 'spam', '004') 