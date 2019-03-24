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




