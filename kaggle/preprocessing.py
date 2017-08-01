import pandas as pd

data = pd.read_csv("train.csv")
# print(data)
#这一步相当于将male改成1，female改成0
newData = data.replace("male",1).replace("female",0)
# 根据Embarked来增加四列，分别为Embarked_C，Embarked_Q，Embarked_S，Embarked_U
#Embarked为C,Q,S时对应的值设为1，否则U等于1
def addColumnC(data):
    if data.Embarked == 'C':
        return 1
    else:
        return 0
def addColumnQ(data):
    if data.Embarked == 'Q':
        return 1
    else:
        return 0
def addColumnS(data):
    if data.Embarked == 'S':
        return 1
    else:
        return 0
def addColumnU(data):
    if data.Embarked == '':
        return 1
    else:
        return 0
newData['Embarked_C'] = newData.apply(addColumnC,axis=1)
newData['Embarked_Q'] = newData.apply(addColumnQ,axis=1)
newData['Embarked_S'] = newData.apply(addColumnS,axis=1)
newData['Embarked_U'] = newData.apply(addColumnU,axis=1)
newData.to_csv("train2.csv")