class MyClass:
    """A simple example class"""
    i = 123456    # class variable shared by all instance

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

    def f(self):
        return 'Hello World'

class MyClasss:
    def __init__(self):
        self.data = []    

class Complex:
    def __init__(self, realpart, imgpart):
        self.realpart = realpart
        self.imgpart = imgpart

class Dog:
    # do not use class variable shared by all instance 
    # if you want unique list for each dog
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)



if __name__ == "__main__":
    x = MyClass('name')
    x.i = 13579
    print(MyClass.f(x)) # x.f() = MyClass.f(x)
    print(x.i)
    print(type(x.f))
    print(type(x.f()))
    y = MyClass('age')
    print(y.i)
    z = MyClasss()
    z.data.append('l')
    print(z.data)
    a = Complex('realpart', 'imgpart')
    print(a.realpart, a.imgpart)
    y.counter = 1
    while y.counter < 10:
        y.counter = y.counter * 2
    print(y.counter)
    del y.counter
