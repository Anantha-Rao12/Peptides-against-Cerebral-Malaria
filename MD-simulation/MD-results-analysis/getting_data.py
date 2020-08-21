import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from analysecentroid import euclidean_distance

path = '/home/asr/Documents/Chimera-files/Repeat3/2.swiss-model-5mza-full-files/mdrun/md1-hybrid/Centroid_analysis/Models/'

models = os.listdir(path)
listoflists = []
for model in models:
    centroid_datafile = os.path.join(path,model)
    data = [model,euclidean_distance(centroid_datafile)]
    listoflists.append(data)

df = pd.DataFrame(listoflists,columns=['model','distance'])
df_new = df.sort_values('model')

df_new.to_csv('./md1_centroid_data.csv')


fig = plt.figure(figsize=(8,7))
ax = fig.add_subplot('111)

x = np.arange(0,101,10)
y = df_new.distance.values

ax.plot(x,y)
ax.set_xlabel('Time (ns)',fontsize=18)
ax.set_ylabel('Distance (A)',fontsize=18)
ax.set_title('Distance between centroid of Protein and peptide',fontsize=22)
plt.show()
