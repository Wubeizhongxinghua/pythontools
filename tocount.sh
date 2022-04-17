#! /bin/bash # employ bash shell
for i in `ls *.count`
do
	awk '{print ($1"\t"$7)}' ${i} > ${i}.countnum
done

for i in `ls *.countnum`
do
	sed '1,2'd ${i} > ${i}.process
done
