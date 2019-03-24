datas=[['game','Zombie vs Plant',3.5,2.0],['app','what\'s app',4.5,1.0],['app','free train',0.0,1.0]]
for data in datas:    #记得加冒号在后面
    if (data[0]=='game' or data[0]=='app' )and data[2]!=0.0:
        data.append("no free")
        print(data)
    if data[2]==0.0:
        data.append("free")
    else:
        data.append("unknown")

print(datas)



