# accessing the internet and processing internet protocols
# urllib.request for retriveving data from 'URLs' and 'smtplib'
# for sending mail
'''
from urllib.request import urlopen
with urlopen('https://translate.google.com/') as response:
    counter = 0
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)
            counter += 1
        else:
            counter += 1
    print(counter)       


# send email
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('From@example.org', 'To@example.org',
"""To: To@example.org
From: From@example.org

Beware the Ides of March
""")
server.quit()
'''

# dates and times
from datetime import date
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# dates support calendar arithmetic
birthday = date(1997, 5, 9)
age = now - birthday
print(age.days/365)

# Data compression
import zlib
s = b'witch which has which witches wrist watch'
print('before compression', len(s))
t = zlib.compress(s)
print('after compression', len(t))
s1 = zlib.decompress(t)
print(s1)
print(zlib.crc32(s))
# print(zlib.__doc__)

# performance measurement
from timeit import Timer
time = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print('processing time: ', time)
print('??: ', Timer('a,b=b,a','a=1; b=2').timeit())