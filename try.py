import pandas as pd
import matplotlib.pyplot as plt
dfAAPL = pd.read_csv("AAPL.csv",index_col='Date',
                     parse_dates=True,
                     na_values=['nan'])
#usecols=['Date', 'Adj Close'],
print(list(dfAAPL.columns))
end_date = dfAAPL.index.max()
start_date = dfAAPL.index.min()
dates = pd.date_range(start_date, end_date)
df1 = pd.DataFrame(index=dates)
df1 = df1.join(dfAAPL)
df1 = df1.dropna()
df1[['Open','Close']].plot()
plt.show()
