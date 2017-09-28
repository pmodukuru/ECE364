#! /bin/bash

#----------------------------------
# $Author$
# $Date$
#----------------------------------

# Do not modify above this line.

if (( $# != 1 ))
then
	echo "Usage: scheduler.bash <filename>"
	exit 1
fi

#readable
[[ ! -r $1 ]] && echo "File is not readable" && exit 2

first="  	07:00 08:00 09:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00"
echo $first > schedule.out

tottimes=(07:00 08:00 09:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00)

while read -a line
do
	name=${line[0]}
	time=$(echo ${line[1]} | cut -d"," -f)
	echo $time
	
done < $1

exit 0
