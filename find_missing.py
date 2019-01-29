#!/usr/bin/env python3
import time
import sys
import re
import os
import math

## check if all the files have been saved
chrtocheck=[6]

samples={'lewssnhsd':'bGV3c25oc2RfMDUwOF9sb3VwZS5sb3VwZQ==',
'bn_both'  : 'Ym5fYm90aF9sb3VwZS5sb3VwZQ==',
'wmi':       'd21pX2xvdXBlLmxvdXBl',
'wli':       'd2xpX2xvdXBlLmxvdXBl',
'lewcrl': 'bGV3Y3JsXzA1MDdfbG91cGUubG91cGU=',
'f344nhsd':'ZjM0NG5oc2RfNTA2X2xvdXBlLmxvdXBl',
'f344ncrl':'ZjM0NG5jcmxfMDUwNF9sb3VwZS5sb3VwZQ==',
'f344cucrl':'ZjM0NGR1Y3JsX2xvdXBlLmxvdXBl',
'bn_male':'Ym5fbWFsZV9sb3VwZS5sb3VwZQ==',
'bn_eve' :'Ym5fZXZhX2xvdXBlLmxvdXBl'
}

chrlen={'chr1': 282.76,
'chr2': 266.44,
'chr3': 177.7,
'chr4': 184.23,
'chr5': 173.71,
'chr6': 147.99,
'chr7': 145.73,
'chr8': 133.31,
'chr9': 122.1,
'chr10': 112.63,
'chr11': 90.46,
'chr12': 52.72,
'chr13': 114.03,
'chr14': 115.49,
'chr15': 111.25,
'chr16': 90.67,
'chr17': 90.84,
'chr18': 88.2,
'chr19': 62.28,
'chr20': 56.21,
'chrX': 159.97,
'chrY': 3.31,
'chrUn_random': 88.16,
'chrMT': 0.02}

strain='bn_both'
serverRoot="http://hchen3:3000/loupe/view/"

def check(chr):
    missing=""
    whichchr="chr"+str(chr)
    baselength=chrlen[whichchr]*1000000
    resolu=500000
    images=math.ceil(baselength/resolu)
    print (whichchr + ": "+ str(images) + " images")
    for cnt in range(images):
        xstart=cnt*resolu+1
        xend=xstart+resolu-1
        xchr=whichchr + ":"  + str(xstart) + "-" + whichchr + ":" + str(xend)
        xy=xchr + ";" + xchr
        filename=whichchr + "_" + str(xstart).zfill(11) + "-" + str(xend).zfill(11) + "_" + strain  + ".png"
        if not os.path.isfile(filename):
            print("missing " + str(cnt)+ " genomic region:" + xy )
            missing = missing + str(cnt) +", "
    return missing

for i in chrtocheck:
    downloadDir="/home/hao/Downloads/chr" +  str(i) + "/"
    result=check(i)
    print (result)


