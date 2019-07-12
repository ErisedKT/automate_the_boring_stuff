#! /usr/bin/python
# pdfParanoia.py - Encrypts or decrypts every PDF in a folder and its subfolders with a password. 

# Usage: ./pdfParanoia.py encrypt <folder> <password> 
#        ./pdfParanoia.py decrypt <folder> <password>

import os, PyPDF2, sys

def encryptAll(foldername, password):
    # Convert foldername into an absolute path and check that it exists.
    foldername = os.path.abspath(foldername)
    if not os.path.exists(foldername):
        raise Exception('The folder you entered could not be found!')
    
    # Search through folder and subfolders for PDFs.
    for folderName, subfolders, filenames in os.walk(foldername):
        print('Current folder is: ' + folderName)

        # Loop through all files in the folder.
        for filename in filenames:
            filePath = os.path.join(folderName, filename)
            # Check if file is a PDF.
            if not filename.endswith('.pdf'):
                continue
            
            pdfReader = PyPDF2.PdfFileReader(open(filePath, 'rb'))
            pdfWriter = PyPDF2.PdfFileWriter()

            # Loop through all the pages in the file.
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))

            # Encrypt the file.
            pdfWriter.encrypt(password)
            encrypted_filename = filename[:-4] + '_encrypted.pdf'
            os.chdir(folderName)

            # Write the encrypted PDF to another file.
            resultPdf = open(encrypted_filename, 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()
            pdfReader = PyPDF2.PdfFileReader(open(os.path.join(folderName, encrypted_filename), 'rb'))

            # Delete original PDF if file encryption was successful.
            if pdfReader.decrypt(password) == 1:
                os.remove(filePath)
            else:
                print('Unsuccessful encryption of: ' + filename)

def decryptAll(foldername, password):
    # Convert foldername into an absolute path and check that it exists.
    foldername = os.path.abspath(foldername)
    if not os.path.exists(foldername):
        raise Exception('The folder you entered could not be found!')
    
    # Search through folder and subfolders for PDFs.
    for folderName, subfolders, filenames in os.walk(foldername):
        print('Current folder is: ' + folderName)

        # Loop through all files in the folder.
        for filename in filenames:
            filePath = os.path.join(folderName, filename)
            # Check if file is an encrypted PDF.
            if not filename.endswith('.pdf'):
                continue
            else:
                pdfReader = PyPDF2.PdfFileReader(filePath, 'rb')
                if not pdfReader.isEncrypted:
                    continue

            pdfWriter = PyPDF2.PdfFileWriter()
            # Decrypt the file and loop through all the pages in it.
            if pdfReader.decrypt(password) == 1:
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
            else:
                print('Unsuccessful decryption of:', filename)

            decrypted_filename = filename[:-4] + '_decrypted.pdf'
            os.chdir(folderName)

            # Write the decrypted PDF to another file.
            resultPdf = open(decrypted_filename, 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()

            # Delete original PDF.
            os.remove(filePath)

if sys.argv[1] == 'encrypt':
    encryptAll(sys.argv[2], sys.argv[3])
elif sys.argv[1] == 'decrypt':
    decryptAll(sys.argv[2], sys.argv[3])
else:
    print('Usage: ./pdfParanoia.py <encrypt/decrypt> <folder> <password>')