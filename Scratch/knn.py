from sklearn.datasets.samples_generator import make_blobs
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(6)
import math
from collections import Counter

(X,y) =  make_blobs(n_samples=50,n_features=2,centers=2,cluster_std=1.95,random_state=50)
# plt.scatter(X[:,0],X[:,1],marker='o',c=y)
# plt.show()

prediction_points = [[-2,-4], [-3, -6], [1, 0], [6,4], [-6,4]]
prediction_points = np.array(prediction_points)
# plt.scatter(X[:,0],X[:,1],marker='o',c=y)
# plt.scatter(prediction_points[:,0],prediction_points[:,1],marker='o')
# plt.show()

def get_distance_ID(point, k):
	distance = np.sqrt(np.sum((X - point)**2 , axis=1))
	return np.argsort(distance)[:k]

def predict(prediction_points, k):
	labels = []
	for point in prediction_points:
		distance_ID = get_distance_ID(point, k)
		results = []
		for index in distance_ID:
			results.append(y[index])

		label = Counter(results).most_common(1)
		# print(results, Counter(results), distance_ID)
		labels.append([point, label[0][0]])
	print (labels)
	return labels

results=predict(prediction_points,10)
for result in results:
    print("Point = ",result[0])
    print("Class = ",result[1])
    print()


 

