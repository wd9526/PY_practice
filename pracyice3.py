#6、python实现列表去重的方法
lis=[11,12,13,12,15,16,13]
a=set(lis)
print(a)

y=[int(x) for x in a]
print(y)