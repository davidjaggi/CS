import pandas as pd
import numpy as np

import random

import matplotlib.pyplot as plt
# set seed so we have everytime the same output
random.seed(7)

# file = pd.read_csv("")
rng = pd.date_range("1/1/2000",periods=1000, freq="H")
rng[:5]
ts = pd.Series(np.random.randn(len(rng)),index=rng)

# Show the head of the file
ts.head()

# Plot the time series
plt.plot(ts)
plt.show()

# Take hourly means
ts.resample("H").mean()

# check stationarity of data
from statsmodels.tsa.stattools import adfuller

def test_stationarity(timeseries):
    # https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/
    # Determine rolling statistics
    rolmean = timeseries.rolling(window=12).mean()
    rolstd = timeseries.rolling(window=12).std

    # Plot rolling statistics
    orig = plt.plot(timeseries, color="blue", label="Original")
    mean = plt.plot(rolmean, color="red",label="Rolling Mean")
    std = plt.plot(timeseries, color="black",label="Rolling Std")
    plt.legend(loc="best")
    plt.title("Rolling Mean & Standard Deviation")
    plt.show(block=False)

    # Perform Dickey Fuller test 
    print("Results of Dickey-Fuller Test:")
    dftest=adfuller(timeseries,autolag="AIC")
    dfoutput=pd.Series(dftest[0:4], index=["Test Statistic","p-Value","# Lags Used","Number of Observations Used"])
    for key, value in dftest[4].items():
        dfoutput[f"Critical Value ({key})"] = value
        print(dfoutput)

test_stationarity(ts)

# Take the log of the series to make it stationary
ts_log = np.log(ts)
plt.plot(ts_log)
plt.show()

# Create a moving average to smooth the series
mavg12=ts.rolling(12).mean()
plt.plot(ts)
plt.plot(mavg12)
plt.show()