import quandl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
import math, datetime

style.use("ggplot")

api_key = "zfh6d5zuyqneiqi7YGyZ"
quandl.ApiConfig.api_key = api_key
df = quandl.get("BITFINEX/BTCUSD")
df.dropna(inplace=True)

df["HL_PCT"] = (df["High"] - df["Low"]) / df["Last"] * 100.0
df["ASKBID_PCT"] = (df["Ask"] - df["Bid"] / df["Ask"]) * 100.0

df = df[["High", "Low", "Last", "HL_PCT", "ASKBID_PCT", "Volume"]]

forecast_out = int(math.ceil(len(df) * 0.09))

df["Label"] = df["Last"].shift(-forecast_out)

X = df.drop(columns="Label")
X = scale(X)
Y = df.iloc[:, -1]
X_toPredict = X[-forecast_out:]
X = X[:-forecast_out]
Y = Y[:-forecast_out]
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, train_size=0.7, random_state=0)

regressor = LinearRegression()
regressor.fit(X_Train, Y_Train)
Accuracy = regressor.score(X_Test, Y_Test)
print(Accuracy)

prediction_set = regressor.predict(X_toPredict)
df["Prediction"] = np.nan

last_date = df.iloc[-1].name
lastDateTime = last_date.timestamp()
one_day = 86400
nextDateTime = lastDateTime + one_day

for i in prediction_set:
    next_day = datetime.datetime.fromtimestamp(nextDateTime)
    nextDateTime += one_day
    df.loc[next_day] = [np.nan for q in range(len(df.columns) - 1)] + [i]

df["Last"].plot(color="b")
df["Prediction"].plot(color="r")
plt.xlabel("Date")
plt.ylabel("Price[USD]")
plt.legend(loc=4)
plt.show()


def factoriel(n):
    if n==1:
        return 1
    else:
        return n*factoriel(n-1)


    print(factoriel(2))





