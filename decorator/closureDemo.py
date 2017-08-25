
"""闭包演示"""

# 现有如下函数
def outer():
    x = 10
    def inner():
        print(x)

    return inner

#问：如何执行内部的inner函数

outer()()
