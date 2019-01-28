
rm svs.tab
for i in `ls *_sv.vcf`; do 
	echo $i
	grep SVTYPE2=DEL $i |grep -v random  |grep -P "call_\d+_1\t" |sed "s/:/\t/" |cut -f 1,2,6|sed "s/\[//" |awk '{print "del\t" $0}'>>svs.tab
	grep SVTYPE2=INV $i |grep -v random |grep -P "call_\d+_1\t" |sed "s/:/\t/" |cut -f 1,2,6|sed "s/\]//" |awk '{print "inv\t" $0}'>>svs.tab
	grep SVTYPE2=DUP $i |grep -v random |grep -P "call_\d+_2\t" |sed "s/:/\t/" |cut -f 1,2,6|sed "s/\[//" |awk '{print "dup\t" $0}'>>svs.tab
	grep "<DUP:TANDEM>" $i |grep -v "random" |sed "s/;/\t/" |cut -f 1,2,8|sed "s/END=//" |awk '{print "dup\t" $0}' >>svs.tab
	grep "<UNK>" $i |grep -v "random" |sed "s/;/\t/" |cut -f 1,2,8|sed "s/END=//" |awk '{print "unk\t" $0}' >>svs.tab
	grep "<INV>" $i |grep -v "random" |sed "s/;/\t/" |cut -f 1,2,8|sed "s/END=//" |awk '{print "inv\t" $0}' >>svs.tab
	grep "<DEL>" $i  |grep -v "random" |sed "s/;/\t/" |cut -f 1,2,8|sed "s/END=//" |awk '{print "del\t" $0}'>>svs.tab
done


for j in `ls *_del.vcf`; do 
	echo $j
	grep SVTYPE2=DEL $j |grep -v random |grep SVTYPE2=DEL |grep -P "call_\d+_1\t" |sed "s/:/\t/" |cut -f 1,2,6|sed "s/\[//" |awk '{print "del\t" $0}' >>svs.tab
	grep "<DEL>" $j  |grep -v "random" |sed "s/;/\t/" |cut -f 1,2,8|sed "s/END=//"  |awk '{print "del\t" $0}'>>svs.tab
done

