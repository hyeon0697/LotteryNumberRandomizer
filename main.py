#################################################
######## 2022/04//11 14:06  #####################
######## 제작자 : 경준현 #########################
######## 사용언어 : python #######################
#################################################

# 제작 의도 : 역대 로도 당첨번호를 엑셀파일로 불러와 가장 많이 등장한 번호 15개를 랜덤하게 돌려 6개의 숫자를 뽑아내는 프로그램

# # 전체 데이터 리스트를 뽑음
# print(data_pd)
# # 행, 열에 맞는 데이터를 뽑아냄.
# print(data_np[Row])
# print(len(data_np))

import useful_function as uf
import copy
import numpy
import random

count_list = [0 for i in range(45)]
bestNumber = []

uf.makeLottery()
uf.countLottery7(count_list)
# uf.howManyCount(count_list)

tempList = copy.deepcopy(count_list)
tempList.sort(reverse=True)

count_list = numpy.array(count_list)

for i in range(15):
    bestNumber += list(numpy.where(count_list == tempList[i])[0])

bestNumber = list(set(bestNumber))
bestNumber.sort()

for i in range(5):
    print("-------list", i+1, "Number-------")
    random.shuffle(bestNumber)
    for i in range(6):
        print("No.", i+1, ":", bestNumber[i]+1)
