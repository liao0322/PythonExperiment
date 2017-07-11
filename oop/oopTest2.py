
__metaclass__ = type




class Student:
    name = 'student' # 定义一个类属性或静态数据

print(Student.name)


s = Student()
print(s.name) # 通过实例也可以得到这个属性，这个属性叫做实例属性


# 实例属性更新了，类属性没有改变，说明类属性不会被实例属性所左右，本质是实例s又建立了一个新的属性，因为与类属性同名，所以覆盖了后者
s.name = 'lili'
print(s.name)
print(Student.name)

del s.name # 把实例s的实例属性name删除之后，s.name还是类属性的值
print(s.name)
print(Student.name)