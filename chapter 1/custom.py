def test():
    print('test')


# 解释：当直接运行 custom.py 文件时，__name__ 的值是 __main__，当 custom.py 文件被其他文件导入时，__name__ 的值是 custom
if __name__ == '__main__':
    test()

# 解释：当使用 from custom import * 导入时，只能导入 __all__ 中指定的函数
__all__ = ['test']