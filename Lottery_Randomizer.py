#########################################################
################ 2022/04//11 14:06  #####################
################ 제작자 : 경준현 #########################
################ 사용언어 : python #######################
#########################################################

# 제작 의도 : 역대 로도 당첨번호를 엑셀파일로 불러와 가장 많이 등장한 번호 15개를 랜덤하게 돌려 6개의 숫자를 뽑아내는 프로그램

# # 전체 데이터 리스트를 뽑음
# print(data_pd)
# # 행, 열에 맞는 데이터를 뽑아냄.
# print(data_np[Row])
# print(len(data_np))

import useful_function as uf

import sys
import subprocess

try:
    # 없는 모듈 import시 에러 발생
    import pandas
except:
    # pip 모듈 업그레이드
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pip'])
    # 에러 발생한 모듈 설치
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pandas'])
    # 다시 import
    import pandas

uf.makeLottery()


while(1):
    print("\n\n\n")
    print("#########################################################################")
    print("#########################################################################")
    print("##########################Lottery Randomizer#############################")
    print("#########################################################################")
    print("#########################################################################")
    print("\n\n\n")

    count_list = [0 for i in range(45)]
    bestNumber = []

    print("1. bestNumber 6\n")
    print("2. bestNumber 7\n")
    print("3. how Many Count Number?\n")
    print("9. help\n")
    print("0. end Program\n")

    print("select your choice : ", end="")
    cNum = input()
    if cNum == '':
        continue
    else:
        cNum = int(cNum)
    

    if cNum == 1:
        uf.countLottery6(count_list)
        uf.resultOfBestNumber(count_list, bestNumber)
        uf.printResult(bestNumber)
        print("press Enter...", end="")
        input()
    elif cNum == 2:
        uf.countLottery7(count_list)
        uf.resultOfBestNumber(count_list, bestNumber)
        uf.printResult(bestNumber)
        print("press Enter...", end="")
        input()
    elif cNum == 3:
        print("select 6 or 7? : ", end="")
        num = int(input())

        if 6 == num:
            uf.countLottery6(count_list)
            uf.howManyCount(count_list)
            print("press Enter...", end="")
            input()
        elif 7 == num:
            uf.countLottery7(count_list)
            uf.howManyCount(count_list)
            print("press Enter...", end="")
            input()
        else:
            print("plese, don't put it other number")
            print("press Enter...", end="")
            input()
    elif cNum == 9:
        print("\n\n\n")
        print("#########################################################################")
        print("#########################################################################")
        print("###############################help menu#################################")
        print("#########################################################################")
        print("#########################################################################")
        print("\n\n\n")

        print("1. bestNumber 6\n")
        print("2. bestNumber 7\n")
        print("3. how Many Count Number?\n")

        print("select your choice : ", end="")
        hNum = input()

        if hNum == '':
            continue
        else:
            hNum = int(hNum)

        if hNum == 1:
            print("'bestNumber 6' is randomize Lottery Number, in Lottery source called 'winning number' select 6 pieces")
            print("press Enter...", end="")
            input()
        elif hNum == 2:
            print("'bestNumber 7' is randomize Lottery Number, in Lottery source called 'winning number' select 7 pieces")
            print("press Enter...", end="")
            input()
        elif hNum == 3:
            print(
                "'how Many Count Number' is in 45 pieces lottery numbers, counting how much each output")
            print("press Enter...", end="")
            input()
        else:
            print("plese, don't put it other number")
            print("press Enter...", end="")
            input()
            continue
    elif cNum == 0:
        print("are you realy end this program? [y/n] : ", end="")
        answer = input()
        if "y" == answer or "Y" == answer:
            break
        elif "n" == answer or "N" == answer:
            pass
        else:
            print("plese, don't put it other char")
            print("press Enter...", end="")
            input()
            continue

    else:
        print("plese, don't put it other number")
        print("press Enter...", end="")
        input()
