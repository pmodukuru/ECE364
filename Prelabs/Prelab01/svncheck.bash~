#! /bin/bash
$Author: ee364f07 $
$Revision: 99166 $
$Id: svncheck.bash 99166 2017-01-16 00:06:30Z ee364f07 $

#check if file_list is readable
if [[ ! -r ./file_list ]]
then
	echo "error: $1 is not a readable file!"
	exit
fi

#opens new file descriptor
exec 10<"file_list"

#read file line by line
while read file_name <&10
do
	#checks svn status of all files in log
	statvar=$(svn status $file_name | cut -c1)
	if [[ $statvar = "?" ]]
	then 
		echo "$file_name - file has not been added to svn"
		read -p "Add file to repository? [y/n] " svnchoice
		
		#checks if file is executable
		if [[ ! -x $file_name ]] && [[ $svnchoice = "y" ]]
		then
			read -p "$file_name is not executable. Make executable? [y/n] " exechoice

			#makes file exe
			if [[ $exechoice = "y" ]]
			then
				chmod +x $file_name
			fi
		fi
	#adds file to svn
	[[ $svnchoice = 'y' ]] && svn add $file_name

	else
		#error if file does not exist on svn or dir
		[[ ! -e $file_name ]] && echo "Error: File $file_name appears to not exist here or in svn"
		#makes files already added exe
		[[ ! -x $file_name ]] && [[ -e $file_name ]] && $(svn propset svn:executable ON $file_name)
	fi
	
done

echo "Auto-committing code"
svn commit -m "Auto commit"
svn update

exit

