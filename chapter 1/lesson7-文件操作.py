# 文件编码的概念
# 文件编码是指将字符转换成字节的编码方式
# 编码是规则集合，可以理解为一种对应关系，字符和字节之间的对应关系
# 1. ASCII编码
# 2. Unicode编码
# 3. UTF-8编码
# 4. BIG5编码
# 最常用的是UTF-8编码

# open() 函数的基础用法
# 1. 函数用于打开文件或者创建文件
# 2. 函数的第一个参数是文件路径
# 3. 函数的第二个参数是打开文件的模式 r w a 分别表示读、写、追加
# 4. 函数的第三个参数是打开文件的编码，默认是 UTF-8
# 5. 函数的返回值是一个文件对象
# 6. 文件对象的方法有：
# read(): 读取文件内容 参数1：读取的长度，单位是字节 参数2：读取的编码 默认是 UTF-8。
# readline(): 读取文件内容，返回一行  参数：读取的编码 默认是 UTF-8
# readlines(): 读取文件内容，返回一个列表，列表中的每个元素是一行  参数：读取的编码 默认是 UTF-8
# write(): 写入文件内容 参数1：写入的内容 参数2：写入的编码 默认是 UTF-8
# close(): 关闭文件 参数：无
# 读取操作多次调用的话，会从上次读取的位置开始读取

# write() 函数的基础用法
# 1. 函数用于写入文件内容
# 2. 函数的第一个参数是写入的内容
# 3. 函数的第二个参数是写入的编码，默认是 UTF-8
# 4. 函数的返回值是写入的字符数
# 5. 写入操作多次调用的话，会从上次写入的位置开始写入
# 5. flush() 函数用于将内存的内容写入到文件中
# 7. 写入操作实际上是将内容写入到内存中，当调用 flush() 或者 close() 时，才会将内容写入到文件中

# 读取
file = open("test.txt", "r", encoding="utf-8")
# print(file.read(), 'file - read')
# print(file.readline(), 'file - readline')
# print(file.readlines(), 'file - readlines')

# 循环读取
for line in file:
    print(line)

# 关闭文件
file.close()

# with open() 操作完文件后会自动关闭文件
with open("test.txt", "r", encoding="utf-8") as file:
    print(file.read(), 'with open')
# 写入
file = open("test.txt", "a", encoding="utf-8")
file.write("\n写入测试")
file.close()
