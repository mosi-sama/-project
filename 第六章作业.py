import os
path = 'C:/Users/Hasee/Documents/mypython课件/chap06/06章.Python IO编程（含实验作业要求）/dataset'
file_list = os.listdir(path)
file_name = file_list[:11]
x = 0
newfile = path + '/' + 'date.txt'
while True:
    if x < 10:
        n = path + '/' + file_name[x]
        if n != newfile:
            with open(n, mode='r', encoding='gbk') as f:
                n_reirong = f.read()
            with open(newfile, mode='a', encoding='gbk') as f:
                f.write(n_reirong)
            x = x + 1
        elif n == newfile:
            x = x + 1
    elif x >= 10:
        break