# ✅ CONFIDENCE-BUILDER PROBLEM SET
# (Topic-wise • Easy → Medium • Within Scope)
# How to use this
# * One topic at a time
# * Finish easy + medium before moving on
# * For EVERY problem:
#     * write plain-English logic on paper
#     * then code

# 🟦 TOPIC 1: CONDITIONS
# Easy
# 1. Check if a number is positive or negative

number = int(input("Enter a number: "))

if number < 0:
    result = "Negative"
elif number == 0:
    result = "Zero"
else:
    result = "Positive"

print(result)
 

# 2. Check if a number is even or odd

number = int(input("enter a number: "))

if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"

print(result)


# 3. Find the larger of two numbers

number1 = int(input("Enter a number: "))

number2 = int(input("Enter second number: "))

is_equal = number1 == number2

if is_equal:
    output = "Both are equal."

else:
    larger = number1
    if number2 > larger:
        larger = number2

    output = larger


print(output)


# Medium
# 1. Find the largest of three numbers

number1 = int(input("Enter the first number"))
number2 = int(input("Enter the second number"))
number3 = int(input("Enter the third number"))

is_equal = number1 == number2 == number3

if is_equal:
    output = "All are equal."
else:
        largest = number1


        if number2 > largest:
            largest = number2
        
        if number3 > largest:
            largest = number3

        output = largest

        
print(output)


# 2. Check if a year is a leap year

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    result = "Leap year"
else:
    result = "Normal year"

print(result)



# 3. Check if a number is divisible by 3, 5, or both

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    result = "The number is divisible by both."
elif number % 3 == 0:
    result = "The number is divisible by 3"
elif number % 5 == 0:
    result = "The number is divisible by 5"
else:
    result = "The number is not divisible by 3 or 5"


print(result)


# 🎯 Confidence signal: You no longer hesitate about condition order or edge cases.

# 🟦 TOPIC 2: LOOPS
# Easy
# 1. Print numbers from 1 to n

n = int(input("enter a number: "))

for i in range(1,n+1):
    print(i)


# 2. Print numbers from n to 1

n = int(input("enter a number: "))

for i in range(n,0,-1):
    print(i)


# 3. Print all even numbers between 1 and n

n = int(input("Enter a number: "))

for i in range(2,n+1,2):
    print(i)
    

# Medium
# 1. Find the sum of digits of a number

number = int(input("Enter a number: "))


sum = 0

while number > 0:
    sum = sum + number % 10
    number = number // 10

print(sum)


# 2. Reverse a number

number = int(input("Enter a number: "))
reversed_digit = 0

while number > 0:
    reversed_digit = (reversed_digit * 10) + (number % 10)
    number = number // 10

print(reversed_digit)



# 3. Count how many digits are in a number

number = int(input("Enter a number: "))
digit_count = 0

while number > 0:
    number = number // 10
    digit_count+=1
  
print(digit_count)



# 🎯 Confidence signal: You can control loop start, stop, and update without guessing.

# 🟦 TOPIC 3: STRINGS
# Easy
# 1. Count vowels in a string
# 2. Reverse a string
# 3. Count number of characters in a string
# Medium
# 1. Check if a string is a palindrome
# 2. Count number of words in a sentence
# 3. Find the longest word in a sentence
# 🎯 Confidence signal: You’re comfortable iterating character-by-character and word-by-word.

# 🟦 TOPIC 4: LISTS
# Easy
# 1. Find the largest number in a list (no max)

number_list = [1,8,5,6,6,2]
largest_number = number_list[0]

for i in number_list:
    if i > largest_number:
        largest_number = i

print(largest_number)

# 2. Find the smallest number in a 

listt = [1,4,3,-4,3,5]
smallest_num = listt[0]

for num in listt:
    if num < smallest_num:
        smallest_num = num

print(smallest_num)


# 3. Count even and odd numbers in a list

listt = [1,5,32,7,4,74,3]
even_count = 0
odd_count = 0

for num in listt:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:",even_count)
print("Odd numbers: ",odd_count)


# Medium
# 1. Find the second largest number in a list

listt = [5,5,1,2]

for num in listt:
    if listt[0] > listt[1]:
        largest = listt[0]
        second_largest = listt[1]
    else:
     
        largest = listt[1]
        second_largest = listt[0]

for num in listt[2:]:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest:
        second_largest = num



print(largest)
print(second_largest)
    




# 2. Reverse a list manually
# 3. Remove duplicates from a list (preserve order)
# 🎯 Confidence signal: You naturally think in terms of traversal + tracking values.

# 🟦 TOPIC 5: TUPLES
# Easy
# 1. Iterate over a tuple and print elements
# 2. Find max and min in a tuple
# Medium
# 1. Count occurrences of an element in a tuple
# 2. Convert a tuple to a list, modify one element, convert back
# 🎯 Confidence signal: You clearly understand immutability and fixed data.

# 🟦 TOPIC 6: DICTIONARIES
# Easy
# 1. Create a dictionary from two lists
# 2. Check if a key exists in a dictionary
# 3. Print all keys and values
# Medium
# 1. Count frequency of elements in a list
# 2. Find the key with the highest value
# 3. Count frequency of characters in a string
# 🎯 Confidence signal: You instinctively reach for a dictionary when counting or grouping.

# 🟦 TOPIC 7: SETS
# Easy
# 1. Remove duplicates from a list using a set
# 2. Find common elements between two lists
# Medium
# 1. Find elements that appear only once in a list
# 🎯 Confidence signal: You understand uniqueness vs order trade-offs.

# ⏱️ HOW TO EXECUTE (IMPORTANT)
# * 2–3 problems per day
# * Don’t rush
# * If stuck >20 minutes → rewrite plain-English logic
# * Finish one topic fully before touching the next

# 🚦 WHEN YOU’LL BE READY FOR MIXED PROBLEMS
# You’ll notice:
# * You can understand problems faster
# * Plain-English logic feels natural
# * You debug by reasoning, not guessing
# At that point, mixed problems will feel like:
# “Oh, this is just multiple steps combined.”
# That’s the goal.

# 🎯 NEXT ACTION (DO THIS NOW)
# Start with Problem 1:
# Check if a number is positive or negative
# 👉 Write plain-English logic on paper.
# Then reply here with only the numbered steps (no code).
# I’ll review them and tell you when to move to the next problem.

