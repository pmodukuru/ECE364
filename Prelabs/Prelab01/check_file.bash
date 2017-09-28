#! /bin/bash
$Author: ee364f07 $
$Revision: 99196 $
$Id: check_file.bash 99196 2017-01-16 00:23:11Z ee364f07 $

#input validation
if (( $# != 1 ))
then 
	echo "Usage: ./check_file.bash <filename>"
	exit
fi

#exist check
[[ -e $1 ]] && echo "$1 exists"
[[ ! -e $1 ]] && echo "$1 does not exist"

#directory check
[[ -d $1 ]] && echo "$1 is a directory"
[[ ! -d $1 ]] && echo "$1 is not a directory"

#ordinary file check
[[ -f $1 ]] && echo "$1 is an ordinary file"
[[ ! -f $1 ]] && echo "$1 is not an ordinary file"

#readable check
[[ -r $1 ]] && echo "$1 is readable"
[[ ! -r $1 ]] && echo "$1 is not readable"

#writable check
[[ -w $1 ]] && echo "$1 is writable"
[[ ! -w $1 ]] && echo "$1 is not writable"

#executable check
[[ -x $1 ]] && echo "$1 is executable"
[[ ! -x $1 ]] && echo "$1 is not executable"


exit

