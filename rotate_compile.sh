#!/bin/bash

# use imagemagick to annotate the image by its name, rotate 45 degrees,
# then compile all images into one for each chromosome

# change the following line to match your files.

imgs=`ls chr20*bnboth.png`

cnt=0

for i in $imgs; do
	cnt=$(( $cnt + 5 ))
	cntd=`bc -l <<< " scale =1; $cnt / 10"`	
	loc="$cntd\_MB"	
	echo $loc
	j=`echo $i |sed "s/png/jpg/"` 
	echo $j
	montage -rotate 45  -geometry 1200x1200+0+0 $i png:- |convert -  -crop  1170x1170+150+400 png:- |convert - -pointsize 46 -font Times-Bold -annotate +900+1100  `echo $loc`  crop_$j 
done;

## change the bn*jpg to match your files
montage crop_*jpg -tile 12x6 -geometry 200x200-2+0  compiled_chr20.png

