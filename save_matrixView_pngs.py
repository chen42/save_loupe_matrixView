from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import sys
import re
import os


samples={'lewssnhsd':'bGV3c25oc2RfMDUwOF9sb3VwZS5sb3VwZQ==',  
'bn_both'  : 'Ym5fYm90aF9sb3VwZS5sb3VwZQ=='}

downloadDir="/home/hao/Downloads/"
serverRoot="http://hchen3:3000/loupe/view/"

options=Options()
options.headless=True
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', downloadDir)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', "image/png,image/jpeg")
browser = webdriver.Firefox(firefox_profile=profile, options=options)

with open(sys.argv[1], 'r') as xys:
    for xy in xys:
        xy=xy.rstrip()
        xy=re.sub(r',', '', xy)
        filexy=xy
        xchr=re.search('(chr.*?:)', xy)
        xy=re.sub(r'-','-'+xchr.group(1), xy)
        xy=re.sub(r':', '%2B', xy)
        xy=re.sub(r';', '&y=', xy)
        filexy=re.sub(r':', '_', filexy)
        filexy=re.sub(r';', '_', filexy)
        for sample in samples:
            url=serverRoot + samples[sample] + '/matrix?x='+ xy
            print (url)
            browser.get(url)
            time.sleep(10) # set it to allow the image to load into the browser
            elem = browser.find_element_by_id('save_image_as_png')  # find the save button 
            elem.click() # and click it
            movecommand="mv " + downloadDir + "loupe-sv-barcode-matrix.png "  + filexy + "_" + sample + ".png"
            os.system(movecommand)

browser.quit()
