
# 旧式类定义语法：
class A:
    pass

a1 = A()

print(type(A))

# 新式类定义语法：
class B(object):
    pass

# 第二种新式类的定义语法：在类的前面写上这么一句：__metaclass__ == type，然后定义类的时候，就不需要在名字后面写(object)了。

__metaclass__ = type

class C:
    pass

