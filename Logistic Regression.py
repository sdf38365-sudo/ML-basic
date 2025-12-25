from sklearn.linear_model import LogisticRegression

X = [[2], [4], [6], [8]]   # Study hours
y = [0, 0, 1, 1]           # 0 = Fail, 1 = Pass

model = LogisticRegression()
model.fit(X, y)

print("Pass probability for 5 hours =", model.predict([[5]]))
