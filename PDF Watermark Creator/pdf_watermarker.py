from pikepdf import Pdf, Page, Rectangle
import os

os.chdir('C:/Users/KIIT/Desktop/ALL CODE ND STUFFS/PROJECTS-REPOS/Python Folder/mini-python-projects/PDF Watermark Creator')

def add_watermark(input_pdf, output_pdf, watermark):
    pdf_to_watermark = Pdf.open(input_pdf)
    watermark_pdf = Pdf.open(watermark)
    watermark_page = Page(watermark_pdf.pages[0])

    for page in pdf_to_watermark.pages:
        page.add_underlay(watermark_page, Rectangle(10, 10, 400, 400))

    pdf_to_watermark.save(output_pdf)

add_watermark('target.pdf', 'output.pdf', 'watermark.pdf')