
# Python Script for all time-series related notebook


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data and create the proper column for time series
flights = sns.load_dataset('flights')
flights['year'] = flights['year'].astype('str')
flights['month'] = flights['month'].astype('str')
flights['date'] = flights['month'] + ' ' + flights['year']


flights['date'] = pd.to_datetime(flights['date'])

# Set the index to be the date. This is important
flights = flights.set_index('date')
flights = flights[['passengers']]

flights.head()

# Sets the style of your plot. Multiple options
plt.style.use('fivethirtyeight')

# Setting the flight plot to ax and adding basic modifications
ax = flights.plot(color='black')
# ax = flights.plot(color='blue',
#                   figsize=(8, 4), fontsize=8,
#                   linewidth=3, linestyle='--')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Passengers')
ax.set_title("Passengers over time")
plt.show();


print(plt.style.available)


# Vertical Line, horizontal line
ax = flights.plot(color='black')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Passengers')
ax.set_title("Passengers over time")
# The markers for vertical and horizontal lines
ax.axvline('1957-01-01', color='red', linestyle='--')
ax.axhline(300, color='green', linestyle='--')
plt.show();

# Shading plot, shade plot, shade parts of plot
ax = flights.plot(color='black')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Passengers')
ax.set_title("Passengers over time")

# The shading using 'span'
ax.axvspan('1957-01-01', '1957-06-06', color='red', linestyle='--')
# ax.axhspan(300, 400, color='green', linestyle='--')
plt.show();


# plot single column time series
flights['passengers*2'] = flights['passengers'] * 2
ax = flights['passengers*2'].plot(color='black')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Passengers * 2')
ax.set_title("Passengers over time")
plt.show();


###
### Aggregation
###

# Rolling average
flights = flights[['passengers']]
flights_averages = flights.rolling(window=12).mean()
# .mean can be .std or other function

# Setting the flight plot to ax and adding basic modifications
ax = flights_averages.plot(color='black')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Passengers')
ax.set_title("Passengers over time")
plt.show();


# Aggregate by year, month or day
idx = flights.index.month
flights_idx = flights.groupby(idx).mean()
flights_idx.plot()
plt.show()

# flights.index.year
# flights.index.month
# flights.index.day


# Boxplot
ax = flights.boxplot()
ax.set_xlabel('Passengers', fontsize=10)
ax.set_ylabel('Number of Passengers', fontsize=10)
plt.show()

# Histogram
ax = flights.plot(kind='hist', bins=25, fontsize=5)
ax.set_xlabel('Passengers', fontsize=10)
ax.set_ylabel('Number of Passengers', fontsize=10)
plt.show()

# Density Plot
# Better to use density to show distribution because histogram is unstable with the number of bins
ax = flights.plot(kind='density', linewidth=4, fontsize=6)
ax.set_xlabel('Passengers', fontsize=10)
ax.set_ylabel('Number of Passengers', fontsize=10)
plt.show()
