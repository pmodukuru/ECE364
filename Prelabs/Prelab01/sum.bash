#! /bin/bash
$Author: ee364f07 $
$Revision: 99196 $
$Id: sum.bash 99196 2017-01-16 00:23:11Z ee364f07 $


SUM=0
while (( $# != 0 ))
do
	((SUM=SUM+$1))
	shift
done

echo $SUM

exit
