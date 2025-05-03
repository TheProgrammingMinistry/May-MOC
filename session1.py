import cv2 as cv

image = cv.imread("May/retaurant 6.jpg")
gray_scale = cv.cvtColor(image,cv.COLOR_BGR2GRAY)


resize = cv.resize(gray_scale,(50,50),interpolation= cv.INTER_AREA)
cv.imshow("resize image",resize)
cv.imshow("Normal image",image)
cv.imshow("Gray image",gray_scale)

cv.waitKey(0)