# saving structured data with json
import json
js = json.dumps([1, 'simple', 'list'])
print(js)

# dump() serializes the object to a text file, 
# if f is a text file object opened for writing, 
# json.dump(x, f)
f = open('filecreatedbyPy','a')
jss = json.dump(js, f)

# if a text file has been opened for reading, 
# decode
de_object = json.load(f)