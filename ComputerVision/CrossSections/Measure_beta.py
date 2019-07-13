#using python2.7
#Write by Delin Li, Schnable Lab @ CAU
#delin.bio@gmail.com
#Start 8:00 PM Jan 05, 2018
#updated 9:30 PM Jan 18, 2018 get rid of effect of white starch
import matplotlib
matplotlib.use('Agg')
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
from matplotlib import pyplot as plt
#from pathlib import Path
import imutils
import numpy as np
import argparse
import cv2
import re
import os

'''functions'''
def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

def BigArea(contours):
    Area=0
    j=0
    for i in range(0,len(contours)):
        c=contours[i]
        if cv2.contourArea(c)>Area:
            j=i
            Area=cv2.contourArea(contours[i])
    return(j)

def Str(c,orig):
    # compute the rotated bounding box of the contour
    box = cv2.minAreaRect(c)
    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    # order the points in the contour such that they appear
    # in top-left, top-right, bottom-right, and bottom-left
    # order, then draw the outline of the rotated bounding
    # box
    box = perspective.order_points(box)
    cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)
    # loop over the original points and draw them
    for (x, y) in box:
        cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)
    # unpack the ordered bounding box, then compute the midpoint
    # between the top-left and top-right coordinates, followed by
    # the midpoint between bottom-left and bottom-right coordinates
    (tl, tr, br, bl) = box
    (tltrX, tltrY) = midpoint(tl, tr)
    (blbrX, blbrY) = midpoint(bl, br)
    # compute the midpoint between the top-left and top-right points,
    # followed by the midpoint between the top-righ and bottom-right
    (tlblX, tlblY) = midpoint(tl, bl)
    (trbrX, trbrY) = midpoint(tr, br)
    # draw the midpoints on the image
    cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
    cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
    cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
    cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
    # draw lines between the midpoints
    cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),(255, 0, 255), 8)
    cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),(255, 0, 255), 8)
    # compute the Euclidean distance between the midpoints
    dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
    dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
    # compute the size of the object
    if dA>=dB:
        dimA = dA * pixelsPerMetric
        dimB = dB * pixelsPerMetric
    else:
        dimA = dB * pixelsPerMetric
        dimB = dA * pixelsPerMetric
    # draw the object sizes on the image
    #cv2.putText(orig, "{:.1f}in".format(dimA),
	#(int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
    #1.65, (255, 0, 0), 2)
    #cv2.putText(orig, "{:.1f}in".format(dimB),
    #    (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
    #    1.65, (255, 0, 0), 2)
    return(orig,dimA,dimB)



'''read in parameter'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
ap.add_argument("-o", "--output", required=True,
	help="output file")
args = vars(ap.parse_args())


'''read in '''
img=cv2.imread(args["image"])
#img=cv2.imread("../../seed/B73/1/B73_1_1.tif")

row, col =img.shape[0:2]

original = img.copy()
'''The marker '''
#cropped = img[54:105,44:540,]
#cv2.imwrite("Marker_200um.png",cropped)
#marker=cv2.imread("Marker_200um.png")
#h1,w1=marker.shape[0:2]
#w1: 496 200/496

#res = cv2.matchTemplate(img,marker,cv2.TM_CCOEFF_NORMED)
#min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)

pixelsPerMetric= 0.4032258

for i in range(50,110):
    for j in range(40,580):
        img[i,j,]=(55,36,34)#(0,0,0)


'''The Seed'''
B,G,R= cv2.split(img)
gaussian = cv2.GaussianBlur(R.copy(), (7, 7), 1)
th, binary = cv2.threshold(gaussian,  70, 255,cv2.THRESH_BINARY);

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
dilated = cv2.dilate(binary, kernel)

contours, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
seed_c=contours[BigArea(contours)]

#plt.imshow(binary)
'''used in early version -> backup
Seed = cv2.Canny(binary, 100, 200)
Seed = cv2.dilate(Seed, None, iterations=1) #8
Seed = cv2.erode(Seed, None, iterations=1) #5
contours, hierarchy = cv2.findContours(Seed.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
seed_c=contours[BigArea(contours)]
'''
Area_seed=cv2.contourArea(seed_c) * pixelsPerMetric

embryo=np.full(img.shape,255,dtype=np.uint8)
cv2.drawContours(embryo, [seed_c], 0, (0, 0, 0), -1)

#create a copy for ouput to show different area and size
Draw_out=embryo.copy()
Draw_out,l_S,s_S=Str(seed_c,Draw_out)



''' To Do '''
#Mask the background as 0
'''
Mask=np.zeros(img.shape,dtype=np.uint8)
cv2.drawContours(Mask, [seed_c], 0, (255, 255, 255), -1)
Masked=np.minimum(Mask,original)
'''
Mask=np.full(img.shape,255,dtype=np.uint8)
cv2.drawContours(Mask, [seed_c], 0, (0, 0, 0), -1)
Masked=np.maximum(Mask,original)


'''The germ'''

#removed the effect of white starch
B,G,R= cv2.split(Masked)

th,RBin=cv2.threshold(R, 200, 1,cv2.THRESH_BINARY_INV)


HSV=cv2.cvtColor(Masked.copy(), cv2.COLOR_BGR2HSV)
th,S=cv2.threshold(HSV[:,:,1].copy() , 140, 1,cv2.THRESH_BINARY)

gaussian=HSV[:,:,0].copy()

th, binary = cv2.threshold(gaussian.copy(), 150, 255,cv2.THRESH_BINARY)

Combine=binary * RBin *S

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
Germ = cv2.dilate(Combine, kernel)

contours, _ = cv2.findContours(Germ.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
germ_c=contours[BigArea(contours)]

#mask the embryo as red
cv2.drawContours(Draw_out, [germ_c], 0, (0, 0, 255), -1)

Draw_out,l_G,s_G=Str(germ_c,Draw_out)
Area_germ= cv2.contourArea(germ_c) * pixelsPerMetric
if Area_germ > Area_seed*0.75:
    print("Possible un-expected error happens that germ accounts for more than 75% of seed:",args["image"])

if Area_germ < Area_seed*0.25:
    print("Possible un-expected error happens that germ accounts for less than 25% of seed:",args["image"])

out=[args["image"], row, col, Area_seed,l_S,s_S, Area_germ,l_G,s_G]

if os.path.exists(args["output"]) and os.path.getsize(args["output"]) > 0:
	with open(args["output"], "a") as fh:
		for item in out:
			fh.write("%s\t" % item)
		fh.write("\n")
	fh.close
else:
	with open(args["output"], "a") as fh:
		fh.write("file\trows\tcols\tSeedArea\tSeedLength\tSeedWidth\tEmbryoArea\tEmbryoLength\tEmbryoWidth\n")
		for item in out:
			fh.write("%s\t" % item)
		fh.write("\n")
	fh.close

'''output the final seed, embryo and their size'''
'''Compare before and after'''
outfig= "%s_%s" % ("Masked",re.sub(r'.*\/',r'',args["image"]))
plt.subplot(2,1,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(2,1,2),plt.imshow(cv2.cvtColor(Draw_out, cv2.COLOR_BGR2RGB))
plt.savefig(outfig)

