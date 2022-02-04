# a list is a collection of ordered elements.
my_list = ["foo", "bar", "blu"]
# print(some_list)
# we can check elements by their number
# here is a good time to introduce the fact that programers count from 0 so the first element will be the element 0
# the second element will be the element 1 and so on
print(my_list[0])
print(my_list[1])
print(my_list[2])

# since our list has only three elements three elements there will be nothing after the index 2
# python wll throw an raise an error if we try to access another element

# uncomment this line to see the error
# print(my_list[42])

# a dict (dictionary) is a collection of named elements
some_dict = {
    "name": "antoine",
    "family_name": "Redier"
}
# print(some_dict)
# we can get an element by it's key instead of it's order of insertion
print(some_dict["name"])

# we can off course combine those elements in order to have a list of dictionaries
# or a list as a value in a dictionary
# or a dict as the key in another dictionary.
# here your imagination is the limit. However I would advise using simple types (ints and strings) as key in
# dictionaries as it can quickly get messy.


# for instance in this example we will have a list of dictionaries, each dictionary represent a slack nessage with
# user name, a message and an attached file

slack_posts = [
    {"user_name": "aredier", "message": "some picture of my cat", "file": "./cat.jpg"},
    {"user_name": "abesson", "message": "some picture of my plant", "file": "./bonsai.png"}
]


# if we want to get the name of the second message sender we do the `[]` in order:
print(slack_posts[1]["name"])
