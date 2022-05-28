import os

def hello():

  os.system('clear')

  print("Enter Your Name:")

  first_name = input("First : ") #user input
  # if first_name.isalpha(): #if string contains all letters
  #   print(first_name + "\n")
  # else:
  #   print("input need to be alphabetical\n")


  last_name = input("Last  : ") #user input
  # if last_name.isalpha(): #if string contains all letters
  #   print(last_name + "\n")
  # else:
  #   print("input need to be alphabetical\n")


  name = first_name + " " + last_name #concatinated strings
  name_length = " (" + str(len(name)-1) + "letters)" #count number of characters
  hello_name = "Hello "+name.title() #print name case title
  # print(hello_name + name_length)


  print("\nEnter Your Age:")
  age = int(input("Age   : "))
  # if age >= 18: #if age is greater than or equal to 18 print "adult"
  #   print("You're "+str(age)+"yrs old (adult)")
  # elif age <= 17: #else if age is ranged from 13 to 17 print "underage"
  #   print("You're "+str(age)+"yrs old (underage)")
  # else:
  #   print("You're "+str(age)+"yrs old")


  # =====
  print("\nEnter Your Height:")
  h_ft = int(input("Feet: "))
  h_inch = int(input("Inches: "))
  h_inch += h_ft * 12
  h_cm = round(h_inch * 2.54, 1)
  # =====

  os.system('clear')
  print(hello_name + name_length)
  print("Your "+str(age)+"yrs old")

  print("Your height is : %d cm." % h_ft)
  print("Your height is : %d cm." % h_inch)
  # print("Your height is : %d cm." % h_cm)

hello()