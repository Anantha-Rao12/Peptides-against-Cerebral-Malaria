# Analysis of Molecular Dynamics simulations

To analyse the MD simulaions of a Protein and its peptide inhibitor, we wanted to understand two particular aspects in greater detail: 
## How does the distance between the centroids of the Protein and peptide evolve over time ? 
  1. If it increasing, it means that over-time the peptide flies away from the protein and is not binding effectively.
  2. If the distance between the centroid of the two entities remains constant, then over the duration of the simulation, the peptide binds strongly to the protein and can act as a good inhibitor. 
  3. If the distance decreases, then the peptide moves closer to the Protein core. (However, this is assumed to be unlikely) 
  
To perform these calculations, I wrote the script PDB_centroid_analyser. 
 
### What does PDB_centroid_analyser do ?

[PDB_centroid_analyser](https://github.com/Anantha-Rao12/Peptides-against-Cerebral-Malaria/blob/master/MD-simulation/MD-results-analysis/PDB_centroid_analyser) basically reads through a .pdb file and captures all lines containing "ATOM .... \<element name\>". This is performed using Python regular expressions. The railroad diagram of the regex code is as follows: 
  
![Regex Diagram](https://github.com/Anantha-Rao12/Peptides-against-Cerebral-Malaria/blob/master/MD-simulation/MD-results-analysis/regex.svg)


Here : 
 - Atom no -->  match.group(2)
 - Chain name --> match.group(4)
 - X co-ordinates --> match.group(6)+match.group(7)
 - Y co-ordinates --> match.group(9)+match.group(10)
 - Z co-ordinates --> match.group(12)+match.group(13)
 - Atom -->  match.group(15)

After reading these lines, the function get_centroid() obtains the centroid (x,y,z) of a given chain. We perform calculations in numpy arrays using the standard centroid formula: 

   **Centroid = sum( w[i] * r[i] ) / sum(w[i])** 
  
A wrapper function, **main()** calls other multiple functions to determine the distance between the centroid of two chains using euclidean_distance(). This is done for all the .pdb files submitted in the text file. *Special care* has to be taken to ensure that all .pdb files are in the official presribed format, otherwise the regex syntax will not be able to identify the chain, atom or element. Finally the script writes a .csv file in the same directory which includes the following fields:

1. File name 
2. Centroid of Chain1 "{chain-name given}"
3. Centroid of Chain2 "{chain-name is user-input}"
4. Distance between the centroids

--> This .csv file serves as a good checkpoint for performing further analysis. 

The script can be run on the command line/terminal and also imported into other scripts if particular functions seem interesting. The command line version takes two arguments:
1. A text file containing all .pdb names 
2. The output .csv filename.

The other functions included in PDB_centroid_analyser are : 
1. get_centorid() --> returns the centroid of a particular chain from a .pdb file
2. euclidean_distance() --> returns the distance between two vectors
3. pdb_names2list() --> returns a list from a text file containing names (one name in each line)
4. pdb_list_centroid2df() --> returns a .csv file containing centroid and distance information

## Hydrogen Bond Analysis

To understand effective binding, we analyse the number of intermolecular Hydrogen bonds between the Protein and the peptide. This entails the analysis of hbonds over each snapshot of the MD simulation to determine which residues and specifically which atom in these residues of the peptide inhibitor form hydrogen bonds with the protein. We also aim to determine the relative abundance of Hydrogen bonds formed over the entire simulation period. 

To perform these calculations, I wrote a script that functions on top of [Chimera](https://www.cgl.ucsf.edu/chimera/).  


