import os
import subprocess
import time
import pandas as pd
#from chimera import runCommand as rc  


def saturated_mutagenesis(model_no,chain_name,start_residue,stop_residue,input_path,file_name,output_path):

	aa_data = 'ala arg asn asp cys glu gln gly his ile leu lys met phe pro ser thr trp tyr val'.split()
	
	for residue_no in range(start_residue,stop_residue+1):
		for amino_acid in aa_data:
			rc("open "+ os.path.join(input_path,file_name))
			rc("swapaa "+str(amino_acid)+" #"+str(model_no)+":"+str(residue_no)+"."+chain_name)
			os.chdir(output_path)
			rc("write #"+str(model_no)+" Inh_1_"+str(residue_no)+"_"+str(amino_acid)+".pdb")
			rc("close all")
			os.chdir(input_path)
			


def AnalyseComplex(foldx_path, file_full_path, output_full_path):
	
	data=[]
	start = time.time()
	process = subprocess.Popen(f'{foldx_path} --command=AnalyseComplex --pdb={file_full_path} --analyseComplexChains=A,B', shell=True, stdout=subprocess.PIPE)
	result = process.communicate()[0] 
	data.append(result)
	end=time.time()
	time_taken = end-start
	print(time_taken)
	return data
	

def make_df_combine(files_path1,files_path2,output_path):
	
	listoflists =[]
	paths= [files_path1,files_path2]
	for path in paths:
		for file in os.listdir(path):
			with open(os.path.join(path,file),'r') as rf:
				lines = rf.read().splitlines()
				data = lines[-1].split('\t')
				header = lines[-2].split('\t')
				listoflists.append(data)
	df = pd.DataFrame(listoflists,columns=header)
	os.chdir(output_path)
	df.to_csv(os.path.join(output_path,'scoring-repeat-1.csv'))


	
