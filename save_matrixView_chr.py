#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import sys
import re
import os
import math
 
# save matrix view images for one chr

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

chrlen={ 'chr1': 282.76,
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
'MT': 0.02}


strain='bn_male'

downloadDir="/home/hao/Downloads/"
serverRoot="http://hchen3:3000/loupe/view/"
# disable the download dialog popup box
options=Options()
options.headless=True
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', downloadDir)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', "image/png,image/jpeg")

browser = webdriver.Firefox(firefox_profile=profile, options=options)

whichchr="chr19"
chrlen=chrlen[whichchr]*1000000
resolu=500000
images=math.ceil(chrlen/resolu)
print ("total " + str(images) + " images")

for cnt in range(images):
    xstart=cnt*resolu+1
    xend=xstart+resolu-1
    xchr=whichchr + ":"  + str(xstart) + "-" + whichchr + ":" + str(xend)
    xy=xchr + ";" + xchr
    print(str(cnt)+ " genomic region:" + xy )
    filename=whichchr + "_" + str(xstart).zfill(11) + "-" + str(xend).zfill(11) + "_" + strain  + ".png"
    xy=re.sub(r':', '%2B', xy)
    xy=re.sub(r';', '&y=', xy)
    url=serverRoot + samples[strain] + '/matrix?x='+ xy
    #print (url)
    browser.get(url)
    time.sleep(10) # set it to allow the image to load into the browser
    elem = browser.find_element_by_id('save_image_as_png')  # find the save button 
    elem.click() # and click it
    movecommand="mv " + downloadDir + "loupe-sv-barcode-matrix.png "  + filename
    os.system(movecommand)
    # somehow the browser fails to load after about 9 images and needs to be restarted
    if (cnt%8==7):
        browser.close() # this keeps the profile
        browser = webdriver.Firefox(firefox_profile=profile, options=options)
browser.quit() # now delete the profile


