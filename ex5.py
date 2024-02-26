import csv
f=open('songs.csv','r',encoding='utf-8')
s=f.read().split('\n')[1:-1]
d={}
def hashtable(s):
    global d
    ##Создание хэш-таблицы, в которой ключом
    ##будет являться имя исполнителя,
    ##а значением количество его песен в базе данных.
    for i in s:
        st=i.split(';')
        if st[1] in d.keys():
            d[st[1]]+=1
        else:
            d[st[1]]=1
    return d
g=hashtable(s)
g=sorted(g.items(),key=lambda x: x[1],reverse=True)#сортируем по количеству песен в БД
g=dict(g)
k=0
for i in g.keys():
    print(f'{i} выпустил {d[i]} песен.')
    k+=1
    if k==10:
        break
 
