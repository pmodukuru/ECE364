#! /bin/bash
$Author: ee364f07 $
$Revision: 99196 $
$Id: exist.bash 99196 2017-01-16 00:23:11Z ee364f07 $

while (( $# != 0 ))
do
	if [[ -r $1 ]]
	then 
		echo "File $1 is readable!"
	else
		touch $1
	fi
shift
done

exit
	
