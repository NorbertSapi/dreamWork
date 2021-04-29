# This is a sample Python script to work on how to open a file.

from pathlib import Path

'''
****************************************************
First Task: OPEN, READ, ASSIGN
    Step 1: open text file
    Step 2: assign the data to list.
    Step 3: decode the given list
    Step 4: assign the decoded list to a new_list
#***************************************************
'''
# assign data to "text"
dataFolder = Path(r'C:\Users\ncssa\PycharmProjects\dreamWork\sample-1.txt')
text = dataFolder.read_text()
# split string to a list
list1 = text.rsplit(" ")
print("list to decode: ", list1)


# this is the decoder function
def decoder(work):
    number = 0              # int variable to store converted numbers - temporary
    list2 = []              # This is a new list to hold the decoded numbers
    for item in work:
        number += int(item)
        list2.append(number)
    return list2


# call the decoder function
decoded_list1 = decoder(list1)
print("decoded list: ", decoded_list1)

'''
****************************************************
Second Task: CONVERT, CREATE NEW TEXT FILE
    Step 1: convert list to String
    Step 2: create new Text File
    Step 3: save the string to the new Text File
#***************************************************
'''

f = open("final-1.txt", "a+")  # create/open a new txt file for the final result
# write the decoded_list_1 in the text file.
for i in decoded_list1:
    f.write("%s " % i)
f.close()

'''
****************************************************
Third Task: TEST the script
    Step 1: write unittest
    Step 2: run unittest
****************************************************
'''
