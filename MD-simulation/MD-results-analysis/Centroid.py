import re
import numpy as np
import sys

def get_centroid(pdb_file, chain_name):
	
    regexp = r'(ATOM\s+)(\d+)(\s+\S+\s*\w{3,4}\s)('+str(chain_name)+')(\s+\S+\s+)(-|\d)(\d{0,3}.\d{1,3})(\s+)(-|\d)(\d{0,3}.\d{1,3})(\s+)(-|\d)(\d{0,3}.\d{1,3})(\s+\S+\s+\S+\s+)([A-Z])'
            
    pattern = re.compile(regexp)

    atomic_wt_dict = { 'H' : 1, 'C' : 12, 'N'  : 14, 'O' : 16 , 'S' : 32}
            
    with open(pdb_file,'r') as rf:
        contents = rf.read()
        matches = pattern.finditer(contents)
            
    '''	
    Atom no -->  match.group(2)
    Chain name --> match.group(4)
    X co-ordinates --> match.group(6)+match.group(7)
    Y co-ordinates --> match.group(9)+match.group(10)
    Z co-ordinates --> match.group(12)+match.group(13)
    Atom -->  match.group(15)
    Atomic weight --> atomic_wt[match.group(15)]
    '''
            
    posn_array = np.zeros((3,1))
    wt = np.zeros((1,1))

    for match in matches:
        x_cord = float(match.group(6)+match.group(7))
        y_cord = float(match.group(9)+match.group(10))
        z_cord = float(match.group(12)+match.group(13))
        atomic_wt = atomic_wt_dict[match.group(15)]
        
        posn_array= np.hstack((posn_array,np.array([[x_cord],[y_cord],[z_cord]])))
        wt = np.hstack((wt,np.array([[atomic_wt]])))

    weighted_posn = posn_array * wt
    wt_sum = np.sum(wt,axis=1,keepdims=True)

    centroid = np.sum((weighted_posn/wt_sum),axis=1,keepdims=True)
    
    return centroid

if  __name__ == '__main__':
       centroid = get_centroid(sys.argv[1],sys.argv[2])
       print(f'The centroid co-ordinates of Chain{sys.argv[2]} of {sys.argv[1]} is : \n {centroid}')

