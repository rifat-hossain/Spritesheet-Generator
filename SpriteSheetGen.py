from os import listdir
from os.path import isfile, join
import cv2
import numpy as np

def insert_img(start_pos, sheet, img, hh, hw):
    offset = [int((hh - img.shape[0])/2), int((hw - img.shape[1])/2)]
    start_pos = [start_pos[0] + offset[0], start_pos[1] + offset[1]]
    sheet[start_pos[0]:start_pos[0]+img.shape[0],start_pos[1]:start_pos[1]+img.shape[1]] = img
    return sheet
direc = input("Enter directory: ")
onlyfiles = [f for f in listdir(direc) if isfile(join(direc, f))]
print("Files to work on",onlyfiles)
hh = 0
hw = 0
hc = 0
for filename in onlyfiles:
    try:
        h, w, c = cv2.imread(direc + "/" + filename, cv2.IMREAD_UNCHANGED).shape
        if hh < h:
            hh = h
        if hw < w:
            hw = w
        if hc < c:
            hc = c
    except:
        print(filename,"is not an image.")
        onlyfiles.remove(filename)
sh = int(input("Enter Sprite Sheet height: "))
sw = hw * len(onlyfiles)
s_sheet = np.zeros((hh,sw,hc),dtype=float)
for n in range(0,len(onlyfiles)):
    s_sheet = insert_img([0,n * hw], s_sheet, cv2.imread(direc + "/" + onlyfiles[n], cv2.IMREAD_UNCHANGED),hh,hw)
ratio = sh / hh
resized = cv2.resize(s_sheet, (int(ratio * sw),sh))
cv2.imwrite(direc + "/ss/spritesheet.png",resized)