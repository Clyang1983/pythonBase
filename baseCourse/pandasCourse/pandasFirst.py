import numpy as ny
import csv

f = open('nyc_taxis.csv','r')    #打开csv文件
taxi_list = list(csv.reader(f))[1:]   #读取成list  ，并且去掉表头

converted_taxi_list = []

for taxi_info in taxi_list:
    converted_info = []
    for item in taxi_info:
        converted_info.append(float(item))
    converted_taxi_list.append(converted_info)

print(converted_taxi_list)
