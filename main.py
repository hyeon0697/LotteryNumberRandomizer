#################################################
######## 2022/04//11 14:06  #####################
######## 제작자 : 경준현 #########################
######## 사용언어 : python #######################
#################################################

import pandas as pd

Location = './../LotteryNumberRandomizer'
File = 'data.xls'

Row = 0
Column = 5

data_pd = pd.read_excel('{}/{}'.format(Location, File), header = None, index_col = None, names = None)
data_np = pd.DataFrame.to_numpy(data_pd)

print(data_pd)
print(data_np[Row][Column])