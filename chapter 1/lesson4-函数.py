# 函数的基础用法
# 1. 使用 """ """ 或者 ''' ''' 来定义函数的注释
def add(a, b=3):
    """
    两个数相加
    :param a: 数字1
    :param b: 数字2
    :return: 相加结果
    """
    return a + b


print(add(1, 2))
