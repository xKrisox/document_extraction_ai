#import NumPy
import PIL.Image
import cv2
import pytesseract
from pdfminer.high_level import extract_pages, extract_text
import re
from pdf2image import convert_from_path

pdf_file = open("document_extraction_ai/test_jednostkowy.pdf")

pages = convert_from_text(pdf_file, dpi=300)
for i, page in enumerate(pages, 1):
    ocr_text = pytesseract.image_to_string(page)
    print(f"--- Page {i} OCR ---")
    print(ocr_text)

