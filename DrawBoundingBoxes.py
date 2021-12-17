#Read image and label file and draw bounding boxes 
#Read image and label file 
import cv2 
from pathlib import Path

#give the image path
#make sure image and labe file is in the same directory if not give path seprately for label file in line 15
image_path="/home/vaaan/Desktop/IMAGE AUGMENTATION/3.1_Vehicles (1)/3.1_Vehicles/Labelled/DM/Data/A1_Frame_1514.0.jpg"
filename = Path(image_path)
image =cv2.imread(image_path)


#read label file
filename_replace_ext = filename.with_suffix('.txt')
la = open(Path(filename_replace_ext), "r")
dh,dw,_=image.shape

#make bounding boxes on yolo format 
with open (filename_replace_ext)as labels:
    for line in labels:
        ls = line.split(" ")
        x=float(ls[1])
        y=float(ls[2])
        w=float(ls[3])
        h=float(ls[4])
        
        l=int((x-w/2)*dw)    
        r=int((x+w/2)*dw)
        t=int((y-h/2)*dh)
        b=int((y+h/2)*dh)
        cv2.rectangle(image,(l,t),(r,b),(0,255,0),2)

#make bounding boxes on KITTI format
#with open (filename_replace_ext)as labels:
    #for line in labels:
    #    ls = line.split(" ")
    #    xmin=float(ls[5])
    #    ymin=float(ls[6])
    #    xmax=float(ls[7])
    #    ymax=float(ls[8])
    #    cv2.rectangle(image,(xmin,ymin),(xmax,ymax),(0,255,0),2)



cv2.imshow('Features', image)
cv2.waitKey(0)
cv2.destroyAllWindows()