#
# Simple Find the Attachment Name given input from a mime File
# Modification of this code: https://www.w3schools.com/python/python_lists_loop.asp

# Define the Variables
# find common data interchange Extensions
Extensions = [".csv", ".txt", ".xlsx"]
file_name = 'F:/python/5eopts4ig1e3ilh6eci9u8a5a6o0to7147j78ig1'

attachment_name = 0
attachments_found = 0
attachment_names = []

# opening a text file
with open(file_name, "r") as file1:
    for Extension in Extensions:
        # setting flag and index to 0
        flag = 0
        index = 0


        # Loop through the file line by line
        for line in file1:
            index += 1

            # checking string is present in line or not
            if Extension in line:
                flag = 1
                attachments_found += 1
                attachment_name = (line.split("=")[1]).replace('"','')
                attachment_names.append(attachment_name)
                break
if attachment_name == 0:
    print("No Attachments Found")
else:
    print("Attachments found:", attachments_found)
    print(attachment_names)