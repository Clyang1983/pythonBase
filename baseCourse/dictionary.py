content_rating2={}
content_rating2['test'] = 'hello world'   #直接增加test:hello world到dictionary里面

print(content_rating2)

content_rating = {'4+':4433,'9+':987,'12+':1155,'17+':622,'18+': content_rating2, '4+':4488}   #dictionary就是一个map，直接用xx={}来定义，key value用:分隔，其中value的类型可以各种各样
#采用 hash()来排列该dictonray   所以如果没法hash的key是不能放入dictornay
print(content_rating)  # 有两个4+，就会取最后一个
print(content_rating['4+'])   # 有两个4+，就会取最后一个

print('测试 4+ 是否在content_raing里面:' + str(('4+' in content_rating)))   #通过in来确定key是否存在

content_rating['4+'] += 100   #某元素直接加100

print(content_rating)


content_rating3=['4+','4+','12+','12+','30+','4+']   #想快速统计里面的数据有多少个，可以用以下办法
content_count={}    #定义一个dictionary用于存放结果，key是key，value是计数
for content_test in content_rating3:
    if(content_test not in content_count):   #如果content_count里面找不到，就设为1，代表第一个
        content_count[content_test] = 1
    else:    #如果content_count里面找到，就累计加1
        content_count[content_test] += 1

print(content_count)


