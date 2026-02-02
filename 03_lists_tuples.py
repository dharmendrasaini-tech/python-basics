# ✅ Lists & Tuples — PRACTICE SET (25 Problems)


 # 🟢 PART A — Lists (15 Problems)
# A1. Creation & Access

# Create a list of 5 integers and print it.

numbers = [1,2,3,4,5]

print(numbers)



# Print the first element of the list.

numbers = [1,2,3,4,5]

print(numbers[0])



# Print the last element of the list.

numbers = [1,2,3,4,5]

print(numbers[-1])


# Print the element at index 2.

numbers = [1,2,3,4,5]

print(numbers[2])

# Slice the list to print the first 3 elements.

numbers = [1,2,3,4,5]

print(numbers[0:3])

# Slice the list to print the last 4 elements.

numbers = [1,2,3,4,5]

print(numbers[-4:])



# A2. Modification

# Change the value at index 1 of a list.

numbers = [1,2,3,4,5]

numbers[1] = 12



# Append a new element to the list.

numbers = [1,2,34,4,5]

numbers.append(12)

print(numbers)


# Insert an element at index 2.

numbers = [1,2,3,3,45]

numbers.insert(2,123)

print(numbers)

# Remove a specific element from the list.

numbers = [1,2,3,3,4,5]

numbers.remove(3)

print(numbers)

# Remove the last element using pop() and print it.

numbers = [1,2,3,4,5,6]

numbers.pop()

print(numbers)

# Clear all elements from the list.

numbers = [1,2,3,4,5]

numbers.clear()

print(numbers)


# A3. Methods + Conditions

# Check whether a given number exists in a list using count().

numbers = [1,2,3,4,5]

numCheck  = int(input("Enter a number to check: "))


if(numbers.count(numCheck) > 0):
    print("Yes")
else:
    print("No")


# Count how many times a number appears in the list.

numbers = [1,2,3,3,4,5]

print(numbers.count(3))



# Copy a list and prove the original list remains unchanged.

numbers = [1,2,3,4,5]

numbers2 = numbers.copy()
numbers2.append(3)

print(numbers)
print(numbers2)



# 🟡 PART B — Tuples (10 Problems)
# B1. Creation & Access

# Create a tuple with 5 elements.

tup = (1,2,3,4,5)

print(type(tup))

# Print the first and last element of the tuple.

tup = (1,2,3,4,5)

print(tup[0])
print(tup[-1])



# Slice the tuple to get the first 3 elements.

tup = (1,2,3,4,5)

print(tup[0:3])

# Create a single-element tuple correctly.

tup = (1,)

print(type(tup))

# Check whether a value exists in a tuple using count().

tup = (1,2,3,4,5,56,6)

if(tup.count(3) > 0):
    print("Yes")
else:
    print("No")





# B2. Tuple Operations

# Count occurrences of an element in a tuple.

tup = (1,2,3,3,4,5)

print(tup.count(3))



# Find the index of a given element in a tuple.

tup = (1,2,3,4,5,6,7)

print(tup.index(4))



# Unpack a tuple of 3 elements into variables.

tup = (1,2,3)

a,b,c = tup

print(a,b,c)



# Swap two variables using a tuple.

a = 3
b = 4

(a,b) = (b,a)



# Convert a tuple to a list and print it.

tup = (1,2,3,4)

numbers = list(tup)

print(type(numbers))
print(type(tup))

print(numbers)