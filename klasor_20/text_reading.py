from PIL import Image
import pytesseract

# fotoğrafı açıyor
img = Image.open("D:\\Resimler\\text.png")
# fotoğraftan metni çıkarıyor
text = pytesseract.image_to_string(img,lang="eng")
print(text) 