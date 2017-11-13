'''
Function：将原始测试集改为sklearn-model所需的测试集格式，最终为.csv文件
Date: 13/11/2017
Author: Ciel
'''

import csv, sys, os

##############################写表头##############################
#step1. 写表头：class（是不是光源）,feature1，feature2 ··· feature342
headTitle=['class']
for i in range(2,344):
    headTitle.append('feature'+str(i-1))
#step2. 写入csv文件
#获取脚本路径
path = sys.path[0]
# print (path)
newtestFileName = path + "\\data\pano_aabrsshujmskyq.csv"
newtestFile=open(newtestFileName,"w", newline='')
# newtestFile=open("modify.csv", "w", newline='')  #测试文件
csv_writer=csv.writer(newtestFile, dialect='excel')
csv_writer.writerow(headTitle)

#打开原始训练集rawtrain.txt
rawtestFileName = path + "\\data\pano_aabrsshujmskyq.txt"
rawtestFile=open(rawtestFileName,"r")
# rawtestFile=open("test.txt","r")  #测试文件

#逐行读取
fileEnd=0  #fileEnd：读到txt文件结尾的标志。0表示没有到结尾，1到了结尾
rowNum=0  #rowNum：txt的行数
while not fileEnd:
    lineContent=rawtestFile.readline()  #lineContent：每行内容

    if(lineContent != ''):
        rowNum=rowNum+1

        #默认分隔符为空格（不管有几个空格），进行分割字符串lineContent，存入splitLine中
        splitLine=lineContent.split()
        colNum=len(splitLine)  #colNum=列数，下标0~n-1
        #print(colNum)
        '''
        修改格式为sklearn-model的测试集，即
        表头：class，feature1 feature2···feature342
        rawtrain.txt中，每行有344列
        第2列为class，第3-344列为342个特征的value
        '''
        trainSample=[str(splitLine[1])]   # class
        for i in range(2, colNum):  # feature(i)
            trainSample.append(splitLine[i])
        csv_writer=csv.writer(newtestFile, dialect='excel')
        csv_writer.writerow(trainSample)
            
    else:
        fileEnd=1

#print(rowNum)

rawtestFile.close()
newtestFile.close()


