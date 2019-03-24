import numpy as ny

mylist = [1,2,3,4,5]
print(mylist)
print('len:' + str(len(mylist)))
print('sum:' + str(sum(mylist)))
print('max:' + str(max(mylist)))
print('min:' + str(min(mylist)))
print('mean:' + str(ny.mean(mylist)))
#print('mean first 3:' + str(ny.mean(mylist,3)))
print('square of all:' + str(ny.square(mylist)))    #所有元素都平方

def square2(anumber, bnumber):
    if(bnumber !=0):
        return anumber*bnumber
    return anumber*anumber

print('square2 of all:' + str(square2(anumber=9,bnumber=9)))    #使用自定义函数

def add_value(x=3, constant=10):    #x跟constant都有个默认取值了
    return constant+x
print(add_value())


def sum_and_diff(x,y):    #支持有两个返回值，成为一个tuple  （tuple与list的不同在于tuple里面的元素只要分配了，就不可变更）
    return x+y,x-y

valueOfVandD = sum_and_diff(10,5)

print(valueOfVandD)

