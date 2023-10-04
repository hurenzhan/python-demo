# list 基本操作
list1 = [1, 2, 3, 4, 5]
print(list1)
print(list1[0])
print(list1[1:3])  # 切片操作，左闭右开
print(list1[3:1:-1])  # 反向切片操作
print(list1[::-1])  # 反转
print(list1[1:])  # 从指定位置到末尾
print(list1[:3])  # 从开头到指定位置
print(list1[-1])  # 从末尾开始

# list 增加元素
list1.append(6)  # 在末尾添加元素
print(list1)
list1.insert(0, 0)  # 在指定位置添加元素
print(list1)
list1.extend([7, 8, 9])  # 在末尾添加多个元素
print(list1)

# list 删除元素
list1.pop()  # 删除末尾元素
print(list1)
list1.pop(0)  # 删除指定位置元素
del list1[3]  # 删除指定位置元素
print(list1)
list1.remove(2)  # 删除指定元素
print(list1)
# list1.clear()  # 清空列表
# print(list1)

# list 修改元素
list1[1] = 0
print(list1)

# list 查找元素
print(list1.index(0))  # 查找指定元素的位置
print(0 in list1)  # 判断元素是否在列表中

# list 排序
list2 = [1, 3, 2, 5, 4]
list2.sort()  # 升序排序
print(list2)
list2.sort(reverse=True)  # 降序排序
print(list2)
list2.reverse()  # 反转
print(list2)

# list 统计
print(len(list2))  # 统计元素个数
print(max(list2))  # 统计最大值
print(min(list2))  # 统计最小值
print(sum(list2))  # 统计总和
print(list2.count(1))  # 统计指定元素个数

# list for 循环
for i in list2:
    print(i)

# list while 循环
i = 0
while i < len(list2):
    print(list2[i])
    i += 1

# ___________________________________________________________________

# tuple 基本操作
# 1. tuple 元组是不可变的(元组中 list 中的元素可以修改)，不能增删改
# 2. tuple 元组可以查询
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)

# ___________________________________________________________________

# string 基本操作
# 1. string 字符串是不可变的，不能增删改
# 2. string 字符串可以查询
string1 = "hello world"
print(string1)

# string 查询
print(string1[0])
print(string1[1:3])  # 切片操作，左闭右开
print(string1[1:])  # 从指定位置到末尾
print(string1[:3])  # 从开头到指定位置
print(string1[-1])  # 从末尾开始

# string 统计
print(len(string1))  # 统计元素个数
print(max(string1))  # 统计最大值
print(min(string1))  # 统计最小值
print(string1.count("l"))  # 统计指定元素个数

# ___________________________________________________________________

# set 基本操作
# 1. set 集合是可变的，可以增删改
# 2. set 集合不能查询(因为集合是无序的)
# 3. set 集合中的元素是不可重复的
set1 = {1, 2, 3, 4, 5}

# set 增加元素
set1.add(6)  # 添加元素
print(set1)

# set 删除元素
set1.remove(6)  # 删除元素
print(set1)
print(set1.pop())  # 随机取出一个元素

# 取差集
# 1. 集合1 - 集合2 = 集合1中有，集合2中没有的元素
set2 = {1, 2, 3, 8}
print(set1.difference(set2))

# 取交集
# 1. 集合1 & 集合2 = 集合1中有，集合2中也有的元素
print(set1.intersection(set2))

# 取并集
# 1. 集合1 | 集合2 = 集合1中有，集合2中也有的元素，但是不重复
print(set1.union(set2))

# set for 循环
for i in set1:
    print(i)

# ___________________________________________________________________

# dict 基本操作
# 1. dict 字典是可变的，可以增删改
# 2. dict 字典可以查询
# 3. dict 字典中的 key 是不可重复的

# dict 增加元素
dict1 = {"name": "ren", "age": 18}

# dict 删除元素
dict1.pop("name")  # 删除指定 key 的元素
# del dict1["name"]  # 删除指定 key 的元素
print(dict1)

# 获取所有 key
print(dict1.keys())

# 获取所有 value
print(dict1.values())

# 获取所有 key 和 value
print(dict1.items())

# dict for 循环
for key, value in dict1.items():
    print(key, value)

# ___________________________________________________________________

# 数据容器的通用操作
# 1. len() 统计元素个数
# 2. max() 统计最大值
# 3. min() 统计最小值
# 4. sum() 统计总和
# 5. 通用类型转换 list() tuple() set() str()
# 6. 排序 sorted()
# 7. 判断元素是否在容器中 in
# 8. for 循环
