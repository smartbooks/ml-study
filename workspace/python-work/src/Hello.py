# encoding:utf-8

from oop.A import A
import oop.A as A2

# 普通打印函数
print("Hello.py")

# 全局共享10
A.id = 5

# 类实例a测试
a = A("A1", "A2")
a.id = 50
a.printA("a-title")
a.welcomeA()
a.testException()

# 类实例b测试
b = A("B1", "B2")
b.printA("b-title")
b.welcomeA()
b.testException()

print("-----------------A2--------------------")
tb = A2.A("OOO", "PPP")
tb.printA("TB")
tb.welcomeA()
tb.testException()
