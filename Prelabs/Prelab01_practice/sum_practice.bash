#! /usr/bin/bash
sum=0
while (( $# != 0))
do
	let sum=sum+$1
	shift
done

echo $sum

exit