#! /usr/bin/bash

while (( $# != 0))
do
	#conditional check
	if [[ -r $1 ]]
	then
		echo "File $1 is readable"
	else
		touch $1
	fi
	shift
done

exit
