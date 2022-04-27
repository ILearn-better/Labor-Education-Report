import pandas as pd
import os
import random
data=pd.read_excel(os.path.join(os.getcwd(),"单词.xls"))
# print(data)

def check_eglish_word(word):
    bo = data.loc[:,"单词"].values==word
    if sum(bo)>=1:
        return data[bo]
    if sum(bo)==0:
        return "单词不存在,或输入有问题"

def check_word_from_etymon(etymon):
    bo = data.loc[:,"词根"].values==etymon
    if sum(bo)>=1:
        return data[bo]
    if sum(bo)==0:
        return "单词不存在,或输入有问题"

def mark_1(word):
    bo = data.loc[:, "单词"].values == word
    if sum(bo) >= 1:
        data[word].loc[:,"标签"]=1
        data.to_excel("单词.xls")

    if sum(bo) == 0:
        return "单词不存在,或输入有问题"

def mark_0(word):
    bo = data.loc[:, "单词"].values == word
    print(bo)
    if sum(bo) >= 1:
        data.loc[data[bo].index,"标签"]=1
        print(data)
        data.to_excel("单词.xls",index=False)#每运行一次多一列
    if sum(bo) == 0:
        return "单词不存在,或输入有问题"

# def add_word(week,word,etymon,etymon_Chi_mean,word_character,Chinese,label):
#     pass#完全封装时再补充


def random_word(label):
    """"
    先在标签内循环,再在标签外循环,直到单词循环完
    """
    bo=data.loc[:,"标签"]==label
    da= data[bo].loc[:, "单词"].values
    index = list(range(len(da)))
    random.shuffle(index)
    for i in index:
        yield da[i]
    # judge=[]
    # i=0
    # while(i<=len(da)):
    #     num=random.randint(0,len(da)-1)
    #     if_judge = num not in judge
    #     print(if_judge)
    #     if if_judge:
    #         # print(da[num])
    #         judge.append(num)
    #         i=i+1
            #问题:运算效率过低

#
# choice = input("请输入你想要查看词还是词根?(词输:0;词根输:1)")
# word_or_etymon = input("请输入你要查询的单词或词根:")
#
# if choice=='0':
#     print(check_eglish_word(word_or_etymon))
# if choice=='1':
#     print(check_word_from_etymon(word_or_etymon))

"""=========================================================="""
# for i in random_word(0):
#     print(i)
#
# print("\n")
#
# raaaa = random_word(0)
# for i in range(7):
#     print(next(raaaa))
"""=========================================================="""
mark_0("significance")