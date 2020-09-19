#!/bin/bash

# author : Anantha S Rao
# date : 19 September, 2020


# get_hbond_data obtains hbond data using chimera nogui option ; arguments all analysis are supplied by the argument ($1) 

function get_hbond_data(){
    ~/chimera/bin/chimera --nogui $1
}

# process_data reads a textfile containing .pdb filenames (line by line), as it reads a line, it manipulates hbond-script.cmd that serves as input to chimera. 
# Each line is a filename and each iteration, wries hbond data from chimera to a _hbond_info.txt file

function process_data(){
    fname=$1
    n=1
    while read line; do
        # reading each line
        echo "Processing $line"
        sed -i "s|filename|$line|" $2
        get_hbond_data $2 | tail -9 > ${line}_hbond_info.txt
        sed -i "s|$line|filename|" $2
        n=$((n+1))
    done < $fname
}

process_data pdbnames.txt hbond-script.cmd
exit
