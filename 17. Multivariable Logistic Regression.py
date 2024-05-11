import pandas as pd
from sklearn.linear_model import LogisticRegression

employee_data = pd.read_csv("https://tinyurl.com/y6r7qjrp")

# grab independent variable columns
inputs = employee_data.iloc[:, :-1]
# grab dependent "did_quit" variable column
output = employee_data.iloc[:, -1]

fit = LogisticRegression(penalty=None).fit(inputs, output)

print(f"COEFFICIENTS: {fit.coef_.flatten()}")
print(f"INTERCEPT: {fit.intercept_.flatten()}")


# Note that the predict_proba() function will output two values, the first being the probability of 0 (false) and the second being 1 (true).
# Interact and test with new employee data
def predict_employee_will_stay(sex, age, promotions, years_employed):
    prediction = fit.predict([[sex, age, promotions, years_employed]])
    probabilities = fit.predict_proba([[sex, age, promotions, years_employed]])
    if prediction == [[1]]:
        return f"WILL LEAVE: {probabilities}"
    else:
        return f"WILL STAY: {probabilities}"


# Test a prediction
while True:
    n = input("Predict employee will stay or leave {sex},{age},{promotions},{years employed}: ")
    (sex, age, promotions, years_employed) = n.split(",")
    print(predict_employee_will_stay(int(sex), int(age), int(promotions), int(years_employed)))
