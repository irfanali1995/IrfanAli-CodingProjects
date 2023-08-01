#!/bin/bash

# this default behavior of the script is to convert to lowercase

declare -a flag_array # to store the flags that have been selected

# The below usage function is essentially the help pf the section
# this will be called whenever an incorrecrt selection has been made or when the -h flag is passed
usage() {                                      # Function: Print a help message.
  echo "Usage: chngnm [ -u uppercase ] [ -l lowercase ].. <dir/file names....>" 
  echo "Some of the flags that can be used are "
  echo '-h --help'
  echo '-u --uppercase'
  echo '-l --lowercase'
  echo '-r --recursive'
  echo '-s --subdirectories'
 
}



flag_counter=0
action=0
# The loop checks if the file was passed without any arguments

while true; do

if [ "$#" -eq 0 ];
  then
   echo 'You did not select any options'
   usage
  exit 1
else
   break
fi

done

# The getopts function is used to select all of the flags that have been passed. 
# it raises an error when any flag other than r,s,l,u,h are passed

while getopts "rsluh" options; do

    case "${options}" in

        r) flag_counter=$((flag_counter+1))
           flag_array+=('r')
           ;;

        s) flag_counter=$((flag_counter+1))
           flag_array+=('s')
           ;;

        l)
           flag_counter=$((flag_counter+1))
           flag_array+=('l')
           action=$((action+1))
           if [ "$action" -eq  2 ];
           then
            echo 'Command syntax incorrect'
            exit 1
           fi
           ;;

        u)
           flag_counter=$((flag_counter+1))
           action=$((action+1))
           flag_array+=('u')
           if [ "$action" -eq 2 ];
           then
            echo 'Command syntax incorrect'
            exit 1
           fi
           ;;

        h)
           flag_counter=$((flag_counter+1))
           action=$((action+1))
           echo 'Help flag has been selected'
           usage
           exit 1
           ;;

        *)
           echo 'Invalid flag option selected'
           exit 1 
           ;;

    esac
 
done

uniq_array=($(printf "%s\n" "${flag_array[@]}" | sort -u | tr '\n' ' '))
shift $flag_counter
#the shift option is used to discard the flags and ensure that $# contain only file names
# below loop checks to see whether the correct option was specified or not
for i in "${uniq_array[@]}";
do

  if [ "$i" = "l" ]
   then
    action=0
    break
  else
    action=1
    break
  fi
done

#the below converts the names to lower or uppercase

for i in "${uniq_array[@]}"; do echo "$i"; done

echo "the value of action is = $action"

while (( "$#" ));do

 if [ -f "$1" ] 
  then
   if [ "$action" -eq 0 ]
    then
     name=$1
     echo "A file with the name, $1 exists on the system."
     up_name="${name,,}"
     mv "$name" "./$up_name"
     echo 'File name has been changed to lowercase'
   else
     name=$1
     echo "A file with the name, $1 exists on the system."
     up_name="${name^^}"
     mv "$name" "./$up_name"
     echo 'File name has been changed to Uppercase' 
   fi


 elif [ -d "$1" ]
  then
     part1=`dirname "$1"`
     part2=`basename "$1"`
     if [ "$action" -eq 0 ]
      then
       up_name="${part2,,}"
       mv "$1" "${part1}/${up_name}"
       echo 'Directory name has been changed to lowercase'
     else
       up_name="${part2^^}"
       mv "$1" "${part1}/${up_name}"
       echo 'Directory name has been changed to uppercase'
     fi

 else
     echo "Error: No file or directory with the name $1  exists."

 fi
 shift

done
