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
dataFolder = Path(r'C:\Users\ncssa\PycharmProjects\open_data_from_text\data_store.txt')
text = dataFolder.read_text()

# split string to a list
list1 = text.rsplit(" ")
print(list1)


# this is the decoder function
def decoder(work):
    number = 0              # int variable to store converted numbers - temporary
    list2 = []              # This is a new list to hold the decoded numbers
    for item in work:
        number += int(item)
        list2.append(number)
    return list2


# call the decoder function
print("test: ", decoder(list1))
