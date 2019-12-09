import cv2 as cv
import os
import shutil

path="/home/ghy/PycharmProjects/Remove_blurred_pictures/images/"

if not os.path.isdir(path+"/backup"):
    os.mkdir(path+"/backup")

for fpath, dirs, fs in os.walk(path):
    for img in fs:
        try:
            image = cv.imread(path+img)
            img2gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            imageVar = cv.Laplacian(img2gray, cv.CV_64F).var()
            if imageVar < 30.0 :
                shutil.move(path+img,path+"/backup/"+img)
        except BaseException:
            continue