## Introduction lines 2-10
print("Hello! What is your name?")

val = input("Enter your name: ")
string = val
if not string:
    print("Sorry! That's not right!")
    quit()
print("Hello!")
print(val)

## Height Conversion 12-38
print("Let's get your height in feet and inches. What are the feet?")
feet = int(input("Enter your feet\n"))
string = feet
if not string:
    print("Sorry! That's not right!")
    quit()

print("Your feet in inches are", feet*12)

inches = int(input("Enter your inches\n"))
string = inches
if not string:
    print("Sorry! That's not right!")

print(feet*12+inches)
if (feet*12+inches>96):
    print("Wow! You're tall!")
w= (feet*12+inches)
print("Now let's convert inches to centimeters")
print("Your height in centimeters is","{0:.2f}".format(w*2.54))
z= (w*2.54)
print("Now let's get your height in meters!")
def divide(e, f):
    return e/f
e= z
f=100
"{0:.2f}".format(e/f)
print("Your height in meters is", "{0:.2f}".format(e/f))
print("Your height in imperial is")
print(feet, "feet and", inches, "inches")

##Outro 40-42
print("Have a Great Day!")
quit()






