
"""闭包演示"""

# 现有如下函数，请问如何执行内部的inner函数？
def outer():
    x = 10
    def inner():
        print(x)

    return inner


# 第一种方式：
foo = outer()
foo()

# 第二种方式：
outer()()
