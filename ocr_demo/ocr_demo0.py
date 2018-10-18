from PIL import Image
import pytesseract

#lang 参数可以多个，用 + 拼接，注意config 的参数配置
# text1 = pytesseract.image_to_string(Image.open('./ocr_demo/pic.png'), lang='normal+chi_sim', config="-psm 6")
text1 = pytesseract.image_to_string(Image.open('./ocr_demo/pic4.png'), lang='normal2', config="-psm 6")
print(text1)
