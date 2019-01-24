import numpy as np
import pandas as pd
from copy import deepcopy

def dist (data, center, ax = 1):
	return np.linalg.norm(data - center, axis = ax)



def kmean(X, k =2):
	C_x = np.random.randint(0, np.max(X), size=k)
	C_y = np.random.randint(0, np.max(X), size=k)


	C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
	clusters = np.zeros(len(X))
	error = 1

	while error != 0:
		for i in range(len(X)):
			distances = dist(X[i], C)
			cluster = np.argmin(distances)
			clusters[i] = cluster
		C_pre = deepcopy(C)
		for i in range(k):
			cluster_points = [X[j] for j in range(len(X)) if clusters[j] == i]
			C[i] = np.mean(cluster_points, axis=0)
		error = dist(C_pre, C, None)
	print (clusters)





X = np.array([[1, 2],
              [1.5, 1.8],
              [5, 8 ],
              [8, 8],
              [1, 0.6],
              [9,11]])

kmean(X)
