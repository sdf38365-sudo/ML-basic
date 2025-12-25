from sklearn.linear_model import LinearRegression

X = [[1000], [1500], [2000], [2500]]  # Area (input)
y = [200000, 300000, 400000, 500000]  # Price (output)

model = LinearRegression()
model.fit(X, y)

print("Prediction for 1800 sqft =", model.predict([[1800]]))
