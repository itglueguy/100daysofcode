# how to convert between json and pyton - found this online
import json
import yaml

sample = {
  "foo": "bar",
  "baz": [
    "qux",
    "quxx"
  ],
  "corge": None,
  "grault": 1,
  "garply": True,
  "waldo": "false",
  "fred": "undefined",
  "emptyArray": [],
  "emptyObject": {},
  "emptyString": ""
}

# dict to json
json_obj = json.dumps(sample)
print('json_obj =', json_obj)

ydump = yaml.dump(sample, default_flow_style=False)
print('ydump=',ydump)

#------------------------------------------------------------------------------------

# from the example above, we can try to convert this to yaml by using the yaml.dump() method

# open the file
data = open('cloudformation_template.json','r')

# load the json as a dict
json_data = json.load(data)
print('json_obj =', json_obj)

ydump = yaml.dump(json_data, default_flow_style=False)
print('ydump=',ydump)