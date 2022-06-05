import json

# Create the list
employee_list = ['John','Anna','Peter']

# create empty dict curley brackets
dict = {}

# equate the list to the key value
dict['employees'] = employee_list

# print it out ( still a dictionary)
dict

# output from dict to json string by using the .dumps() method
json_string = json.dumps(dict)

# print it out as a string
print(json_string)

#----------------------------------------------------------------------------------------------------------------------

import json
# initiate the list
employee_list = []

employee_dict = {}
employee_dict['name'] = 'John'
employee_dict['salary'] = '65'
employee_dict['title'] = 'Cheo'

employee_list.append(employee_dict)

employee_dict = {}
employee_dict['name'] = 'Anna'
employee_dict['salary'] = '85'
employee_dict['title'] = 'Choo'

employee_list.append(employee_dict)

employee_dict = {}
employee_dict['name'] = 'Peter'
employee_dict['salary'] = '45'
employee_dict['title'] = 'ChMo'

employee_list.append(employee_dict)

# employee list now has attributes
employee_list

# create empty dict
employee_list_dict = {}

# equate the list to the key value
employee_list_dict['employees'] = employee_list

# convert the dict to a json string
json_string = json.dumps(employee_list_dict)

# print out the json string
print(json_string)
# the structure is:     overalldict{dict_key=list[dict{}]}

# github copilot is a really good tool for students and i would recommend it to anyone who is looking to learn python - hahah recommendations
employee_list_dict['Author'] = 'Toni Nguyen'

# convert the dict to a json string
json_string = json.dumps(employee_list_dict)

# print out the json string
print(json_string)


#-----------------------------------------------------------------------------------------------------------------------
# convert from json to dictionary
json_dict = json.loads(json_string)

# Access the key values related to employees
json_dict['employees']

# see what attributes are available
dir(json_dict['employees'])

#--------------

# use a sample format to help me get to my final format

import csv

# prepopulates the header beforehand  
employee_info = ['emp_id', 'emp_name', 'skills']
  
new_dict = [
{'emp_id': 456, 'emp_name': 'George', 'skills': 'Python'},
{'emp_id': 892, 'emp_name': 'Adam', 'skills': 'Java'},
{'emp_id': 178, 'emp_name': 'Gilchrist', 'skills': 'Mongo db'},
{'emp_id': 155, 'emp_name': 'Elon', 'skills': 'Sql'},
{'emp_id': 299, 'emp_name': 'Mask', 'skills': 'Ruby'},
]

# you need to create the c:\temp folder and file test.csv befoer hand  
with open('c:\\temp\\test.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = employee_info)
    writer.writeheader()
    writer.writerows(new_dict)



