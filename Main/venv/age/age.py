import os
os.system('clear')

age = int(input("How old are you?: "))


# if age is greater than or equal to 18 print "adult"
if age >= 18:
  print("You're "+str(age)+"yrs old (adult)")


# else if age is ranged from 13 to 17 print "underage"
elif age <= 17:
  print("You're "+str(age)+"yrs old (underage)")


else:
  print()


