import PyPDF2

File1 = open('Cross-problems_6.pdf', 'rb')
File2 = open('Cross-problems_7.pdf', 'rb')

f1Reader = PyPDF2.PdfFileReader(File1)
f2Reader = PyPDF2.PdfFileReader(File2)
pdfWriter = PyPDF2.PdfFileWriter()  # representerar blank pdf

for pageNum in range(f1Reader.numPages):
    pageObj = f1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    
    
for pageNum in range(f2Reader.numPages):
    pageObj = f2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    
pdfOutput  = open('together.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

File1.close()
File2.close()