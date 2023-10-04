# 函数的多返回值
# 1. 函数的返回值可以是多个
# 2. 返回值是元组类型
def func1():
    return 1, 2, 3


x, y, z = func1()
print(x, y, z)


# 不定长参数
# 1. 函数的参数可以是不定长的
# 2. 函数的参数可以是元组类型
# 3. 函数的参数可以是元组类型的拆包
def func2(*args):
    print(args)


func2(1, 2, 3)


# 键值对参数
# 1. 函数的参数可以是键值对的形式
# 2. 函数的参数可以是字典类型
# 3. 函数的参数可以是字典类型的拆包
def func3(**kwargs):
    print(kwargs)


func3(a=1, b=2, c=3)

dict1 = {"a": 1, "b": 2, "c": 3}

func3(**dict1)


def func4(a, b, c):
    print(a, b, c)


func4(1, b=2, c=3)


# 函数作为参数
# 1. 函数的参数可以是函数
# 2. 函数的参数可以是函数的拆包
def func5(a, b, c):
    print(a, b, c)


def func6(func, *args):
    func(*args)


func6(func5, 1, 2, 3)

# lambda 表达式
# 1. lambda 表达式是一个匿名函数
# 2. lambda 表达式的返回值是一个函数
# 3. lambda 表达式函数体只能有一行代码


func6(lambda a, b, c: print(a, b, c), 1, 2, 3)
