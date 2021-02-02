import reprlib
# abbreviated dispalys of large or deeply nested containers
print(reprlib.repr(set('supercalifragilisticesxpoalodocing')))

import pprint
# When the result is longer than one line, the “pretty printer” 
# addsline breaks and indentation to more clearly reveal data structure
t = [[[['black','cyan'],'white', ['green','red']], 
                    [['magenta','yellow'],'blue']]]

pprint.pprint(t, width=30)

import textwrap
# formats paragraphs of text to fit a given screen width
doc = """The wrap() method is just like fill() except that it 
returns...a list of strings instead of one big string with newlines to 
separate...the wrapped lines."""

print(textwrap.fill(doc, width=45))

import locale
# data formating
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
conv = locale.localeconv()  # get a mapping of conventions
x = 1234567.8
print(locale.format_string("%d", x, grouping=True))  # locale.format will be remove in future python
print(locale.format_string("%s%.*f", (conv['currency_symbol'],
                        conv['frac_digits'], x),grouping=True))

from string import Template
# $ is placeholder, $$ creates a single escaped $
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='NorthGrad', cause='the ditch fund'))

t = Template('Return the $item to $owner')
d = dict(item='book')
try:
    t.substitute(d)  # error
# for safe return
except KeyError as err:
    print('KeyError: ', err)
    print('Process safe substitute')
    print(t.safe_substitute(d))

import time, os.path
photofiles = ['img_01.jpg', 'img_02.jpg', 'img_03.jpg']
class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style ( %d-data %n-seqnum %f-format):  ')
t = BatchRename(fmt)
date = time.strftime('%d%by')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{} --> {}'.format(filename, newname))

# Working with binary data record layout
# "H", and "I" represent two and four byte unsigned numbers respectively
# "<" indicated that they are standard size and in little-endian byte order
import struct

with open('Learn_.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):  # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size  # skip to the next header