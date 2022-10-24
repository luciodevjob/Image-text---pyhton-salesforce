from email.mime import image
import cv2
import pytesseract

imagem = cv2.imread("lucio.png")
imgCroppedNome = imagem[0:60, 0:740]


Nome = pytesseract.image_to_string(imgCroppedNome, lang="por")
print(Nome)
#print(contato)