# 捕获异常
try:
    print(a)
    open("xxx", "r", encoding="utf-8")
except NameError as e:
    print(e, 'NameError')
except Exception as e:
    print(e, 'Exception')
else:
    print('没有异常才会执行')
finally:
    print('有没有异常都会执行')

# 捕获多个异常
try:
    print(b)
    open("xxx", "r", encoding="utf-8")
except (NameError, Exception) as e:
    print(e, 'NameError, Exception')

# 模块
# 1. 模块是一个 Python 文件
# 导入方式:
# 1. import 模块名 (作用：导入模块)
# 2. from 模块名 import 函数名 (作用：导入模块中的函数)
# 3. from 模块名 import * (作用：导入模块中的所有函数)
# 4. import 模块名 as 别名 (作用：导入模块并起别名)

import time
import custom

print(time.time(), 'start time')
time.sleep(2)
print(time.time(), 'end time')

# 调用自定义模块
custom.test()

# 包
# 1. 包是一个文件夹
# 2. 包中必须包含一个 __init__.py 文件
# 3. 包中可以包含多个模块

# 调用自定义包
# from my_package import my_module1
# from my_package import my_module2
from my_package import *

my_module1.info_print1()
my_module2.info_print2()
