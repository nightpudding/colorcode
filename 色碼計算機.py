# -*-coding:utf-8-*-
# symbol
r = input('請輸入R值')
g = input('請輸入G值')
b = input('請輸入B值')
trans = input('輸出進位數')
color = [r,g,b]

# check1
try:
    cons = 0
    for i in color:
        i = int(i)
        color[cons] = i
        cons += 1
except:
    for i in color:

        i=list(i)
        for c in range(0,2):
            if i[c].isdigit():
                i[c] = int(i[c])
            elif i[c] == 'a':
                i[c] = 10
            elif i[c] == 'b':
                i[c] = 11
            elif i[c] == 'c':
                i[c] = 12
            elif i[c] == 'd':
                i[c] = 13
            elif i[c] == 'e':
                i[c] = 14
            elif i[c] == 'f':
                i[c] = 15
            else :
                print('請輸入在0~255之間的十進位數字或十六進位數字')

        i = i[0]*16 + i[1]
        color[cons] = i
        cons += 1

# check2
for i in color:
    if i >= 256:
        print('請輸入小於256的十進位數字或十六進位數字')
        break
    elif i <= -1:
        print('請輸入大於0的十進位數字或十六進位數字')
        break
    else:
        continue

# color10
if trans == '10':
    print("R值: "+ str(color[0]))
    print("G值: "+ str(color[1]))
    print("B值: "+ str(color[2]))

# color16    
if trans == '16':
    d = 0
    for i in color:
        trans16 = [str(i//16) , str(i%16)]
        for c in range(0,2):
            if trans16[c] == '10':
                trans16[c] = 'a'
            elif trans16[c] == '11':
                trans16[c] = 'b'
            elif trans16[c] == '12':
                trans16[c] = 'c'
            elif trans16[c] == '13':
                trans16[c] = 'd'
            elif trans16[c] == '14':
                trans16[c] = 'e'
            elif trans16[c] == '15':
                trans16[c] = 'f'
            else :
                trans16[c] = trans16[c]
        i = trans16[0] + trans16[1]
        color[d] = i
        d += 1

    print("R值: "+ color[0])
    print("G值: "+ color[1])
    print("B值: "+ color[2])
print(input("點擊一下enter以結束應用程式"))


    

