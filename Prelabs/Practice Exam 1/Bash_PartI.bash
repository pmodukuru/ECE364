#! /bin/bash

#----------------------------------
# $Author$
# $Date$
#----------------------------------

function part_a 
{               
    # Fill out your answer here
	numfiles=$(ls myDir/*.pdf | wc -w)
	echo $numfiles
	return                      
}                               

function part_b
{              
    # Fill out your answer here
	head -n 9 data.txt | tail -n 1
	return                     
}                              

function part_c
{
    # Fill out your answer here
		

	return
}

function part_d
{
    # Fill out your answer here
	string=$(diff foo1.txt foo3.txt)
	[[ -z $string ]] && echo "Files are similar"
	[[ -n $string ]] && echo "Files are not similar"

	return
}

function part_e
{
    # Fill out your answer here
    return
}

# To test your function, you can call it below like this:
#
# part_a
part_d
