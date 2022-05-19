import pandas as pd
import location as lo


def makeLottery():
    global data_np
    global data_pd

    Location = lo.local
    File = lo.file

    data_pd = pd.read_excel('{}/{}'.format(Location, File),
                            header=None, index_col=None, names=None)
    # header : Row를 얼마나 내릴지, 스타팅 Row값
    data_np = pd.DataFrame.to_numpy(data_pd)


def countLottery6(countList):
    for i in range(len(data_np)):
        tempList = data_np[i]
        for i in range(len(tempList)-1):
            countList[tempList[i]-1] += 1


def countLottery7(countList):
    for i in range(len(data_np)):
        tempList = data_np[i]
        for i in range(len(tempList)):
            countList[tempList[i]-1] += 1


def howManyCount(countList):
    for i in range(45):
        print("No.", i+1, "inside : ", countList[i])
