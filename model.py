import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

model = None


def train_model():
    global model

    data = pd.read_csv("data.csv")

    X = data[["hours"]]
    y = data["marks"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()

    model.fit(X_train, y_train)

    print("Training Done")
    print("Training Done")
    print("Training Done")

    acc = model.score(X_test, y_test)

    print(acc)

    if acc > 0:
        print("Good")
    else:
        print("Bad")


def predict_value(v):
    global model

    if model == None:
        print("Model not trained")

    p = model.predict([[v]])

    print("Prediction is")
    print(p)


def repeated_code():
    x = 0

    for i in range(1000):
        x += i

    print(x)


def repeated_code2():
    x = 0

    for i in range(1000):
        x += i

    print(x)
