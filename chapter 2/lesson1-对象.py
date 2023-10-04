# class 的基本使用
class Student1():
    name = 'xiaoming'
    age = 18

    def say(self):
        self.name = 'xiaohong'
        self.age = 20
        print('My name is {0}'.format(self.name))
        print('My age is {0}'.format(self.age))


stu_1 = Student1()
stu_1.say()


# class 构造方法
class Student2():
    name = 'xiaoming'
    age = 18

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('My name is {0}'.format(self.name))
        print('My age is {0}'.format(self.age))


stu_2 = Student2('xiaohong', 20)
stu_2.say()


# class 继承
class Person():
    name = 'xiaoming'
    age = 18

    def eat(self):
        print('eat food')

    def drink(self):
        print('drink water')


class PersonChild(Person):
    def study(self):
        print('study')

    # 重写父类方法
    def eat(self):
        super().eat()  # 调用父类方法
        print('child eat food')


person_child: PersonChild = PersonChild()
person_child.eat()
person_child.drink()
person_child.study()


# 多态
# 1. 多态是一种技巧，不是一种语法
# 2. 多态的前提是继承
# 3. 多态的作用是增加代码的灵活度
# 4. 多态的表现形式是：父类的引用指向子类的对象
# 5. 多态的好处是：调用方法的时候，不需要关心对象的类型，只需要关心对象有没有这个方法

class Animal():
    def eat(self):
        print('eat food')


class Dog(Animal):
    def eat(self):
        print('dog eat food')


class Cat(Animal):
    def eat(self):
        print('cat eat food')


def func(animal):
    animal.eat()


dog = Dog()
cat = Cat()
func(dog)
func(cat)

# 基础数据类型注解
var_1: int = 1
var_2: float = 1.1
var_3: bool = True
var_4: str = 'hello'
var_5: list[int] = [1, 2, 3]
var_6: tuple[int, int, int] = (1, 2, 3)
var_7: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
var_8: set[int] = {1, 2, 3}
var_9: frozenset = frozenset({1, 2, 3})


# 函数注解
def func_1(a: int, b: int) -> int:
    return a + b


# Union 联合类型注解
from typing import Union

var_10: list[Union[int, str]] = [1, 2, '3', '4']
var_11: dict[str, Union[int, str]] = {'a': 1, 'b': '2', 'c': 3}
