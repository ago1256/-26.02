import csv
f=open('songs.csv','r',encoding='utf-8')
s=f.read().split('\n')[1:-1]
a=input()
fl=0
while a!='0':
    for i in s:
        st=i.split(';')
        if st[1]==a:
            print(f'У артиста {st[1]} найдена песня {st[2]}')
            fl=1
    if fl==0:
        print('К сожалению, ничего не удалось найти')
    a=input()