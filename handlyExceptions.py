while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except (ValueError, NameError, TypeError): # also can name multiple exception
        print("Oops! That was no valid number.  Try again...")


class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print('D')
    except C:
        print('C')
    except B:
        print('B')

import sys

"""
try :
    f = open('testFile.txt')
    s = f.readline()
    i = int(s.strip)
except OSError as err:
    print("OS error: {}.".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error: ", sys.exc_info()[0])
    raise
"""


"""
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
"""

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly
                         # but may be overridden in exception subclasses

    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)

try:
    raise Exception(int(input("Enter number: ")))
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly
                         # but may be overridden in exception subclasses

    x = inst.args     # unpack args
    print('x =', x)

    
# def fun(name, *books, **dictionary):
#     print('You name is: ', name)
#     print("The book you have borrowd are:")
#     for book in books:
#         print(book)
#     for dirs in dictionary:
#         print(dirs, ': ', dictionary[dirs])

# fun('Li Lei', 'Jian', 'ChangJian', 'DaJian',shell0='Sinence',
# shell1='Math',shell2='Art')

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

# raise statement allows the programmer to
# force a specified exception to occur
# raise NameError('Hithere')


# If you need to determine whether an exception was raised 
# but don’t intend to handle it,
# a simpler form of the raise statement allows you to re-raise the exception
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    

# defining clean-up actions
# try statement has another optional clause
# which must be executed under all circumstances
print('next')
try:
    raise Exception(TypeError)
finally:
    print("Goodby, night!")