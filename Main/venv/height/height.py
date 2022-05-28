
def heights():
    conversion = .0254
    group = int(input('How many people are in your group? '))

    for people in range(1, group+1):
        print('\n''Person Number', people)
        feet = range(10)
        inches = range(12)
        a = int(input('Enter your height in feet inches, separated by a comma: '))
        meters = a*conversion
        print("Your height in feet and inches: ", a,"'",'"')
        print("Your height in meters is: ", meters)

    print('\n' "The average height of your group in feet and inches is: ", a/group)
    print("The average height of your group in meters is: ", a/meters)

heights()