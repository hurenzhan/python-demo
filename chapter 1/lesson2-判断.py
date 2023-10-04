# 按年龄分类
age = int(input("请输入你的年龄："))

if age < 0:
    print("你还没出生呢")
elif age < 18:
    print("你是未成年人")
elif age < 30:
    print("你是青年人")
elif age < 50:
    print("你是中年人")
else:
    print("你是老年人")

# 用户输入嵌入 if 判断
if input("请输入你的性别：") == "男":
    print("你是男性")
elif input("请输入你的性别：") == "女":
    print("你是女性")
else:
    print("你是妖怪吧")
