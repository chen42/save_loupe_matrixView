#!/bin/bash

# use imagemagick to add the name of image

for i in `ls chr*png`; do
	j=`echo $i |sed "s/png/jpg/"` 
    montage -label "%t" $i -tile 1x1 -geometry +0+0 -pointsize 24 -border 5  -bordercolor "grey" $j 
done;

#montage *jpg -tile 3x3 -geometry 400x400+40+2  compiled.png
