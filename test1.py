# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

sa='啦啦啦'+\
   '嘿嘿嘿'+\
   '啊哈哈'
print(sa)

for i in sys.argv:
   print(i)

print(type(1.2),type('we'))   #type 类型
print(type(False))   # bool 为布尔值

aa=True+True   #python3 True、false分别为1和0
print(aa)

print(type(2e+2j)) # complex 为复数

ac='qwert'
print(ac[0:3])
print(ac*2)
