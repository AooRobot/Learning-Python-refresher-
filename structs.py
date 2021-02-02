# python struct

class Employee:
    pass

john = Employee()
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1800



# iterator in class
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]



# newbie
def reverse(data):
    index = len(data)
    re_data = []
    for i in range(index):
        if index == 0:
            raise StopIteration
        index = index - 1
        re_data.insert(i, data[index])
    return re_data




# Generators 
# a simple and powerful tool for creating iterators
# use "yield" statement whenever want to return data

def reverse_re(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]





if __name__ == "__main__":
    print('This is main fucntion')
    # iterators
    s = 'abc'
    for i in s:
        print(i)

    it = iter(s)
    print(next(it))
    print(next(it))
    print(next(it))

    rev = Reverse([1,2,3])

    container = iter(rev)
    print(container)

    for char in rev:
        # for statement call rev.__iter__ then call __next__
        print(char)
    
    print(reverse("spam"))
    print(reverse('123'))

    for char in reverse_re("golf"):
        print(char)

    # Generator expressions
    print_sum = sum(i*i for i in range(10))  # sum of squares
    print(print_sum)
    
    xvec = [10, 20, 30]
    yvec = [7, 5, 3]
    vec_sum = sum(x*y for x,y in zip(xvec, yvec))  # dot product
    print(vec_sum)
    
    from math import pi, sin
    sine_table = {x : sin(x*pi/180) for x in range(0, 91)}

    # unique_words = set(word for line in page for word in line.split())

    # valedictorian = max((student.gpa, student.name) for sutdent in graduates)

    data = 'golf'
    l = list(data[i] for i in range(len(data)-1, -1, -1))
    print(l)
    pass
