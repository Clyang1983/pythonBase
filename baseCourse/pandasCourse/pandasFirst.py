import numpy as np
import csv

f = open('nyc_taxis.csv','r')    #打开csv文件
taxi_list = list(csv.reader(f))[1:]   #读取成list  ，并且去掉表头

converted_taxi_list = []

for taxi_info in taxi_list:
    converted_info = []
    for item in taxi_info:
        converted_info.append(float(item))
    converted_taxi_list.append(converted_info)

dataArray = np.array(converted_taxi_list)    #把 list转换成 numpy的array，这是个n维数组，方便用于计算，因此里面只能是同一种类型的数据，例如都是数字
                                             #numpy的array比 list of list快30倍，在查找的时候

#print(dataArray)
print(dataArray.shape)   #打印有多少行多少列
print(dataArray[0,1:])



col_distance = dataArray[:,7]   # 把所有第七列取出来，距离（公里）
col_length = dataArray[:,8]   #把所有第八列取出来，时间（秒）
speed=col_distance/(col_length/3600)
print(speed.min())    #做两列运算     计算时速   //两种运算都可以的，用函数或者用变量本身方法

print(np.min(speed))  #计算最小值

pirnt(dataArray.max(axis=0))   #设axis=i ,则numpy沿着第i个下标变化的方向进行操作，
pirnt(dataArray.max(axis=1))   #设axis=i ,则numpy沿着第i个下标变化的方向进行操作，