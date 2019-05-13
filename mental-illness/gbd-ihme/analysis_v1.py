
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("IHME-GBD_2017_DATA-fc25cec6-1.csv")
data = df
data = data[['location', 'sex', 'age', 'cause', 'metric', 'year', 'val', 'upper', 'lower']]

data = data.pivot_table(index=['location', 'sex', 'age', 'cause', 'year'], columns='metric', values=['val', 'upper', 'lower']).reset_index()


data.columns = ['_'.join(col).strip() for col in data.columns.values]

data.columns = ['location', 'sex', 'age', 'cause', 'year', 'low_num',
              'low_perc', 'low_rate', 'up_num', 'up_perc',
              'up_rate', 'val_num', 'val_perc', 'val_rate']

data = data[['location', 'sex', 'age', 'cause', 'year',
                 'val_num', 'low_num', 'up_num',
                 'val_perc', 'low_perc', 'up_perc',
                 'val_rate', 'low_rate', 'up_rate']]

data.head()
