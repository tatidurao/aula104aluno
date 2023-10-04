import cv2

#imagens coloridas [[[40 148 75]]]
#preto e branco [[40 148 75]]
#binaria 101010101010101 [40 148 75]

#uma leitura da imagem
img = cv2.imread("butterfly.jpg")

#mostrar a imagem
#cv2.imshow("Imagem de exibição", img)
#print(img)

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("Imagem de exibição", gray_img)
print(gray_img)
cv2.waitKey(0)

