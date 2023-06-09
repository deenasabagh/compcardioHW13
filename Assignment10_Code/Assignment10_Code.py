import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

edges = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]]) 
nodes = np.unique(edges)
position = np.array([[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1]])
pos_d = pos_d = dict(enumerate(position, 1))
Q = nx.Graph()
Q.add_nodes_from(nodes)
Q.add_edges_from(edges.T)
                          
lap = nx.laplacian_matrix(Q).toarray()
dt = .01

f = nodes*0
f[0] = 1
run_to = 100
ten_plots = round(run_to/10)
j = 0

for i in range(run_to+1):
    
    if i in [0, 50, 100]:
        plt.close('all')
        plt.figure(10)
        nx.draw_networkx(Q, node_color=f, pos=pos_d, with_labels=False, vmin=0,vmax=.25)
        plt.title('time = '+str(i))
        plt.savefig('outputs/'+'time'+str(j)+'.png')
        
        j += 1

    f = f - dt*np.matmul(lap,f)
    
# Extract temperature values at tstep = 0, 50, and 100
tstep0_temp = f[0 :]
tstep50_temp = f[50 :]
tstep100_temp = f[100 :]

# Calculate mean and standard deviation using NumPy functions
tstep0_mean = np.mean(tstep0_temp)
tstep50_mean = np.mean(tstep50_temp)
tstep100_mean = np.mean(tstep100_temp)

tstep0_std = np.std(tstep0_temp)
tstep50_std = np.std(tstep50_temp)
tstep100_std = np.std(tstep100_temp)

print("Mean temperature at tstep = 0: {:.2f}".format(tstep0_mean))
print("Standard deviation of temperature at tstep = 0: {:.2f}".format(tstep0_std))

print("Mean temperature at tstep = 50: {:.2f}".format(tstep50_mean))
print("Standard deviation of temperature at tstep = 50: {:.2f}".format(tstep50_std))

print("Mean temperature at tstep = 100: {:.2f}".format(tstep100_mean))
print("Standard deviation of temperature at tstep = 100: {:.2f}".format(tstep100_std))
 
