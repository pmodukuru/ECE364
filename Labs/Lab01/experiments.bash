#! /bin/bash

#---------------------------------------
# $Author: ee364f07 $
# $Date: 2017-01-18 14:02:31 -0500 (Wed, 18 Jan 2017) $
#---------------------------------------

# Do not modify above this line.

if (( $# < 1 )) 
then
	echo "Usage: experiments.bash <input 1> [input 2] .. [input N]"
	exit 1
fi


while (( $# != 0))
do
	echo "$1:"
	#check if files are readable
	if [[ ! -r $1 ]]
	then
		echo "Filename \"$1\" is not readable."
		echo ""
		shift
		continue
	fi

	#print output
	while read ID data1 data2 data3
	do
		ID=$(echo "$ID" | cut -f1)
		let SUM=$data1+$data2+$data3
		let AVG=($data1+$data2+$data3)/3
		echo "$ID $SUM $AVG"
	done < $1

	echo ""
	shift
done



exit 0

