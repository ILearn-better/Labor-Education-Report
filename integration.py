import pandas as pd
import os
import random

class word():
    def __init__(self,dir):
        self.data= pd.read_excel(dir)

    def check_eglish_word(self,word):
        bo = self.data.loc[:,"单词"].values==word
        if sum(bo)>=1:
            return self.data[bo]
        if sum(bo)==0:
            return "单词不存在,或输入有问题"

    def check_word_from_etymon(self,etymon):
        bo = self.data.loc[:,"词根"].values==etymon
        if sum(bo)>=1:
            return self.data[bo]
        if sum(bo)==0:
            return "单词不存在,或输入有问题"


    def mark_(self,word,num):
        if (num==1 or num==0):
            bo = self.data.loc[:, "单词"].values == word
            # print(bo)
            if sum(bo) >= 1:
                self.data.loc[self.data[bo].index,"标签"]=num
                # print(self.data)
                self.data.to_excel("单词.xls",index=False)#index不写入列名字
            if sum(bo) == 0:
                return "单词不存在,或输入有问题"
        else:
            num=input("请输入0或1:")
            num = int(num)
            self.mark_(word,num)
    # def add_word(week,word,etymon,etymon_Chi_mean,word_character,Chinese,label):
    #     pass#完全封装时再补充


    def random_word(self,label):
        """"
        先在标签内循环,再在标签外循环,直到单词循环完
        """
        bo=self.data.loc[:,"标签"]==label
        da= self.data[bo].loc[:, "单词"].values
        index = list(range(len(da)))
        random.shuffle(index)
        for i in index:
            yield da[i]



if __name__=="__main__":
    w = word(os.path.join(os.getcwd(),"单词.xls"))
    print("====================================")
    print("模糊词汇:")
    for j in w.random_word(1):
        print(j)
        num = input("记得1,不记得0:")
        w.mark_(j, int(num))

        print("-------------------------------------------------------------")
        print(w.check_eglish_word(j))
        print("-------------------------------------------------------------")
    print("====================================")

    print("易忘词汇:")
    for i in w.random_word(0):
        print(i)
        num = input("记得1,不记得0:")
        w.mark_(i, int(num))
        print("-------------------------------------------------------------")
        print(w.check_eglish_word(i))
        print("-------------------------------------------------------------")
    print("====================================")


