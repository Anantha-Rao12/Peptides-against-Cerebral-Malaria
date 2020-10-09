import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def Interaction_energy_heatmap(csv_file_path):

	df = pd.read_csv(csv_file_path)   # read the csv file from the given path 
	df.drop('Unnamed: 0',axis=1, inplace=True)  # if there is a column called "Unnamed :0" then it is drop , is it is not there please comment it out
	df.Pdb = df.Pdb.apply(lambda x : x.split('/')[-1]) # based on the previous convention follow, we rename the elements in the column 'Pdb' and replace it with the name instead of the entire path
	df['mresidue'] = df.Pdb.apply(lambda x : x.split('_')[2]) # create a new column that contains the mutated residue no based on the name of the row in the 'Pdb' column
	df['amino_acid'] = df.Pdb.apply(lambda x : x.split('_')[3]) # create a new column that contains the mutated amino acid name based on the name of the row in the 'Pdb' column

	cols = df.columns.tolist()  # In the next three lines we are renaming the columns
	cols = cols[0:1] + cols[-2:] + cols[1:-2]
	df = df[cols]

	heatmap = df.groupby(['amino_acid','mresidue']).mean()['Interaction Energy'].unstack() # Create a new dataframe for creating a heatmap that uses the columns 'amino_acid' and 'mresidue' that we created earlier
	
	fig = plt.figure(figsize=(10,9))  # create a figure object and some plotting conventions
	ax = fig.add_subplot(1, 1, 1)
	sns.heatmap(heatmap,cmap='viridis',fmt='.2f',annot=True,axes=ax)
	ax.set_title('Interaction Energy for SwM_Full',fontsize=22)
	ax.set_xlabel('Mutated Residue No',fontsize=18)
	ax.set_ylabel('Amino Acid',fontsize=18)
	
	return fig

def get_hybrid_peptide(csvfile_path):   # reads through the scores.csv of the Saturated Mutagenesis file and gives data on hybrid peptide -- output is written to a .csv called "hybrid_peptide.csv"

	df = pd.read_csv(csvfile_path)
	df.drop('Unnamed: 0',axis=1, inplace=True)
	df.Pdb = df.Pdb.apply(lambda x : x.split('/')[-1])
	df['mresidue'] = df.Pdb.apply(lambda x : x.split('_')[2])
	df['amino_acid'] = df.Pdb.apply(lambda x : x.split('_')[3])

	cols = df.columns.tolist()
	cols = cols[0:1] + cols[-2:] + cols[1:-2]
	df = df[cols]

	best_mut = df.iloc[df.groupby('mresidue')['Interaction Energy'].idxmin()][['Pdb','mresidue','amino_acid','Interaction Energy']]
	best_mut.to_csv('hybrid_peptide.csv')
	
	return best_mut


path = '/home/asr/Documents/Chimera-files/Repeat3/2.swiss-model-5mza-full-files/scores.csv'	
df = get_hybrid_peptide(path)
fig = Interaction_energy_heatmap(path)
print(df)
os.chdir('/home/asr/Documents/Chimera-files/Repeat3/2.swiss-model-5mza-full-files/')
fig.savefig('heatmap_Sw_Fullchain.png')
df.to_csv('hybrid_peptide.csv')
#print(df.to_csv('trialhybrid.csv'))

