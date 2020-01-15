a = [1, 2, 3, [4, 5, 6]]
print(a[1], a[3][1])

# 切片
numList = ['1', '2', '3']
print(numList[0:2])
print(numList[1:])
print(numList[:2])
print(numList[-1:])

# 下标及值遍历
for i, value in enumerate([1, 2, 3, 4]):
    print('下标：', i, "值：", value)

# 列表新增及移除操作
list1 = []
list1.append('chl')
print(list1)
list1.remove('chl')
len = list1.__len__()
print('移除后的列表', list1, '长度为', len)

'''
列表生成式  用于生成列表
可执行元素修改，过滤等操作
'''
makeList = [x * x for x in range(1, 10) if x % 2 == 0]
print('列表生成式列表：', makeList)
# 也可以进行合流操作
mergeList = [m + n for m in [1, 2, 3] for n in [1, 2, 3]]
print(mergeList)
