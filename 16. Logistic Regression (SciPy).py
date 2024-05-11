import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load the data
df = pd.read_csv('https://bit.ly/33ebs2R', delimiter=",")
X = df.values[:, :-1]
Y = df.values[:, -1]

model = LogisticRegression(penalty=None)

model.fit(X, Y)
# print beta1
print(model.coef_.flatten())
# print beta0
print(model.intercept_.flatten())
