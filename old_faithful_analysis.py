import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/faithful.csv')

#using numpy.asarray() to convert csv columns to arrays
x = np.asarray(df['eruptions'])
y = np.asarray(df['waiting'])

#Scatter plot
plt.scatter(x, y)
plt.xlabel('Eruption Duration (minutes)')
plt.ylabel('Time Until Next Eruption (minutes)')
plt.title('Old Faithful Geyser: Duration of Eruptions vs Length of Time until Next Eruption')
plt.show()

#Mean times of eruptions and waiting column
mean_x = np.mean(x)
mean_y = np.mean(y)

#Centering the data by subtracting the mean from each row. (adapted from lecture 3/22)
x_centered = x - mean_x
y_centered = y - mean_y

#Centered scatter plot (shifts the x and y axis)
plt.scatter(x_centered, y_centered)
plt.axvline(x=0, color='gray', linestyle='--')
plt.axhline(y=0, color='gray', linestyle='--')

plt.xlabel('Eruption Duration (minutes)')
plt.ylabel('Time Until Next eruption (minutes)')
plt.title('Old Faithful Geyser: Duration of Eruptions vs Length of Time until Next Eruption (Centered Data)')
plt.show()

#Output mean times
print('The mean of the eruption time is:')
print(mean_x)
print('The mean of the waiting time is:')
print(mean_y)
