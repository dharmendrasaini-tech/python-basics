# 🌱 LEVEL 1 — String Basics + Simple Conditions (Warm-up Logic)

# Goal: Be comfortable reading and inspecting text.

# Problems 1–15

# Take a name input → print it in uppercase
name = input("Enter your name: ")

result = ""

for ch in name:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)


# Take a name input → print it in lowercase

name = input("Enter your name: ")

result = ""

for ch in name:
    if 'A' <= ch <= 'Z':
        result += chr(ord(ch)+ 32)

    else:
        result += ch

print(result)


# Take a word → print length

word = input("Enter a word: ")
length = 0

for ch in word:
    length += 1


print(length)


# Take a word → print first character

word = input("Enter a word:")

first_ch = ""

if word:
    first_ch = word[0]


print(first_ch)


# Take a word → print last character

word = input("Enter a word: ")

last_chr = ""

if word:
    last_chr = word[-1]

print(last_chr)


# Take a sentence → count characters

sentence = input("Enter a sentence: ")
char_count = 0

for ch in sentence:
    char_count += 1

print(char_count)



# Take a name → check if length > 5 → print message

name = input("Enter a name: ")
length = 0

for ch in name:
    length += 1


if length > 5:
    print("Yes")
else:
    print("No")




# Take a word → check if first letter is capital

word = input("Enter a word:")

is_cap = word[0].isupper()

if is_cap:
    print("Yes")
else:
    print("No")

# Take a word → check if it equals "python"

word = input("Enter a word:")

normalized = word.strip().lower()

print(normalized == "python")

# method 2

word = input("Enter a word:")

check = "python"

is_python = True

if len(word) != len(check):
    is_python = False

else:
    for i in range(len(word)):
        if word[i] != check[i]:
            is_python = False
            break


print(is_python)    


#method 3

word = input("Enter a word: ")

word_check = "python"

is_true = True

if len(word) != len(word_check):
    is_true = False
else:
    for ch1, ch2 in zip(word,word_check):
        if ch1 != ch2:
            is_true = False
            break

print(is_true)


# Take a word → check if it is empty

word = input("Enter a word: ")

is_empty = True

for ch in word:
    if ch != "":
        is_empty = False
        break


print(is_empty)

#method 2

word = input("Enter a word: ")

is_empty = not word

print(is_empty)
    



# Take a word → print reversed word

word = input("enter a word: ")

rev_word = ""

for ch in word:
    rev_word = ch + rev_word

print(rev_word)

    # Take a name → print first 3 characters

    name = input("enter a name: ")
    first_three = ""

    i = 0

    while i < 3 and i < len(name):
        first_three = first_three + name[i]
        i+=1

    print(first_three)

#method 2

name = input("Enter your name: ")
first_three = ""

for i in range(min(3,len(name))):
    first_three += name[i]



print(first_three)



# Take a name → print last 2 characters

name = input("enter your name: ")

for i in range(-1,-3,-1):
    print(name[i])


# Take a word → check if contains letter "a"

word = input("Enter a word: ")

if 'a' in word:
    print("Yes")
else:
    print("No")


# Take a word → check if it ends with "ing"

word = input("Enter a word: ")

ends_with = word[-3:]

if ends_with == "ing":
    print("Yes")
else:
    print("No")



# 🌿 LEVEL 2 — String Methods + Condition Thinking

# Goal: Start using built-in string tools like real code.

# Problems 16–30

# Take sentence → convert to lowercase → print

sentence = input("Enter a sentence: ")

all_lower = sentence.lower()

print(all_lower)



# Take sentence → remove spaces using .strip()

sentence = input("enter a sentence: ")

rem_spaces = sentence.strip()

print(rem_spaces)

#method 2

sentence = input("enter a sentence: ")
no_space = ""

for ch in sentence:
    if not ch.isspace():
        no_space += ch

print(no_space)


#method 3

sentence = input("enter a sentence: ")

no_spaces = "".join(sentence.split())

print(no_spaces)



# Take sentence → replace "bad" with "good"

sentence = input("enter a sentence: ")

new_sentence = sentence.replace("bad","good")

print(new_sentence)


#method 2

sentence = input("enter a sentence")
good_sentence = ""

i = 0

while i < len(sentence):

    if sentence[i:i+3] == "bad":
        good_sentence = good_sentence + "good"
        i += 3
    else:
        good_sentence = good_sentence + sentence[i]

        i += 1


print(good_sentence)



# Take sentence → count how many times "a" appears

sentence = input("Enter a sentence: ")
a_times = 0

for ch in sentence:
    if ch == "a":
        a_times += 1

print(a_times)


# Take email → check if contains "@"

email = input("Enter your email: ")

if "@" in email:
    print("Yes")


else:
    print("No")


