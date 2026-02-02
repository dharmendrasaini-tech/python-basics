#Q1 Write a program to input user's first name and print its length.

name = input("First Name: ")

print(len(name))

#Q2 Write a program to find the occurence of '$' in a String.

str = input("Write a string: ")

print(str.count("$"))

#Q3 Grade students based on marks
# marks >= 90 , grade = "A"
# 90 > marks >= 80 , grade = "B" 
# 80 > marks >= 70 , grade = "C"
# 70 > marks , grade = "D"

marks = int(input("Enter your marks: "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("The grade of the student is: ", grade)

#Q4 Check if a number entered by the user is odd or even.

num = int(input("Enter a number: "))

if(num % 2 == 0):
    print("Even")
else:
    print("Odd")


#Q5 Find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if(num1 >= num2 and num1 >= num3):
    greatest = num1
elif(num2 >= num1 and num2 >= num3):
    greatest = num2
else:
    greatest = num3

print("Greatest number is : ", greatest)

#Q5 Find the greatest of 4 numbers entered by the user.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
num4 = int(input("Enter num4: "))

if(num1 >= num2 and num1 >= num3 and num1 >= num4):
    greatest = num1

elif(num2 >= num1 and num2 >= num3 and num2 >= num4):
    greatest = num2
elif(num3 >= num1 and num3 >= num2 and num3 >= num4):
    greatest = num3
else:
    greatest = num4


print("The greatest number is: ", greatest)


#Q5 Check if a number is a multiplier of 7 or not

num = int(input("Enter a number: "))

if(num % 7 == 0):
    print("Yes")
else:
    print("No")

#Q6 Take a string input and print its length

str1 = input("Enter a string: ")

print(len(str))

#Q7 2. Take a string and print its first and last character.

str1 = input("Enter a string: ")

if(len(str1) == 0):
    print("Empty string")

else:
    print("First character: ", str1[0], "Last character: ", str1[len(str1)-1])


#Q8 Take a string and check whether it is empty or not.

str1 = input("Enter a string: ")

if(len(str1) == 0):
    print("Empty string")
else:
    print("Not empty")


#Q9 Take a string and print:  * "Yes" if its length is greater than 10  * "No" otherwise


str1 = input("Enter a string: ")

if(len(str1) > 10):
    print("Yes")
else:
    print("No")

#Q10  Take a number and check whether it is positive, negative, or zero.

num = int(input("Enter a number: "))

if(num < 0):
    print("Negative")
elif(num == 0):
    print("Zero")
else:
    print("Positive")


#Q11 Take a string and check whether it contains the letter 'a'.

str1 = input("Enter a string")

findA = (str1.find('a'))

if(findA == -1):
    print("No")
else:
    print("Yes")


#Q12 Take a string and check whether it is all lowercase.

str1 = input("Enter a string: ")

if(str1.islower()):
    print("Yes")
else:
    print("No")

#Q12 Take a string and check whether it starts with a vowel.

str1 = input("Enter a string: ")

if(str1.startswith(('a','e','i','o','u'))):
    print("Yes")
else:
    print("No") 
#Q13 Take a number and check whether it is divisible by 3 or 7.

num = int(input("Enter a number: "))

if(num % 3 == 0 or num % 7 == 0):
    print("Yes")
else:
    print("No")

#Q14 Take a string and check whether its length is even or odd.

str1 = input("Enter a string: ")

if(len(str1) % 2 == 0 ):
    print("Even")
else:
    print("Odd")

#Q15 1. Take a string and:
# Print "Short" if length < 5
# Print "Medium" if length is between 5 and 10
# Print "Long" if length > 10


str1 = input("Enter a string: ")

length = len(str1)

if(length < 5):
    print("Short")
elif(length >= 5 and length <= 10):
    print("Medium")
else:
    print("Long")

#Q16 Take a string and check whether the first and last characters are the same.

str1 = input("Enter a string: ")

if(len(str1) == 0):
    print("Empty string")

elif(str1[0] == str1[len(str1)-1]):
    print("Yes")
else:
    print("No")


#Q17 2. Take a string and count how many times 'a' appears.
# Print "Many" if count > 3
# Else print "Few"

str1 = input("Enter a string: ")

countA = str1.count('a')

if(countA > 3):
    print("Many")
else:
    print("Few")

#Q18 Take a string and check whether it is a valid identifier (letters, digits, underscore, not starting with digit).


str1 = input("Enter a string")

if(str1.isidentifier()):
    print("Yes")
else:
    print("No")

#Q19 Take a string and check whether it is a palindrome (same forward and backward).

str1 = input("Enter a string: ")

if(str1 == str1[::-1]):
    print("Yes")
else:
    print("No")







   
   




















