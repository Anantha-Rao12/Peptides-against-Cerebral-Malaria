# Computing the Hydrogen Bond Profile

## Objective :
- Given a .pdb file, we use ```Hbond-analyzer.sh``` along with the ```hbond-script.cmd``` to obtain a ```{}_hbond_info.txt``` file. This contains information about the hydrogen bonds in the given .pdb file. We do this for multiple .pdb files
- The python script ```PDB_Hbond_analyser.py ``` reads through multiple ```{}_hbond_info.txt``` files and returns a .csv file with a structured dataframe format that can be used for further analysis. 


## ```Hbond-analyzer.sh```
The bash script hbond-analyzer is a wrapper-script containing functions built over Chimera and uses the --nogui flag to run it without the graphical user interface.

The Script takes two arguments : 
1. A text file containing .pdb files that are to be analysed (must be in the same directory as the script and .pdb files)
2. A .cmd file containing chimera commands

The commands to be run in chimera is submitted in a .cmd file, with each line containing the command based on chimera documentation. 

### Working

The script loops over each line of the text line (basically a file name), reads that particular file and processes it based on the instructions given in the .cmd file. After processing, the last 8 lines of the output (required information is stored here) is written to an external file. We then use the Linux stream editor ('sed') to replace the filename to be read next in the .cmd file and a similar process continues untill all files in the .txt file are processed.   


## ```PDB_Hbond_analyser.py ```

The script takes two arguments : 
1. A text file  containing the names of ```._hbond_info.txt files``` (outputs of ```Hbond-analyzer.sh```) that are to be analysed (must be in the same directory as the script and .txt files)
2. The name of the output .csv file where the output data is written 

### Working 
The python script contains a host of preprocessing functions that read data from the output files of ```Hbond-analyzer.sh``` ie files ending with ```hbond_info.txt```. The script processes each line in the .txt file using grep expressions and returns a dataframe containing information on the Hydrogen bonds (Donor atom, Acceptor atom, Donor-Hydrogen, Distance D-A, Distance D-H-A, No of Hydrogen bonds). This is used for further Data Analysis and Interpretation
