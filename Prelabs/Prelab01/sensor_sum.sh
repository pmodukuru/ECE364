#! /bin/bash
$Author: ee364f07 $
$Revision: 99196 $
$Id: sensor_sum.sh 99196 2017-01-16 00:23:11Z ee364f07 $

#input validation
if (( $# != 1 )) 
then
	echo "usage: sensor_sum.sh log"
	exit
fi

#check if log is readable
if [[ ! -r $1 ]]
then
	echo "error: $1 is not a readable file!"
	exit
fi

#read file line by line
while read ID data1 data2 data3
do
	ID=$(echo "$ID" | cut -c1,2)
	let SUM=$data1+$data2+$data3
	echo "$ID $SUM"
done < $1


exit
