# methods to process csv files doesn't seem to satisfy my simplicity compared
# to using the import-csv command in powershell. Let me try the pandas method
# it will require that i install the pandas module by running the
# pip install pandas command

# much better
import pandas
dataframe = pandas.read_csv('sample.csv')

# this seems to print the dataframe
print(dataframe)

# print items related to the key 'Name' column
dataframe['name']

# get the value in the 2nd row of the age column
dataframe['age'][1]

# not what i expected - but it seems to give the command some structure
# im sure its not meant to be run multiple time, but it does not seemt to be immutable
dataframe = dataframe.reset_index()  # make sure indexes pair with number of rows
for index, row in dataframe.iterrows():
    print(row['name'], row['age'])

# this make a little more sense to ee - i can see how it relates to using the index accordingly
for i in range(0, len(dataframe)):
    name = dataframe.iloc[i]['name']
    age =  dataframe.iloc[i]['age']
    hobby =  dataframe.iloc[i]['hobby']
    print("Name: " + name + "| Age: " + str(age) + "| Hobby: " + hobby)

for i in range(0, len(dataframe)):
    print(dataframe.iloc[i]['name'], dataframe.iloc[i]['age'], dataframe.iloc[i]['hobby'])


# --------------------------------------------------------------------------------------------

# Writing values to a csv file

# Cribbed this online - it seems to establish a procedure to write the header and than the row information
import csv

# use a list as the header
header = ['name', 'area', 'country_code2', 'country_code3']

data = [
    ['Angola', 1246700, 'AO', 'AGO']
]

# use a nested list for the row
data = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)


# Writing a function makes life so much easier - thanks github copilot :)
def writetocsv (file_path,header, data):
    with open(file_path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)   

# A function is easer - but it can be easier to write a function to read a csv file
writetocsv ('countries.csv', header, data) 

# write to the c:\temp folder? - nope that didnt work
writetocsv ('c:\temp\countries.csv', header, data) 

# write to the c:\temp folder using double slaeshes - that worked
writetocsv ('c:\\temp\\countries.csv', header, data) 

# Lets try forward slashes - heard it worked in Docker Syntax
writetocsv ('c:/temp/countries.csv', header, data) 

# --------------------------------------------------------------------------------------------

### thats enough practice for now - JSON and XML practice for tommorrow