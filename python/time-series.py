
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


#### Seasonality
# Autocorrelation plot
fig = tsaplots.plot_acf(flights['passengers'], lags=24)

# Partial Autocorrelation
fig = tsaplots.plot_pacf(flights['passengers'], lags=24)


#### Time Series Decomposition
import statsmodels.api as sm
from pylab import rcParams
decomposition = sm.tsa.seasonal_decompose(flights)
rcParams['figure.figsize'] = 11, 9
fig = decomposition.plot()
plt.show()

# Plot Individual Decomposed components
trend = decomposition.trend
ax = trend.plot(figsize=(12, 6), fontsize=6)
plt.show()



# Mutiple Time Series
# Modifying some of the passenger data
flights['kids'] = round(flights['passengers']/50) + random.randint(0, 2)
flights['baggage'] = flights['passengers'] - random.randint(10, 100)

# multiple time series plot
flights.plot()

# time series area plot
flights.plot.area()

# summary stats to plots
flights_mean = pd.DataFrame(flights.mean()).transpose()
flights_mean = flights_mean.rename(index={0:'mean'})

ax = flights.plot(fontsize=6, linewidth=1)

# Add x-axis labels
ax.set_xlabel('Date', fontsize=6)

# Add summary table information to the plot
ax.table(cellText=flights_mean.values,
         colWidths = [0.15]*len(flights_mean.columns),
         rowLabels=flights_mean.index,
         colLabels=flights_mean.columns,
         loc='top')


#### Subplots for multiple time series
# How to create multiple plots so scaling issues are minimized
flights.plot(subplots=True,
          layout=(3,1),
          sharex=False,
          sharey=False,
          colormap='viridis',
          fontsize=10,
          legend=True,
          linewidth=0.5)

plt.show()


#### Correlations for time-series

flight_corr = flights.corr()
flight_corr

# Making a heatmat
sns.heatmap(flight_corr,
            annot=True,
            linewidths=0.4,
            annot_kws={"size": 10})
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.show()


# Making a cluster heatmat
fig = sns.clustermap(flight_corr,
                     row_cluster=True,
                     col_cluster=True,
                     figsize=(10, 10))

plt.setp(fig.ax_heatmap.xaxis.get_majorticklabels(), rotation=90)
plt.setp(fig.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
plt.show()
