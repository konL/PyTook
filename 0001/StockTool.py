import pandas as pd
from pandas_datareader import data

#计算变化率
def chan(column):
    curPrice=column[252]
    buyPrice=column[0]
    chanPrice=(curPrice-buyPrice)/buyPrice
    return chanPrice
code=input('输入查询股票代码：')
start_date='2019-01-01'
end_date='2020-01-01'
df=data.get_data_yahoo(code,start_date,end_date)
# print(df.head())
print(df.describe())
# print(chan(df['Close']))

import matplotlib.pyplot as plt
plt.plot(df['Close'],color='green')
plt.title('Stock Telsa')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.show()



