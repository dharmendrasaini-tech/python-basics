
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




# 🟦 TOPIC 3: STRINGS
# Easy
# 1. Count vowels in a string

str1 = "aeiouther"
count = 0

for i in str1:
    if i in 'aeiou':
        count+=1

print(count)

# 2. Reverse a string


str1 = "dharmendra"

length = len(str1)

rev_string = ""

for i in range(length-1,-1,-1):
    rev_string = rev_string + str1[i]



print(rev_string)


# 3. Count number of characters in a string

str1 = "dharmendra"
count = 0

for i in str1:
    count+=1

print(count)


# Medium
# 1. Check if a string is a palindrome

str1 = "madamji"

rev_string = ""

length = len(str1)

for i in range(length-1,-1,-1):

    rev_string += str1[i]


if str1 == rev_string:

    print("Palindrome")
else:
    print("Non Palindrome")


# 2. Count number of words in a sentence

str1 = "I will be back."
counter = 0

for i in range(len(str1)):
    if (not str1[i].isspace()) and (i == 0 or str1[i-1].isspace()):
        counter+=1


    
print(counter)


# 3. Find the longest word in a sentence

sentence = "dharmendra is a very passionate man."
current_wordlength = 0
max_wordlength = 0

for ch in sentence:
    if not ch.isspace():
        current_wordlength+=1
    else:
        if current_wordlength > max_wordlength:
            max_wordlength = current_wordlength
        current_wordlength = 0



if current_wordlength > max_wordlength:
    max_wordlength = current_wordlength

print(max_wordlength)



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

listt = [1,5,2,7,4,8]
rev_listt = []


for items in range(len(listt)-1,-1,-1):
    rev_listt.append(listt[items])

print(rev_listt)


# 3. Remove duplicates from a list (preserve order)

listt = [2,6,4,1,8,1,3,2]

new_listt = []

for items in listt:
    if items not in new_listt:
        new_listt.append(items)


print(new_listt)
    





# 🟦 TOPIC 5: TUPLES
# Easy
# 1. Iterate over a tuple and print elements

values = (1,4,3,6,2,4,3,1)

for val in values:
    print(val)



# 2. Find max and min in a tuple

values = (1,3,7,4,2,56,8,4)
max_value = values[0]
min_value = values[0]

for i in range(len(values)):
    if values[i] > max_value:
        max_value = values[i]
    if values[i] < min_value:
        min_value = values[i]


print(max_value)
print(min_value)



# Medium
# 1. Count occurrences of an element in a tuple

values = (1,5,8,3,5,8,4,8)
element = 5
occurance = 0

for i in range(len(values)):
    if values[i] == element:
        occurance+=1


print(occurance)


    

# 2. Convert a tuple to a list, modify one element, convert back

values = (1,5,3,6,2,6,43)

values2 = list(values)

values2[0] = 34

values3 = tuple(values2)

print(values3)




# 🟦 TOPIC 6: DICTIONARIES
# Easy
# 1. Create a dictionary from two lists

list1 = [1,2,3,4,5]
list2 = ["apple","orange","banana","oats","rice"]

result = {}

for i in range(len(list1)):
    result[list1[i]] = list2[i]

print(result)

# 2. Check if a key exists in a dictionary

values = {"amit": 5, "suresh": 7, "harish": 8}

key = "amit"

is_key = key in values

print(is_key)


# 3. Print all keys and values

dict1 = {"aman":23, "rohian": 34, "plane": 65}

for key,value in dict1.items():
    print(key,value)



# Medium
# 1. Count frequency of elements in a list

list1 = [1,2,3,1,2,3,1,2,3]

freq = {}

for i in list1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)





# 🟦 TOPIC 7: SETS
# Easy
# 1. Remove duplicates from a list using a set

values = [1,2,4,6,7,5,4,5,5,6]

values = set(values)

print(values)


# 2. Find common elements between two lists

list1 = [1,4,5,3,4,6,4,4,3]
list2 = [3,5,6,4,3,2,4,5,6]

list1 = set(list1)
list2 = set(list2)

common = list1 & list2

print(common)


# Medium
# 1. Find elements that appear only once in a list

list1 = [1,2,4,6,3,3,3,5,3,67,4]
unique = 0

for i in range(len(list1)):
    if list1.count(list1[i]) == 1:
        unique += 1



print(unique)


