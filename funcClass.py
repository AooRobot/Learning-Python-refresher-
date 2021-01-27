# assigning a function object to a local variable 
# in the class is also ok

def f1(self, x, y):
    return min(x, x + y)

class C:
    f = f1

    def g(self):
        return 'Hello world'
    
    h = g
# x = C
x = C()

# print(C.f(x, 2, 4))
print(x.f(2, 4))

# print(x.h(x))
print(x.h())
