import os
import pandas as pd
from random import randint

## set the chr here
chrname="chr7"

#based on pixel position of matrix view
startPixel=144
endPixel=1168
pixelPerBase=(endPixel-startPixel)/500000
#unk: beige; del grey, inv red, dup:blue 
svcolor={"unk": "#dac29215",
         "del": "#22222215",
         "inv": "#ee222215",
         "dup": "#2222ee15"}

def drawbox(imgName, x1, x2, bp1, bp2, svtype):
    svImgName="sv_"+imgName
# you can redo one specific image if needed:
#    if svImgName!="sv_chr1_00036000001-00036500000_bn_both.png":
#        return
    if not os.path.exists(svImgName):
        os.system("cp allPng/" +  img + " " +svImgName)
    text=svtype+" " + str(int(bp1))+"-"+str(int(bp2))
    col=svcolor[svtype]
    x=200+randint(0,100)
    y=400+randint(0,200)
    os.system("mogrify " +  svImgName +   " -fill \""+ col + "\" -draw \"rectangle " + str(x1) + ",0 " +  str(x2) + ",1024\" " +  " -pointsize 24 -fill \"#00000004\" -gravity southwest -draw \"rotate 315 text " + str(x) + "," + str(y) +"\'" + text + "\'\" " +  svImgName)


filename=chrname+"_svs.tab"
df=pd.read_csv(filename, delimiter="\t", header=None)
for row, cols in df.iterrows():
    chrom=cols[1]
    if chrom == chrname: #just checking to make sure
        svtype=cols[0]
        bpStart=cols[2]
        bpEnd=cols[3]
        imgStart=int(bpStart/500000)
        imgEnd=int(bpEnd/500000)
        pixelStart=startPixel+(bpStart-imgStart*500000)*pixelPerBase
        pixelEnd=startPixel+(bpEnd-imgEnd*500000)*pixelPerBase
        chrstart=imgStart*500000+1
        chrend=(imgEnd+1)*500000
        if (imgEnd-imgStart==0):
            img= chrname+ "_" +  str(chrstart).zfill(11) + "-" + str(chrend).zfill(11) +  "_bn_both.png"
            print (chrname+ ":"+ str(bpStart) + "-" + str(bpEnd) )
            drawbox(img, pixelStart, pixelEnd, bpStart, bpEnd, svtype)
        elif (imgEnd-imgStart==1):
            print (chrname+ ":"+ str(bpStart) + "-" + str(bpEnd) )
            chrend1=chrend-500000
            img= chrname+ "_" +  str(chrstart).zfill(11) + "-" + str(chrend1).zfill(11) +  "_bn_both.png"
            drawbox(img, pixelStart, endPixel, bpStart, bpEnd, svtype )
            chrstart1=chrend1+1
            img= chrname+ "_" +  str(chrstart1).zfill(11) + "-" + str(chrend).zfill(11) +  "_bn_both.png"
            drawbox(img, startPixel, pixelEnd, bpStart, bpEnd, svtype)
