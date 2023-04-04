#calculation for the correlation of eruption and waiting time.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/faithful.csv')

x = np.asarray(df['eruptions'])
y = np.asarray(df['waiting'])

mean_x = np.mean(x)
mean_y = np.mean(y)

x_centered = x - mean_x
y_centered = y - mean_y

#Correlation formula
#Corr(x,y) = <x,y>/|X||Y|
corr = np.dot(x_centered, y_centered) / (np.linalg.norm(x_centered) * np.linalg.norm(y_centered))

print(f"Correlation: {corr}")
