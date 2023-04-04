# Regression-Analysis-of-Old-Faithful
This repo analyzes data from Old Faithful geyser using linear regression. Python code with NumPy and Pandas is used to plot data, compute correlation, and predict waiting times for given eruption durations.

faithful.csv is the dataset which consists of two variables: the duration of eruptions in minutes (eruptions column) and the length of time until the next
eruption (waiting column). The data comes from the "Old Faithful" geyser in Yellowstone National Park

old-faithful-analysis.py reads data from the 'faithful.csv' file and generates a scatter plot of the duration of eruptions versus time until the next eruption. It also calculates and outputs the mean times of the two variables. Additionally, the code centers the data by subtracting the mean from each row, and generates a second scatter plot using the centered data. The scatter plots can help identify any patterns or trends in the data, while the mean times provide summary statistics that help describe the central tendencies of the dataset. This code is useful for exploratory data analysis and can be used as a starting point for more complex regression analyses. 

correlation.py calculates the correlation between two variables, eruption time and waiting time, in the Old Faithful geyser dataset. The code reads the dataset using pandas, converts columns to numpy arrays, and centers the data. Then, it calculates the correlation using the formula Corr(x,y) = <x,y>/|X||Y| and outputs the result. This code can be useful in understanding the relationship between variables and identifying patterns in the data. 
