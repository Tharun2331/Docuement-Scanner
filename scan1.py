# import numpy as np
# import imutils
# import cv2
# import argparse
# from skimage.filters import threshold_local
# from pyimagesearch.transform import four_point_transform


# ap = argparse.ArgumentParser()
# ap.add_argument("-i","--image",required=True,help=" go to image directory")
# args= vars(ap.parse_args())

# image = cv2.imread(args["image"])
# ratio = image.shape[0] / 500.0
# orig = image.copy()
# image = imutils.resize(image,height=500)


# gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# gray= cv2.GaussianBlur(gray,(5,5),0)
# edged= cv2.Canny(gray,70,200)

# print("Step1: Edge detection")
# cv2.imshow("gray",edged)
# cv2.imshow("image",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# cnts = cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:5]
# for c in cnts:
#     peri = cv2.arcLength(c,True)
#     approx=cv2.approxPolyDP(c,0.02 * peri,True)

#     if len(approx) == 4:
#         scrn = approx
#         break
# print("Step2: Finding contours")
# cv2.drawContours(image,[scrn],-1,(0,255,0),2)
# cv2.imshow("outline",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# warped = four_point_transform(orig,scrn.reshape(4,2)*ratio)
# warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
# T = threshold_local(warped, 11, offset = 10, method = "gaussian")
# warped = (warped > T).astype("uint8") * 255

# print("Step 3: Apply perspective transform")
# cv2.imshow("orig",imutils.resize(orig,height=600))
# cv2.imshow("image",imutils.resize(warped,height=600))
# cv2.waitKey(0)
