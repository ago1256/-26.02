import csv
with open('songs.csv', 'r', encoding='utf-8') as f:
    with open('rusian_artists.txt', 'w', encoding='utf-8') as ru:
      with open('foreign_artists.txt', 'w', encoding='utf-8') as fo:
        s = f.read().split('\n')[1:-1]
        rus = 0 #количество русских исполнителей(впоследствие будет изменяться)
        forg = 0 #количество иностранных исполнителей(впоследствие будет изменяться)
        alp = 'цукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
        for i in s:
            st = i.split(';')
            if len([j for j in st[1] if j in alp])  >0:#смотрим есть ли русские буквы в названии исполнителя
                rus += 1
                ru.write(st[1]+'\n')
            elif st[1] != 'unknown':
                forg += 1
                fo.write(st[1]+'\n')
print(f'Количество российских исполнителей: {rus}')
print(f'Количество иностранных исполнителей: {forg}')
