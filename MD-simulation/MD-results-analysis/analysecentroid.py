import numpy as np

def euclidean_distance(centroid_datafile):

    def find_centroid(centroid_datafile):

        with open(centroid_datafile,'r') as rf:
            data = rf.readlines()

        cA = data[-3].split()
        cB = data[-2].split()
        
        cAx, cAy, cAz = float(cA[-3][:-1]), float(cA[-2][:-1]), float(cA[-1][:-1])
        cBx, cBy, cBz = float(cB[-3][:-1]), float(cB[-2][:-1]), float(cB[-1][:-1])

        centroid_data = {'A':{'cAx':cAx, 'cAy':cAy, 'cAz':cAz},'B':{'cBx':cBx, 'cBy':cBy, 'cBz':cBz}}

        return centroid_data
    
    centroid_data = find_centroid(centroid_datafile)

    A_posn =  np.array(list(centroid_data['A'].values()))
    B_posn = np.array(list(centroid_data['B'].values()))
    abs_diff = abs(A_posn - B_posn)
    distance =np.sqrt(np.sum(abs_diff**2))

    return distance

