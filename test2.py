# -*- coding：utf-8 -*-

a=123
print('''aa
asd
asdsa''')

print(r'''hello,\n
world''')

aa=3>2
print(aa)

print(ord('c'))
print(chr(100))

c='abc'    # 表示把str通过encode()编码成bytes
print(c.encode('utf-8'))

# 表示把bytes通过decode()编码成str
d=b'\xe6\x98\xaf\xe7\x9a\x84\xe6\x92\x92'
print(d.decode('utf-8'))

# r''表示引号内部的不转义
print(r'hello\nworld')

print(int(1.23e9))

# /除法，//整除，%取余
print(9%2)

# 格式化
print('你好，%s，你的号码为%s。'%('李豪',10))

#list列表
list=['ok','ki','test']
print(list[0])
print(list[len(list)-1])
print(list[-1])

list.append(1)  # 插入元素到列表结尾
list.insert(0,'one')    # 插入元素到列表指定位置
list.pop(-2)    # 删除列表中第n个元素
print(list)

q=1.75
w=80.5
if (w/(q*q))<18.5:
    print('过轻')
elif (w/(q*q))<25:
    print('正常')
elif (w/(q*q))<28:
    print('过重')
elif (w/(q*q))<32:
    print('肥胖')
elif (w/(q*q))>32:
    print('严重')

# 求和
sum=0
for vl in range(101):
    sum=sum+vl
print(sum)

# 求奇数之和
sum=0
a1=99
while a1>0:
    sum=sum+a1
    a1=a1-2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello,',name+'!')

test1=1
while test1<=100:
    print(test1)
    test1=test1+1
    if test1==11:
        break
    continue
    print('hello')

# 打印奇数
for a in range(10):
    #print(a)
    a = a + 1
    if a % 2==0:
        continue
    print(a)

ss1=range(101)
sum=0
for shu in ss1:
    sum=sum+shu
print(sum)

d={'A':1,'B':2,'C':3}
print(d['A'])   # 打印字典'A'
# 用dict提供的get()取出键'r'的值，如果键'r'没有值，则返回None
print(d.get('r'))
# 用dict提供的get()取出键'r'的值，如果键'r'没有值，则指定一个值-1
print(d.get('r',-1))

st1=set([1,2,3])
st2=set([2,3,6])
print(st1)

# 添加key
st1.add(4)
print(st1)
st1.add(4)
print(st1)
# 删除key
st1.remove(4)
print(st1)

# 交集
stt=st1&st2
print(stt)
# 并集
stt=st1|st2
print(stt)

f1='ace'
f2=f1.replace('a','A')
print(f2)

f3=(1, 2, 3)
f4={'A':1,'B':(1,2,3)}
print(f4)

def min1(x):
    if x<100:
        return print('这个值小于100')
    else:
        return print('这个值大于100')

min1(22)