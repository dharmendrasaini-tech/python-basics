# 1 Print numbers from 1 to 100.

i = 1

while i <= 100:
    print(i)
    i += 1

# 2 Print numbers from 100 to 1.

i = 100

while i >= 1:
    print(i)
    i -= 1


# 3 Print the multiplication table of a number n.

n = int(input("enter a number: "))
i = 1

while i <= 10:
    print(n, " * ", i, " = ", n * i)
    i += 1


# 4 Print the elements of the following list using a loop:
num1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 0

while i < len(num1):
    print(num1[i])
    i += 1

# 5 Search for a number x in this tuple using loop: [1,4,9,16,25,36,49,64,81,100]

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter a number to search: "))

i = 0

while i < len(nums):
    if x == nums[i]:
        print("Found at index", i)
        break
    else:
        print("Finding")
    i += 1
print("end of loop")


# 6 Print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for i in nums:
    print(i)

# 7 Search for a number x in this tuple using loop: [1,4,9,16,25,36,49,64,81,100]

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 22

for i in nums:
    if i == x:
        print("Found")

# 8 Print numbers from 1 to 100 using range.

for i in range(1,101):
    print(i)
    
#9 Print numbers from 100 to 1.

for i in range(100,0,-1):
    print(i)
    
#10 Print the multiplication table of a number n.

n = 10

for i in range(1,11):
    print(i * n)
    
    
#11 Write a program to find the sum of first n numbers.(using while)

n=5

i=1

sum=0

while i<=n:
    sum = sum+i
    i+=1
    
print(sum)




# 🟢 Level 1 — Warm-up (build confidence)

# 1️⃣ Print numbers from 1 to n

n = int(input("Enter a number: "))

i=1

while i<=n:
    print(i)
    i+=1
    

# 2️⃣ Print numbers from n to 1

n = int(input("Enter a number: "))

i = n

while i >= 1:
    print(i)
    i-=1


# 3️⃣ Print even numbers from 1 to n

n = int(input("Enter a number: "))

i=1

while i <= n:
    if(i % 2 == 0):
        print(i)
    i+=1

#or

n = int(input("Enter a number: "))

i=2

while(i<=n):
    print(i)
    i+=2


# 4️⃣ Print odd numbers from 1 to n

n = int(input("Enter a number: "))

i = 1;

while i<=n:
    print(i)
    i+=2
    


# 5️⃣ Find the sum of first n numbers

n = int(input("Enter a number: "))

sum=0
i=1

while i<=n:
    sum = sum+i
    i+=1
    
print("Sum: ",sum)
    


# 6️⃣ Find the sum of even numbers from 1 to n

n = int(input("Enter a number: "))

i = 2

sum = 0


while i<=n:
    
    sum = sum + i
    i+=2
    
print("Sum: ",sum)

# 🟡 Level 2 — Core logic (important)

# 7️⃣ Find the factorial of a number

n = int(input("enter a number: "))

fact = 1

i = 1

while i<=n:
    fact = fact * i
    i+=1
    
print(fact)



# 8️⃣ Count the number of digits in a number

n = int(input("enter a number: "))

counter = 0

while n > 0:
    n = n // 10

    counter = counter+1
      
 
print(counter)
    
    

# 9️⃣ Reverse a number

n = int(input("enter a number: "))

rev = 0

while n>0:
 
    rev = rev * 10 + (n %10)
    n = n // 10
    
print(rev)


# 10️⃣ Check whether a number is a palindrome

n = int(input("enter a number: "))
nCopy = n

rev=0

while n>0:
    rev = rev * 10 + (n % 10)
    
    n = n // 10
    
print(rev)
    
if(rev == nCopy):
    print("Palindrom")
else:
    print("Not palindrom")
    







    
