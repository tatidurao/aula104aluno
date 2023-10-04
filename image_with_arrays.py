import numpy as np
import cv2

#LINHAS E COLUNA
black = np.zeros([100,100])
#print(black)

#[linha_inicial : linha_final, coluna_inicial : coluna_final]

#row = black[1:3]
#print(row)

#col = black[ :,1:3]
#print(col)

black[40:60, 10:30] = 255


cv2.imshow("preto",black)
cv2.waitKey(0)
