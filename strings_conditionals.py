# 🌱 LEVEL 1 — String Basics + Simple Conditions (Warm-up Logic)

# Goal: Be comfortable reading and inspecting text.

# Problems 1–15

# Take a name input → print it in uppercase

name = input("Enter your name:")

name = name.upper()

print(name)



# Take a name input → print it in lowercase

name = input("Enter a name: ")

name = name.lower()

print(name)

# Take a word → print length

name = input("enter a word:")

length = len(name)

print(length)

# Take a word → print first character

word = input("enter a word: ")

print(word[0])

# Take a word → print last character

word = input("enter a word: ")

length = len(word)

print(word[length-1])

    # Take a sentence → count characters

sentence = input("enter a sentence: ")

length = len(sentence)

print(length)


# Take a name → check if length > 5 → print message

name = input("Enter your name: ")

length = len(name)

if length > 5:
    message = "Your name's length is bigger than 5"

print(message)



# Take a word → check if first letter is capital

word = input("Enter a word:")

is_cap = word[0].isupper()

if is_cap:
    print("Yes")
else:
    print("No")

# Take a word → check if it equals "python"

word = input("Enter a word: ")

if word == "python":
    print("Yes")
else:
    print("No")

# Take a word → check if it is empty

word = input("Enter a word: ")

if not word:
    print("empty")
else:
    print("Not empty")

# Take a word → print reversed word

word = input("Enter a word: ")

rev_word = word[::-1]

print(rev_word)


# Take a name → print first 3 characters

name = input("Enter your name: ")

print(name[:3])



# Take a name → print last 2 characters

name = input("Enter your name: ")


print(name[-2:])

# Take a word → check if contains letter "a"

word = input("Enter a word: ")

if "a" in word:
    print("Yes")
else:
    print("No")

# Take a word → check if it ends with "ing"

word = input("Enter a word: ")

lastWords = word[-3:]

if lastWords == "ing":
    print("Yes")
else:
    print("No")

lastWords = word.endswith("ing")

print(lastWords)

# 🌿 LEVEL 2 — String Methods + Condition Thinking

# Goal: Start using built-in string tools like real code.

# Problems 16–30

# Take sentence → convert to lowercase → print

sentence = input("Enter a sentence: ")

lower_sentence = sentence.lower()

print(lower_sentence)

# Take sentence → remove spaces using .strip()

sentence = input("Enter a sentence: ")

remove_space = sentence.strip()
print(remove_space)


# Take sentence → replace "bad" with "good"

sentence = "Girls love dreamy boys."

result = ""

i = 0

while(i < len(sentence)):
    if sentence[i:i+3] == "bad":
        result += "good"
        i += 3
    else:
        result += sentence[i]
        i+=1

print(result)

result2 = sentence.replace("bad","good")

print(result2)


# Take sentence → count how many times "a" appears

sentence = input("Enter a sentence: ")


a_frequency = sentence.count("a")

print(a_frequency)


counter = 0

for val in sentence:
    if val == "a":
        counter+=1

print(counter)


# Take email → check if contains "@"

email = input("Enter an email: ")

if "@" in email:
    answer = "yes"
else:
    answer = "no"

print(answer)

# Take word → check if all letters are digits

word = input("Enter a word: ")

all_digits = True

for ch in word:
    if ch < '0' or ch > '9':
        all_digits = False


print(all_digits)



# Take word → check if alphabet only

word = input("Enter a word")

is_alpha = True

for ch in word:
    if (ch < 'a' or ch > 'z') or (ch < 'A' or ch > 'Z'):
        is_alpha = False


print(is_alpha)



# Take password → check length >= 8

password = input("Enter your password: ")

if len(password) >= 8:
    print("Yes")
else:
    print("No")


# Take sentence → split words → print word count

sentence = input("Enter a sentence: ")

word_count = 0

split_sentence = sentence.split()


for i in range(len(sentence)):
    if not (sentence[i].isspace()) and (sentence[i-1].isspace() or i == 0):
        word_count += 1
 

print(split_sentence)

print(word_count)




# Take sentence → print first word

sentence = input("Enter a sentence: ")

word = ""

i = 0

#skip leading spaces

while i < len(sentence) and sentence[i].isspace():
    i+=1


#collect first word

while i < len(sentence) and not sentence[i].isspace():
    word = word + sentence[i]
    i+=1


print(word)

# Take full name → split → print last name

name = input("Enter your name: ")



# Take word → check if palindrome

# Take word → check if starts with vowel

# Take word → check if ends with digit

# Take sentence → remove all spaces

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