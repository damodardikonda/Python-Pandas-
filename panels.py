#Data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame
import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
p = pd.Panel(data).to_frame()
print(p)
