
class Person(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setBreast(self, n):
        self.breast = n

    def color(self, color):
        print('%s is %s' % (self.name, color))

    def how(self):
        print('%s breast is %s' % (self.name, self.breast))

girl = Person('lily')
girl.setBreast(50)
girl.color('white')
girl.how()