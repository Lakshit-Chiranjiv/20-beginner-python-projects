import PyPDF2
import pyttsx3

pdf_file_obj = open("C:/Users/KIIT/Desktop/KIIT_me/SEM 5/CN/week 11.pdf",'rb')

pdf_file_reader = PyPDF2.PdfFileReader(pdf_file_obj)

page_obj = pdf_file_reader.getPage(2)

page_text = page_obj.extract_text()

print(page_text)

speak_obj = pyttsx3.init()
speak_obj.say(page_text)
speak_obj.runAndWait()

pdf_file_obj.close()
