#  inheritance 
class BaseClassName:
    pass


class DerivedClassName(BaseClassName):
    # <statement-1>
    # if want to call the baseclass method
    # directly call BaseClassName.methodname(self, arguments)
    pass

# when a class is defined in another module
"""class DerivedClassName(modName.BaseClassName):
    pass"""


# Multiple inheritance
"""class DerivedClassName(Base1, Base2, Base3):
    pass"""

# Private Variables
# 
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    
    __update = update    # private copy of original update() method

class MappingSubClass(Mapping):
    def update(self, keys, values):
        # provide new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

if __name__ == "__main__":
    c = MappingSubClass('c')
    x = Mapping('x')
    print(x.items_list)
    w = Mapping
    v = MappingSubClass
    x.update('ii')
    c.update('key', 'value')
    print(x.items_list)
    print(c.items_list)