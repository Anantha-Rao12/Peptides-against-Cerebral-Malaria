# Computing the Hydrogen Bond Profile

The bash script hbond-analyzer is a wrapper-script containing functions built over Chimera and uses the --nogui flag to run it without the graphical user interface.

The Script takes two arguments : 
1. A text file containing .pdb files that are to be analysed (must be in the same directory as the script and .pdb files)
2. A .cmd file containing chimera commands

The commands to be run in chimera is submitted in a .cmd file, with each line containing the command based on chimera documentation. 

## Working

The script loops over each line of the text line (basically a file name), reads that particular file and processes it based on the instructions given in the .cmd file. After processing, the last 8 lines of the output (required information is stored here) is written to an external file. We then use the Linux stream editor ('sed') to replace the filename to be read next in the .cmd file and a similar process continues untill all files in the .txt file are processed.   
