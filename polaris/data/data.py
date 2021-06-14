import pandas as pd
import numpy as np

def get_inputs():
  N = 100
  age = np.random.randint(1, 30, size=N)
  region = np.random.randint(1, 300, size=N)
  price = 0.5*age + 0.3*region + np.random.normal(scale=3, size=N)
  return pd.DataFrame({
    "age": age,
    "region": region,
    "known_price": price
  })