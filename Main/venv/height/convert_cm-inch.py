#take input from user
cm=int(input("Enter the height in centimeters:"))

#convert centimeter to inches
""" 1 inch = 2.54 centimeters"""
inches = cm/2.54 

#print result
print("The height in inches",round(inches,0))