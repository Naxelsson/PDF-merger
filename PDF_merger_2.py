import PyPDF2

File1 = open('first_file.pdf', 'rb')
File2 = open('second_file.pdf', 'rb')

f1Reader = PyPDF2.PdfFileReader(File1)
f2Reader = PyPDF2.PdfFileReader(File2)
pdfWriter = PyPDF2.PdfFileWriter()  # represents blank pdf

for pageNum in range(f1Reader.numPages):
    pageObj = f1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    
    
for pageNum in range(f2Reader.numPages):
    pageObj = f2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    
pdfOutput  = open('together.pdf', 'wb') # creates a new file with the merged pdfs
pdfWriter.write(pdfOutput)
pdfOutput.close()

File1.close()
File2.close()
