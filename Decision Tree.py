from sklearn.tree import DecisionTreeClassifier

X = [[1], [2], [3], [4], [5]]
y = ["Low", "Low", "Medium", "High", "High"]

model = DecisionTreeClassifier()
model.fit(X, y)

print("Category of value 4 =", model.predict([[4]]))
