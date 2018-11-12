import pandas as pd
import numpy as np

import mapplotlib.pyplot as plt
# 

# file = pd.read_csv("")
rng = pd.date_range("1/1/2000",periods=1000, freq="H")
rng[:5]
ts = pd.Series(np.random.randn(len(rng)),index=rng)

ts.head()

# Take hourly means
ts.resample("H").mean()

