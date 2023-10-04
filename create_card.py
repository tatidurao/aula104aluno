import cv2

img = cv2.imread("poster.jpg")
# linhas e colunas
rocket = img[100:400, 400:500]
#print(rocket)

img[0:300, 500:600] = rocket

text_to_show = "Eu amo programar na BYJUS FutureSchool"


cv2.putText(img,  
           text_to_show,
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.6,  
           color=(0,0,255)
           )
 
#cv2.imshow("Imagem de exibição", rocket) 

cv2.imshow("Imagem de exibição", img)

cv2.waitKey(0)