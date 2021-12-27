#! python3
# combinePdfs.py- Combines all the PDFs in the current working directory  into a single PDF

import PyPDF2, os

cwd = os.getcwd() # Gets the current working directory

exclPage = int(input('Enter the number of pages in the beginning of each document that should be excluded: '))
outName = input('Enter the name of the output file: ')
print('Combining files in ' + cwd) 

# Get all the PDF filenames
pdfFiles = []
i = 0
for filename in os.listdir('.'):
    if filename.endswith('.pdf') and filename[:4] == 'Inlu': # Specify the first letters in the files to be combined
        pdfFiles.append(filename)
        i += 1

pdfFiles.sort(key = str.lower) # sorts the files in alphabetical order

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the  pages in each PDF-file, excluding those specified 
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(exclPage,pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
        
pdfOutput = open(outName, 'wb') # opens the output file
pdfWriter.write(pdfOutput)  # writes the file
pdfOutput.close()

print('Number of files merged: ' + str(i) + '. The merged files are stored in: ' +  outName)