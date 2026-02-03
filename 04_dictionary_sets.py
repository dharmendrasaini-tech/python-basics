# 🟢 LEVEL 1 — Basics (Warm-up)

# Create a dictionary with keys: name, age, city. Print all values.

student = {
    "name" : "Dharmendra",
    "age" : 32,
    "city" : "Jaipur"
}

print(student.values())

# Access the value of a key entered by the user.

student = {
    "name" : "aman",
    "age" : 34,
    "city" : "chennai"
}

findKey = input("Enter a key: ")

print(student.get(findKey))

# Add a new key email to an existing dictionary.

student = {
    "name" : "dhatarwal",
    "age" : 12,
    "city" : "jalore"


}

student["email"] = "dsp@gmail.com"

student.update({"marks" : 23, "passed": "Yes"})

print(student)

# Update the value of an existing key.

student = {
    "name" : "rohit",
    "age" : 45,
    "marks" : 23
            
}

student["name"] = "rahul"

print(student)

# Delete a key from a dictionary.

student = {
    "name" : "mohit",
    "marks" : 12,
    "passed" : "yes"
}

student.pop("name",None)

print(student)



# Check if a key exists in a dictionary.

record = {
    "name" : "rohan",
    "purpose" : "doctor",
    "age" : 23
}

print(record.get("name"))

# Print all keys.

record = {
    "name" : "anita",
    "age" : 12,
    "passed" : "Yes"
}

print(record.keys())

# Print all values.

record = {
    "name" : "ram",
    "age" : 34,
    "passed" : "yes"
}

print(record.values())


# Store following word meanings in a python dictionary: 
# table : "a piece of furniture", "list of facts and figures"
# cat : "a small animal"

dict1 = {
    "table": ("a piece of furniture","list of facts and figures"),
    "cat": "a small animal"
}

# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

# "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"


classrooms = {

"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
}


print(len(classrooms))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value.

marks = {}

x = int(input("Enter maths marks: "))
y = int(input("Enter physics marks: "))
z = int(input("Enter chemistry marks: "))

marks.update({"maths":x})
marks.update({"physics": y})
marks.update({"chemistry": z})


print(marks)



# 1️⃣ Remove Duplicates (Warm-up)

# You are given a list of numbers.

# 👉 Convert this into a set and print the unique numbers.

nums = [1, 2, 3, 2, 4, 1, 5, 3]


numSet = set(nums)

print(numSet)



# 2️⃣ Count Unique Values

# Given:

subjects = ["python", "java", "python", "c", "java", "c++"]

# 👉 Print how many unique subjects are there.

subj = set(subjects)

print(len(subj))

