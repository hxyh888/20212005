a = [12,34,345,546,657,67,78]
#从大到小排序
#第一层循环 遍历他的长度的数
for i in range(len(a)):
    #第二层循环  找出每一次的最大数
    for j in range(len(a)-i):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
print(123)
