# in the list and dict lesson we have learned to create lists and dictionaries.
# however we might want to be able to perform some action on each element of a list or keu, value pair of a dictionary.
# this is where loops come into play.
# to do something for each eleemnt of the list we use the `for` statement

student_list = ["Adelie", "Hamza", "Noemie"]
for student_name in student_list:
    print("welcome " + student_name)

# you can see we used `:` at the end of the for statement. In python `:` generally means then and the next
# line will be indented (moved four spaces or one tab to the right).

# so the block of code above reads
# for each student_name in the student_list print welcome and then the student_name


# in the same way we can do a for loop on a dictionary, this will give
# all the KEYS (and not the values) of the dictionary:

beatle_ages = {
    "Paul": 42,
    "John": 53,
    "Ringo": 18,
    "George": 23
}

for beatle_name in beatle_ages:
    print(beatle_name + " is " + beatle_ages[beatle_name] + " years old.")

# this block of code can be read as:
# for each key in the beatle_ages dictionary, put the key in a temporary beatle_name variable and print the message.


# EXERCISE
# create a list of dictionaries where each dictionary represents a slack message has the foloowing information
# - the name of the sender
# - the message itself
# - several attachments (it can be 0, 1, 2 or more

# then for each of those message print the name of the sender, the message itself, the number of attchment and
# for each atachment in the message print the name of the sender followed by " has attached " and the file of the attachment.
