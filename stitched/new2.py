import cv2 as cv2

dim=(1024,768)
left=cv2.imread('images/examples-task2/building1.jpg',cv2.IMREAD_COLOR)
right=cv2.imread('images/examples-task2/building2.jpg',cv2.IMREAD_COLOR)

#left=cv2.imread('images/examples-task2/1.jpg',cv2.IMREAD_COLOR)
#right=cv2.imread('images/examples-task2/2.jpg',cv2.IMREAD_COLOR)

#left=cv2.imread('images/examples-task2/S1.jpg',cv2.IMREAD_COLOR)
#right=cv2.imread('images/examples-task2/S2.jpg',cv2.IMREAD_COLOR)



left=cv2.resize(left,dim,interpolation = cv2.INTER_AREA)   #ReSize to (1024,768)
right=cv2.resize(right,dim,interpolation = cv2.INTER_AREA) #ReSize to (1024,768)

images=[]
images.append(left)
images.append(right)

stitcher = cv2.Stitcher.create()
ret,pano = stitcher.stitch(images)

if ret==cv2.STITCHER_OK:
    cv2.imshow('Panorama',pano)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("Error during Stitching")