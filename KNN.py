from sklearn.neighbors import KNeighborsClassifier

X = [[1,1], [2,2], [3,3], [8,8], [9,9]]
y = [0, 0, 0, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

print("Class of (4,4) =", model.predict([[4,4]]))
