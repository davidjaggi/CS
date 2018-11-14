import random
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# set seed for random generation
random.seed(7)

def random_generator(N=1000):
    rng = pd.date_range("1/1/2000",periods=N, freq="H")
    return pd.Series(np.cumsum(np.random.uniform(-0.5,0.5,(N))), index=rng)

'''
x = random_generator(1000)
plt.plot(x)
plt.show()
'''