# module to work with json data
import json

# some JSON: ( the datastructure seems similar to a dictionary - just loaded differently)
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["city"])

#---------------------------------------------------------------------------------------------

# The example converts from a dictionary to a JSON string:

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#--------------------------------------------------------------------------------------------- 

# lets make some functions to convert it to get in some practice
def jsontodict(dict):
    r = json.loads(y)
    return r

def dicttojson(dict):
    r = json.dumps(x)
    return r

#-------------------------------------------

jsontodict (y)

dicttojson (x)