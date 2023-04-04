import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/faithful.csv')

x = np.asarray(df['eruptions'])
y = np.asarray(df['waiting'])

mean_x = np.mean(x)
mean_y = np.mean(y)

#Calculation for linear regression model
#Both the alpha and beta formulas for linear regression are adapted from lecture 3/13:
#Calculation for beta (slope)
#Beta = <x,y>/|x|^2
beta = np.dot(x - mean_x, y - mean_y) / np.sum((x - mean_x) ** 2)

#Calculation for alpha (intercept)
#Alpha = y - (Beta*x)
alpha = mean_y - beta * mean_x

#Original uncentered data
plt.scatter(x, y)
plt.xlabel('Eruption duration (minutes)')
plt.ylabel('Time until next eruption (minutes)')
plt.title('Old Faithful Geyser: Duration of Eruptions vs Length of Time until Next Eruption ')

#Linear regression model, colored RED
plt.plot(x, alpha + beta * x, color='red')

plt.show()

#Output slope and y-intercept
print(f"Slope: {beta}")
print(f"Y Intercept: {alpha}")

#Calculation for R^2 statistic
#Regression model equation to get predicted y values
y_pred = alpha + beta * x

#Calculation for value e (error)
error = y - y_pred

#SSE value (Sum of Squared Residual Errors aka UNexplained variance in Y)
#SST value (Sum of Squared Totals aka total variance in Y)
#R^2 = 1 - (unexplained variance in Y / total variance in Y)
ss_err = np.sum(error ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r_2 = 1 - (ss_err / ss_tot)

#Output R^2 value
print(f"R^2: {r_2}")
