import fitz
import os
from PIL import Image
from docx import Document
from pypdf import PdfReader

B =PdfReader('book.pdf')
print(len(B.pages))
for i in range(len(B.pages)):
    page = B.pages[i]
    text = page.extract_text()
def save_text_to_docx(text, docx_path):
    doc = Document()
    for i in text:
        doc.add_paragraph(text)
    doc.save(docx_path)
save_text_to_docx(text, 'book.DOCX')
print("Text saved to 'book.DOCX'.")


file_path = 'book.pdf'
pdf_file = fitz.open(file_path)
page_nums = len(pdf_file)
image_list = []
for page_num in range(page_nums):
    page_content =pdf_file[page_num]
    image_list.extend(page_content.get_images())

print(image_list)

for i, Image in enumerate(image_list,start=1):
    xref = Image[0]
    base_image = pdf_file.extract_image(xref)
    image_bytes = base_image['image']
    image_ext = base_image['ext']
    image_name = str(i) + '.' + image_ext
    with open(os.path.join('images/',image_name),'wb') as image_file:
        image_file.write(image_bytes)
        image_file.close
