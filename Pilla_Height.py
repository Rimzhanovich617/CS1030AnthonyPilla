## Introduction lines 2-10
print("Hello! What is your name?")

val = input("Enter your name: ")
string = val
if not string:
    print("Sorry! That's not right!")
    quit()
print("Hello!")
print(val)

## Height Conversion 12-40
print("Let's get your height. What the feet?")

val = input("Enter the feet:  ")
string = val
if not string:
    print("Sorry! That's not right!")
    quit()
def multiply(x, y):
    return x*y
x= int(val)
y= 12
c= x*y
print ("Your height in inches is:", multiply(x,y))
if(c>96):
    print("Wow! You're Really Tall!")
print("Now let's convert inches to centimeters")
def multiply(c, d):
    return c*d
c= x*y
d=2.54
print("Your height in centimeters is", "{0:.2f}".format(c*d))
print("Now let's get your height in meters!")
def divide(e, f):
    return e/f
e=c*d
f=100
"{0:.2f}".format(e/f)
print("Your height in meters is", "{0:.2f}".format(e/f))

##Outro 43-44
print("Have a Great Day!")
quit()






