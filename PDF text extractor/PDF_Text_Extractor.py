import PyPDF2

pdf_file_obj = open("C:/Users/KIIT/Desktop/KIIT_me/SEM 5/CN/week 11.pdf",'rb')

pdf_file_reader = PyPDF2.PdfFileReader(pdf_file_obj)

print(pdf_file_reader.numPages)

page_obj = pdf_file_reader.getPage(2)

page_text = page_obj.extract_text()

print(page_text)

pdf_file_obj.close()
