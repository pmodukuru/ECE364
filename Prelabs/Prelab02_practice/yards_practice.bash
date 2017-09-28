#! /usr/bin/bash

#Input validation
if (( $# != 1 ))
then 
	echo "Usage: yards.bash <filename>"
	exit
fi

#check if file is readable
[[ ! -r $1 ]] && echo Error: $1 not readable && exit


maxavg=0
#read file line by line
while read -a line
do
	sum=0
	avg=0
	var=0
	let numteams=${#line[*]}-1
	
	#get name of conf
	conf=${line[0]}
	
	#get sum
	for yards in ${line[*]:1}
	do
		let sum+=yards
	done

	#get avg
	let avg=sum/numteams
	(( avg > maxavg )) && let maxavg=avg

	#get var
	for yards in ${line[*]:1}
	do
		let var+=(yards-avg)**2
	done
	let var=var/numteams
	
	echo "$conf schools averaged $avg yards recieving with a variance of $var"
	
done < $1

echo "The largest average yardage was $maxavg"

exit


