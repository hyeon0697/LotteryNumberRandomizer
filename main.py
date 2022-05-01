#################################################
######## 2022/04//11 14:06  #####################
######## 제작자 : 경준현 #########################
######## 사용언어 : python #######################
#################################################

#제작 의도 : 역대 로도 당첨번호를 엑셀파일로 불러와 가장 많이 등장한 번호 15개를 랜덤하게 돌려 6개의 숫자를 뽑아내는 프로그램

import pandas as pd

Location = './../LotteryNumberRandomizer'
File = 'data.xls'

Row = 3
Column = 5

data_pd = pd.read_excel('{}/{}'.format(Location, File), header = None, index_col = None, names = None)
#header : Row를 얼마나 내릴지, 스타팅 Row값
data_np = pd.DataFrame.to_numpy(data_pd)

#전체 데이터 리스트를 뽑음
print(data_pd)
#행, 열에 맞는 데이터를 뽑아냄.
print(data_np[Row])

