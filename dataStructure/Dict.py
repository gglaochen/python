"""
字典 dict 用花括号包含
"""
dict1 = {1: 'one', 2: 'two', 3: 'three'}
print('字典根据key获取值:', dict1.get(1))
print('如果获取没有的字典:', dict1.get(4))
dict1.pop(1)
print('pop进行根据key移除', dict1)

for key in dict1:
    print(key)
for value in dict1.values():
    print(value)
for key, value in dict1.items():
    print("key:", key, "value:", value)
