# Get a name for the file from user
# Link external file: LotsOfNumbers.txt
# Open and Read file
print("Hello! I have a file, but I want you to name it. What would you want to name it?")
file_name = input()
"LotsOfNumbers.txt" == file_name

# Count all the integers in the file

print("Let's find out how many integers are in this file")
file = open("LotsOfNumbers.txt", "r")
data = file.read()
number_of_integers =len(data)
print("The total count of integers is: ", number_of_integers)

# Find the sum of all the integers in the file: LotsOfNumbers.txt

print("Let's find out the total sum of these numbers")
file = open("LotsOfNumbers.txt", "r")
content_of_file = file.readlines()
sum_of_numbers = 0
for line in content_of_file:
    for i in line:
        if i.isdigit() == True:
            sum_of_numbers += int(i)
print("The sum of all numbers is:", sum_of_numbers)
total = sum_of_numbers

# Find the average of all the integers in the file: LotsOfNumbers.txt

print("Let's find out the average of all of these numbers")
average = sum_of_numbers/number_of_integers
print("The average of all numbers is: ", average)

# Find the average of all the integers in the file: LotsOfNumbers.txt
# Send output of total integers, sum of all integers, and  average to external file: Program2.out
new_file = open("Python2.out", "w+")
new_file = open("Python2.out", "a+")
with open('Python2.out', "a+") as f:
    a = number_of_integers
    b = sum_of_numbers
    c = average
    f.write('{}\n'.format( ','.join(map(str, (a, "\n", b, "\n", c, "\n"))) ))
f.close()

