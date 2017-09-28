#! /usr/bin/bash

#input validation
(( $# != 1 )) && echo "Usage: ./check_file.bash <filename>" && exit

#check if exists
[[ -e $1 ]] && echo $1 exists
[[ ! -e $1 ]] && echo $1 does not exist

exit

