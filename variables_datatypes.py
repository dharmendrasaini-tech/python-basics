# 🧠 LEVEL 1 — Type Recognition (Warm-up Brain Wiring)

# Goal: Instantly recognize types without thinking.

# Problems 1–15

# What is the type of 10

#int

# What is the type of 10.5

#float

# What is the type of "10"

#str

# What is the type of True

#bool

# What is the type of 3 + 4j

#complex  

# Store your name in a variable and print its type

name = "Dharmendra Saini"
print(type(name))

# Store your age and print its type

age = 32
print(type(age))

# Convert integer 25 into float

float_val = float(25)
print(float_val)


# Convert float 10.8 into int (observe output)

int_val = int(10.8)

print(int_val)


# Convert string "123" into integer

int_val = int("123")

print(int_val)

# Convert integer 456 into string

str_val = str(456)

print(str_val)

# Check type of result: 5 + 2.0

print(type(5+2.0))

# Check type of result: "5" + "2"

print(type("5" + "2"))

# Try: int("50") → note result

print(int("50"))

# Try: int("hello") → observe error

print(int("hello"))

# 🧠 LEVEL 2 — Variable Behavior (Memory Model Thinking)

# Goal: Understand variables are labels pointing to values.

# Problems 16–30

# Create variable a = 10, print it

a = 10

print(a)


# Change a to string "ten" and print type

a = "ten"

print(type(a))

# Create two variables with same value → check if types same

a = 10
b = 10

print(type(a))
print(type(b))


# Swap two numbers using third variable

a = 12
b = 14

c = a
a = b
b = c

print(a)
print(b)

# Swap two numbers without third variable

a = 10
b = 20

(a,b) = (b,a)

print(a)
print(b)



# Store sum of two numbers in third variable

a = 10
b = 20

total = a + b

print(total)

# Store multiplication of two numbers

a = 10
b = 20
multi = a * b

print(multi)

# Create variable and update value using +=

val = 10
val += 1

print(val)

# Create variable and update using *=

val = 10
val *= 1

# Check type after a = 5; a = a / 2

a = 5
a = a /2

print(type(a))



# Check type after a = 5; a = a // 2

a = 5
a = a //2

print(type(a))

# Store boolean result of 5 > 3

result = 5 > 3

print(result)

# Store boolean result of 5 == "5"

result = 5 == "5"

print(result)

# Store result of bool(0)

result = bool(0)

print(result)

# Store result of bool(100)

result = bool(100)
print(result)

# 🧠 LEVEL 3 — Implicit Type Conversion (Python Magic Zone)

# Goal: Predict when Python auto converts.

# Problems 31–45

# Predict type: 5 + 5.0

#float

# Predict type: True + 5

#int

# Predict output: "Age: " + str(25)

#str


# Try "Age: " + 25 → understand error

#str can concatenate with only str not int

# Predict output: float(5) + int(3.2)

#float

# Predict output: 5 * "Hi"

#HiHiHiHiHi

# Predict output: "Hi" * 3

#HiHiHi

# Try "Hi" * 3.5 → observe

 #it give error message - can't multiply sequence by non-int of type 'float'

# Predict type: 10 / 2

#float

# Predict type: 10 // 2

#int

# Predict type: 10 % 3

#int

# Predict type: 2 ** 3

#int

# Predict type: 2 ** 3.0

#float

# Store result of 5 + True

#result = 6

# Store result of False * 10

#result = 0

# 🧠 LEVEL 4 — Real Thinking (Mini Logic + Types)

# Goal: Apply types inside small logic.

# Problems 46–60

# Take input number → convert to int → print type

number = int(input("Enter a number:"))

print(type(number))


# Take input decimal → convert to float → print type


number = float(input("Enter a number: "))

print(type(number))

# Take input name → print length → print type

name = input("Enter your name: ")

print(len(name))

print(type(name))


# Take input number → multiply by 2 → print type

number = int(input("Enter a number: "))

print(type(number * 2))



# Store temperature float → convert to int → compare

temp1 = 13.54
temp2 = int(13.54)

print(temp1)
print(temp2)



# Check if variable is string using type()

a = "dharm"

print(type(a))

# Check if variable is int using type()

a = 45

print(type(a))



# Convert boolean True → int → print result

a = True

print(int(a))



# Convert boolean False → int → print result

b = False
print(int(b))

# Store "True" → convert to bool → observe

a = "True"

b = bool("True")

print(b)
#It give output True even when there is something else written then True because it only checks whether there is a string value present.




print(type(b))




# Compare bool("False") vs False

a = bool("False")
#it give output True because there is a string value


b = False

print(a)
print(b)


# Create variable → print value + type in same line

a = 34

print(a,type(a))

# Store result of int(True) + float(False)

a = int(True) + float(False)

print(a)



# Take input → convert to int → add 10 → print type

a = int(input("Enter a number: "))

a = a + 10

print(type(a))



# Create 3 variables of different types → print all types

a = 45
b = "python"
c = 12.85

print(type(a))
print(type(b))
print(type(c))




