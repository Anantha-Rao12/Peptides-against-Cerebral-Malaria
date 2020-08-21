import numpy as np

def find_centroid(centroidinfo_file_path):

    with open(centroidinfo_file_path,'r') as rf:
        data = rf.read().split('\n')

    cA = data[8].split()
    cB = data[9].split()

    cAx, cAy, cAz = float(cA[3][:-1]), float(cA[4][:-1]), float(cA[5][:-1])
    cBx, cBy, cBz = float(cB[3][:-1]), float(cB[4][:-1]), float(cB[5][:-1])

    hybrid_centroid = {'A':{'cAx':cAx, 'cAy':cAy, 'cAz':cAz},'B':{'cBx':cBx, 'cBy':cBy, 'cBz':cBz}}

    return hybrid_centroid

def euclidean_distance(centroid_data):

    A_posn =  np.array(list(centroid_data['A'].values()))
    B_posn = np.array(list(centroid_data['B'].values()))
    abs_diff = abs(A_posn - B_posn)
    distance =np.sqrt(np.sum(abs_diff**2))

    return distance
        
path = '/home/asr/Documents/Chimera-files/Repeat3/2.swiss-model-5mza-full-files/mdrun/md1-hybrid/Centroid_analysis/centroidinfo'

centroid_data= find_centroid(path)
distance = euclidean_distance(centroid_data)

print(distance)


