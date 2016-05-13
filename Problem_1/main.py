#coding=utf-8
#所有3的倍数构成的列表
list3 = range(0, 1000, 3)
#所有5的倍数构成的列表
list5 = range(0, 1000, 5)
#将两个列表合并
list3_5 = list3 + list5
#利用set特性去除重复的元素
set3_5 = set(list3_5)
#求所有元素和
print sum(set3_5)