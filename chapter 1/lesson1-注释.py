# 多个变量字符串格式化
# 1. %s %d %f 表示将内容格式化为字符串，整数，浮点数
# 2. .2 表示保留两位小数并四舍五入
print("I am %s, I am %d years old or %.2f years old." % ("ren", 100, 19.99))

# 字符串格式化快速写法
# 1. 使用f开头，将变量名放在{}中
name = "ren"
age = 19.996
print(f"I am {name}, I am {age} years old or {age:.2f} years old.")
