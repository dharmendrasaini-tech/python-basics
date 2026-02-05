


# Take two numbers and print their sum, difference, product, division.

num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))

print("Sum: ",num1 + num2)
print("Difference: ",num1 - num2)
print("Product: ", num1 * num2)
print("Division: ",num1/num2)

# Swap two numbers without using a third variable.

a = 10
b = 20

print(a,b)

a,b = b,a

print(a,b)






#(a,b) = (b,a)


print(a,b)



# Take temperature in Celsius and convert to Fahrenheit.

celsius = float(input("Enter temperature in celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(fahrenheit)

# Input a number and print its type before and after conversion to float.

num1 = input("enter a number: ")

print(type(num1))

print(type(float(num1)))



# Take name and age, print:
# "Hello Rahul, you will be 60 years old in 38 years"

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name,", you will be 60 years old in ", 60-age, "years")



# Check if a number is positive, negative, or zero.

num = int(input("enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("zero")

# Check if a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Find the largest of three numbers.

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num3 and num2 >= num1:
    largest = num2
else:
    largest = num3

    
print(largest)

# Check whether a year is a leap year.

year = int(input("Enter the year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 != 0 and year % 4 == 0:
    print("Leap year")
else:
    print("Normal year")



# Check if a character is a vowel or consonant.

ch = input("Enter a character: ")

if ch in "aeiou":
    print("vowels")
else:
    print("consonant")
    
    
# Take marks and print grade (A/B/C/Fail).

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 80:
        print("Grade A")
elif marks >= 60:
        print("Grade B")
elif marks >= 40:
        print("Grade C")
else:
        print("Fail")


# Check whether a number is prime.

num = int(input("enter a number: "))

if num <= 1:
     print("Not prime")
else:
     
     i = 2
     is_prime = True

     while i <= num // 2:
          if num % i == 0:
               is_prime = False
               break
          i+=1

     if is_prime:
          print("Prime")
     else:
          print("Not prime")
          
         




    # Count vowels in a string.

strr = input("Enter a string")

strr_lower = strr.lower()

count = 0

for i in strr_lower:
    if i in 'aeiou':
        count+=1

print(count)

     

# Reverse a string.

name  = input("Enter a string: ")

reversed_name = ""

for i in name:
     reversed_name = i + reversed_name 


print(reversed_name)
 

# Check if a string is a palindrome.

name = input("enter your name: ")

lower_name = name.lower()



reversed_name = ""


for i in lower_name:
     reversed_name = i + reversed_name

if lower_name == reversed_name:
     print("palidrome")
else:
     print("not palindrome")
 
     

# Count words in a sentence.

sentence = input("enter a sentence")

count = 0

in_word = False

for i in sentence:
     if i != " " and in_word == False:
          count+=1
          in_word = True
     else:
          if i == " ":
               in_word = False
          
      
print(count)

# Convert "hello world" → "Hello World".

sentence = "hello world"

new_sentence = ""

in_word = False

for i in sentence:
     if not i.isspace() and in_word == False:
          new_sentence = new_sentence + i.upper()
          in_word = True

     elif i.isspace():
          new_sentence = new_sentence + i
          in_word = False
     else:
          new_sentence = new_sentence + i
  
print(new_sentence)

        
     


     







          
          











# Remove duplicate characters from a string.

# 🔸 D. Lists & Tuples (8 problems)

# Find sum of elements in a list.

# Find max and min in a list (without using max()).

# Remove duplicates from a list.

# Count how many even numbers are in a list.

# Reverse a list.

# Find the second largest number.

# Merge two lists.

# Convert list to tuple and explain why tuple is safer.

# 🔸 E. Sets (6 problems)

# Find unique elements from a list.

# Find common elements between two lists.

# Find subjects chosen by only one student.

# Check if two sets are disjoint.

# Count number of unique words in a sentence.

# Classroom problem (unique subjects → classrooms).

# 🔸 F. Dictionaries (7 problems)

# Create a dictionary of student marks and print average.

# Count frequency of elements in a list using a dictionary.

# Find key with maximum value.

# Merge two dictionaries.

# Check if a key exists.

# Convert two lists into a dictionary.

# Student record system (name, age, marks).

# 🔸 G. Loops (10 problems)

# Print numbers from 1 to 100.

# Print even numbers between 1 and 100.

# Count digits in a number.

# Reverse a number.

# Sum of digits of a number.

# Fibonacci series up to n.

# Factorial of a number.

# Multiplication table.

# Count number of primes between 1 and n.

# Pattern printing (simple * triangle).

# 🔥 PHASE 2 — MIXED (REAL CONFIDENCE BUILDERS)

# After finishing at least 70% of above:

# Student management system (list + dict).

# Find duplicate elements and their counts.

# Password strength checker.

# Word frequency counter.

# Menu-driven program using while.

# Find common subjects of multiple students.

# Remove vowels from a sentence.

# Find longest word in a sentence.

# Bank account simulation (deposit/withdraw).

# Mini quiz program.

# These don’t tell you which topic to use — like real life.