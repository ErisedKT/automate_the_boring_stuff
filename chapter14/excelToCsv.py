#! /usr/bin/python
# excelToCsv.py - Converts all the Excel files in the current working directory and outputs them as 
# CSV files.

import os, openpyxl, csv

for filename in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    if not filename.endswith('.xlsx'):
        continue
    wb = openpyxl.load_workbook(filename)
    for sheetName in wb.get_sheet_names():
        # Loop through every sheet in the workbook.
        sheet = wb.get_sheet_by_name(sheetName)

        # Create the CSV filename from the Excel filename and sheet title.
        csvFilename = filename[:-5] + '_' + sheetName + '.csv'
        # Create the csv.writer object for this CSV file.
        csvFile = open(csvFilename, 'w')
        csvWriter = csv.writer(csvFile)
        
        # Loop through every row in the sheet.
        for row in sheet.rows:
            rowList = [cellObj.value for cellObj in row]
            csvWriter.writerow(rowList)
        
        csvFile.close()