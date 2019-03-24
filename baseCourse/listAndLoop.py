import tensorflow as tf

row_1 = ['Facebook',0.0,'USD',297476,3.5]
row_2 = ['Instagram',0.0,'USD',2161558,4.5]
row_3 = ['Clash of Clans', 0.0, 'USD',2130805,4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
rows= [row_1,row_2,row_3,row_4,row_5]
print(row_1)

row_1.append('yangdayu')  #增加一个元素到list后面
print(row_1)
row_1.remove('yangdayu')
print(row_1)

ratings=[]
for row in rows:
    rating=row[4]
    ratings.append(float(rating))  #把取出来的元素加到一个新的list ratings

avg_rating=sum(ratings)/len(ratings)   #用sum直接把ratings数组进行计算，好方便

print(avg_rating)

some_character='\n'
some_string='id,track_name,size_bytes\n284882215,Fackbook,389879808\n389801252,Instagram,11395481'

split_result=some_string.split(some_character)  #按照给定符号做切分
print(split_result)