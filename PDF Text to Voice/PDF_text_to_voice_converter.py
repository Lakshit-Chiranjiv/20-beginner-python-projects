import PyPDF2
import pyttsx3

pdf_file_obj = open("C:/Users/KIIT/Desktop/KIIT_me/SEM 5/CN/week 11.pdf",'rb')

pdf_file_reader = PyPDF2.PdfFileReader(pdf_file_obj)

page = 1
speak_obj = pyttsx3.init()
while page <= pdf_file_reader.numPages:
    page_obj = pdf_file_reader.getPage(page)

    page_text = page_obj.extract_text()

    # print(page_text)
    speak_obj.say(page_text)
    speak_obj.runAndWait()
    speak_obj.say('Page complete, moving to next page')
    speak_obj.runAndWait()
    page += 1

pdf_file_obj.close()
