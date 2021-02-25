#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''name=input('欢迎:')
print ('hello,',name)
'''

a=1*2
print ('1 * 2 =',a)

if a>3:
    print (a)
else:
    print ('ok')

print (r'\\\t\\')   # \ 为转义符，r 为默认内部字符串不转义

print (r'''hello\ta 
3333
2222''')    #'''xxx''' 也为换行

a='aa'
b='bb'
if a=='aa':
    print ('a')
elif a!='bb':   #elif 或者如果判断
    print ('b')
else:
    print ('c')

x=10
x=x+2
print (x)

a=9//3  # /为浮点数除法，//在整数除整数情况下仍保留整数
print (a)

p=ord ('沙') # ord 获取字符的整数表示
r=chr(66)   # chr 获取整数的字符表示
print(p)
print(r)

'''l=input('请输入')
aaa='li%s,%f'%(l,123)
print(aaa)'''

s1=72
s2=85
rr=72/85*100
print(rr)

'''v=input('请输入：\n')
print(v)'''

print(float(1))
print(int(1.732))
print(str('ewde12落'))
