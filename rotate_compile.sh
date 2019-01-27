#!/bin/bash

# use imagemagick to annotate the image by its name, rotate 45 degrees,
# then compile all images into one for each chromosome

# change the following line to match your files.

for chrs in {1..8} ; do
	chr="chr$chrs"
	imgs=`ls $chr\_*bn_male.png`
	cnt=0
	for i in $imgs; do
		cnt=$(( $cnt + 5 ))
		cntd=`bc -l <<< " scale =1; $cnt / 10"`	
		loc="$cntd\_MB"	
		j=`echo $i |sed "s/png/jpg/"` 
		echo $j
		if [ ! -f crop_$j ] ; then 
			montage -rotate 45  -geometry 1200x1200+0+0 $i png:- |convert -  -crop  1170x1170+150+400 png:- |convert - -pointsize 64 -font Times-Bold -annotate +900+1100  `echo $loc`  crop_$j 
		fi
	done;
	montage crop_$chr\_*jpg -tile 10x4 -geometry 200x200-2+0  compiled_$chr\_bnmale.pdf
done
