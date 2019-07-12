#! /usr/bin/python
# pdfPasswordBreaker.py - Brute-force password breaker for PDFs.

import PyPDF2, os

def crack(pdfName):
    pdfFile = open(pdfName, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    if pdfReader.isEncrypted:
        dictFile = open('dictionary.txt')
        words = [word.strip('\n') for word in dictFile.readlines()]
        found = False
        for word in words:
            upper = pdfReader.decrypt(word)
            lower = pdfReader.decrypt(word.lower())
            if upper == 1 or lower == 1:
                if upper == 1:
                    password = word
                else:
                    password = word.lower()
                print('Password found:', password)
                pdfWriter = PyPDF2.PdfFileWriter()
                for numPage in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(numPage))
                del pdfReader
                pdfFile.close()
                decryptedFile = open(pdfName, 'wb')
                pdfWriter.write(decryptedFile)
                decryptedFile.close()
                print('Decryption successful!')
                found = True
                break
        if not found:
            print('Password not found.')
    else:
        print('This file is not encrypted.')

crack('pdf_encrypted.pdf')