from Centroid import get_centroid, euclidean_distance
import pandas as pd
import sys

def write_centroid_dataframe(pdb_files_textfile, output_file):
    
    with open(pdb_files_textfile,'r') as rf:
        pdb_files = rf.read().split('\n')
        pdb_files = [item for item in pdb_files if item.endswith('.pdb')] 

    listoflists = []
    for f in pdb_files:
        cA = get_centroid(f,'A')
        cB = get_centroid(f,'B')
        distance = euclidean_distance(cA,cB)
        data = [f,cA,cB,distance]
        listoflists.append(data)

        print(f'The distance between the two centroids in {f} is {distance:.5}A ')


        df = pd.DataFrame(listoflists,columns =['Filename','CentroidA','CentroidB','Distance'])
        df.to_csv('./'+str(output_file)+'.csv',index=False)


if __name__ == '__main__':
    
    if len(sys.argv) !=  3 :
        print('Incorrect number of arguments. Expecting only 2 !')
        sys.exit(1)
    else:
        print(' Running \n')
        write_centroid_dataframe(sys.argv[1],sys.argv[2])
        sys.stdout.write(f'\nProcess Successful! Output saved to {sys.argv[2]}.csv\n ')
        
        
