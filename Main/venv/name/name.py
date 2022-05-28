

first_name = input("What is your first name?: ") #user input
# print(first_name.isalpha()) #if string contains all letters

last_name = input("What is your last name?: ") #user input
# print(last_name.isalpha()) #if string contains all letters

name = first_name + " " + last_name #concatinated strings

name_length = " (" + str(len(name)-1) + "letters)" #count number of characters

hello_name = "Hello "+name.title() #print name case title

print(hello_name + name_length)
