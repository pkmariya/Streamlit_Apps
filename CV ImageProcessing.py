import cv2

img = cv2.imread('/Users/mariya/pers/Development/Python/Computer Vision/IMG_4045.PNG')

cv2.imwrite('/Users/mariya/pers/Development/Python/Computer Vision/CopyOfAlexa.PNG', img)

cv2.imshow("Alexa Transformed", img)
cv2.waitKey(3000)

cv2.destroyAllWindows()