import pandas as pd
import numpy as np
import quandl


quandl.ApiConfig.api_key = '4cxB9K_871PFs2475SZk'
data =  quandl.get_table('WIKI/PRICES') # taking hole table
data_A = data.loc[data['ticker'] == 'A']    # taking only "A" ticker value


volume = np.log(data_A['volume'])   # Taking log value of the series "volume"
delta = volume - volume.shift(2)    # difference of volume,shifting 2 
drop_data = delta.dropna()  # Drop the NaN values from series delta
delta_rank = drop_data.rank(ascending = False)  # ranking of series

#print len(drop_data)


x1 = (data_A['close'] - data_A['open'])/data_A['open']  # x1 = (close-open)/open
x1_drop_data = x1[2:]   # Dropng frist two values from series x1

#print len(x1_drop_data)


x1_rank = x1_drop_data.rank(ascending = False)  # ranking of series 
m = -1 *(pd.rolling_corr(x1_drop_data, drop_data, window=6))    # correlation between x1_drop_data, drop_data with methods of pearson correlation
n = m.dropna()  # droping the NaN data from m


#print n
