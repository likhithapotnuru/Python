import cv2
#import pandas as pd
import colorsqlite

img_path = 'colorpic.jpg'
index = ['color','colorname','hex','R','G','B']
img = cv2.imread(img_path)
img = cv2.resize(img,(800,600))

def draw_function(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #print(x,y)
        b, g, r = img[y, x]
        #print(r,g,b)
        global a
        a = colorsqlite.displaycolorname(int(r), int(g), int(b))
        print(a[0])

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()