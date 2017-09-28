#! /usr/bin/bash

#input validation
if (( $# < 1 ))
then
	echo "Usage: line_num.bash <filename>"
	exit
fi

#check if readable
[[ ! -r $1 ]] && echo "Cannot read $1" && exit

cnt=1
#read file line by line
while read file_line
do
	echo "$cnt: $file_line"
	let cnt=cnt+1
done < $1

exit
	
	


