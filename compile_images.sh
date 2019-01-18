#!/bin/bash

# use imagemagick to annotate the image by its name 
# then compile all images into one for each loci

# bn_both is the 'anchor sample'

locs=`ls *bn_both.png |sed "s/bn_both.png//"`

for l in $locs; do
	for i in `ls $l*`; do
		j=`echo $i |sed "s/png/jpg/"` 
		montage -label "%t" $i -tile 1x1 -geometry +0+0 -pointsize 36 -border 5  -bordercolor "grey" $j 
	done;
	montage $l*jpg -tile 4x3 -geometry 400x400+20+2  compiled_$l.png
	rm $l*.jpg
done;

