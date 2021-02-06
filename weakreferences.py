import weakref, gc

class A:
    def __init__(self, value):
        self.value = value 
    def __repr__(self):
        return str(self.value)

a = A(10)    # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a    # does not create a reference
print(d['primary'])    # fetch the object if it is still alive
                       # and it will be removed automatically

del a
gc.collect()
try:
    d['primary']
except KeyError as err:
    print('KeyError:', err)

