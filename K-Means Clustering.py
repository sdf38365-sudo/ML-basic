from sklearn.cluster import KMeans

X = [[1,1], [2,2], [3,3], [10,10], [11,11], [12,12]]

model = KMeans(n_clusters=2)
model.fit(X)

print("Cluster labels =", model.labels_)
