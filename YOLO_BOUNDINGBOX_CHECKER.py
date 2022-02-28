from tkinter import N
import cv2 
path="/home/priyanshu-vaaan/DATA/VIDS_ALL_DATA/EBIN_TRAINING/VIDS_Dasna/Frame_1_3.jpg"
image = cv2.imread(path)

textpath=("{}.txt").format(path.split(".j")[0])
classfile="/home/priyanshu-vaaan/DATA/VIDS_ALL_DATA/EBIN_TRAINING/classes.txt"

with open(classfile) as f:
    class_lines = f.readlines()

    
with open(textpath) as f:
    lines = f.readlines()
    
dh,dw,_=image.shape

def map_class(class_ID):
    class_name=class_lines[int(class_ID)]
    return class_name
    



for line in lines:
    line=line.split(" ")
    class_ID=line[0]
    x=float(line[1])
    y=float(line[2])
    w=float(line[3])
    h=float(line[4])


    l=int((x-w/2)*dw)    
    r=int((x+w/2)*dw)
    t=int((y-h/2)*dh)
    b=int((y+h/2)*dh)

    cv2.rectangle(image,(l,t),(r,b),(0,255,0),2)
    cv2.putText(image, map_class(class_ID).strip(), (int(l),int(t)), cv2.FONT_HERSHEY_SIMPLEX,2, (0,0,255),2)
    print(map_class(class_ID))

cv2.imshow('Features', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