# Take word → check if all letters are digits


word = input("Enter a word: ")

all_digits = True

for ch in word:
    if ch < '0' or ch > '9':
        all_digits = False
        break

print(all_digits)


# Take word → check if alphabet only

word = input("Enter a word:")

only_alpha = True

for ch in word:
    if not ( 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'):

        only_alpha = False
        break

print(only_alpha)

# Take password → check length >= 8

password = input("Enter your password: ")

length = len(password)

if length >= 8:
    print("yes")
else:
    print("No")



# Take sentence → split words → print word count

sentence = input("Enter a sentence: ")

counter = 0

for i in range(len(sentence)):
    if not sentence[i].isspace() and (i == 0) or sentence[i-1].isspace():
        counter+=1
    

print(counter)


sentence = input("enter a sentence: ")

split_sentences = sentence.split()

print(len(split_sentences))




# Take sentence → print first word

sentence = input("Enter a sentence: ")

first_word = ""

i = 0

#remove leading spaces
while i < len(sentence) and sentence[i].isspace():
    i+=1

while i < len(sentence) and not sentence[i].isspace():
    first_word += sentence[i]
    i+=1

print(first_word)



# Take full name → split → print last name

name = input("Enter your name: ")

last_name = ""

if not name:
    print(last_name)

else:
    i = -1

    while i >= -len(name) and name[i].isspace():
        i -= 1

    while i>= -len(name) and name[i].isspace():
        last_name = name[i] + last_name
        i -= 1

    print(last_name)







# Take word → check if palindrome

word = input("enter a word: ")
rev_word = ""
length = len(word)

for i in range(length -1,-1,-1):
    rev_word += word[i]



if rev_word == word:
    print("yes")
else:
    print("no")




# Take word → check if starts with vowel

word = input("Enter a word: ")

if word and word[0] in 'aeiou':
    print("yes")
else:
    print("no")



# Take word → check if ends with digit

word = input("Enter a word: ")

last_digit = word[-1]

if word and '0' <= last_digit <= '9':
    print("Yes")
else:
    print("No") 

# Take sentence → remove all spaces

sentence = input("enter a sentence: ")

remove_spaces = ""

i = 0

while(i < len(sentence)):
    if not sentence[i].isspace():
        remove_spaces += sentence[i]
        i+=1
    
    i+=1


print(remove_spaces)







# 🌳 LEVEL 3 — Real Decision Logic

# Goal: Combine string + if/else logic.

# Problems 31–45

# Take age input → if >= 18 print Adult else Minor

# Take number string → check if positive or negative

# Take username → if length < 4 → invalid

# Take password → check if contains number

# Take password → check if contains uppercase

# Take password → check if contains special char

# Take name → if empty → ask again message

# Take score → print Grade (A/B/C/D)

# Take temperature → classify Hot/Warm/Cold

# Take word → if length even → print Even

# Take word → if length odd → print Odd

# Take country → if "india" → print Local User

# Take input → if numeric → convert → else error message

# Take string number → if > 100 → print Large

# Take word → check if contains space

# 🌲 LEVEL 4 — Real World Mini Logic (Almost Program Thinking)

# Goal: Multi-condition thinking.

# Problems 46–60

# Login check → username + password match

# Email validation → must contain @ and .

# Password strength → length + number + uppercase

# Name validation → no digits allowed

# Phone validation → length must be 10 digits

# Check if string is integer number

# Check if string is decimal number

# Check if string is valid yes/no answer

# Grade calculator with ranges

# Shopping discount logic

# ATM PIN check simulation

# Username must start with letter

# Sentence word count + length check

# Detect spam word in message

# Check if two strings are anagrams

# 🌌 LEVEL 5 — Challenge Brain (Edge Case Thinking)

# Goal: Start thinking like real software.

# Problems 61–70

# Username must be 5–15 chars + no spaces

# Password must have uppercase + number + special char

# Detect if string is palindrome ignoring spaces

# Count vowels in sentence

# Find longest word in sentence

# Mask email (hide middle characters)

# Validate date format (basic check only)

# Detect repeated characters in string

# Check if string contains only whitespace

# Menu system (input → conditional → action)

# 🧬 Hidden Skill This Will Build

# By end you’ll naturally think:

# Input → Clean → Validate → Decide → Act


# That’s backend logic.
# That’s API validation.
# That’s authentication systems.
# That’s 60% of real software work.

# ⚡ How To Do These (Important)

# Don’t rush.

# For each problem:
# 1️⃣ Predict behavior
# 2️⃣ Write code
# 3️⃣ Test edge cases
# 4️⃣ Break it intentionally

# You’re stepping into the part of programming where computers stop being calculators and start being decision-making machines — and that’s where software starts feeling less like math and more like teaching logic to electricity.