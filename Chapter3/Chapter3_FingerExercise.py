# Author : Sam Davis Omekara Jr.

# Program to find the cube root of a positive integer

number = int(input("Enter a number: "))
ans = 0

while ans ** 3 < abs(number):
    ans += 1

if ans ** 3 != abs(number):
    print("The number Entered is not a perfect cube")
else:
    if number < 0:
        ans = -ans
    print("The cube root of ", number, "is", ans)

# Finger Exercise on Page 27
num = int(input("Enter an integer number: "))
pwr = 2

isFound = False  # boolean variable to check if any pair isFound

while pwr < 6:
    root = 1
    while root <= abs(num):  # loop checking all possibilities of root from 1 til num (i.e Exhaustive Enumeration)
        if root ** pwr == abs(num):  # if the root raised to pwr == num
            if num < 0:  # if the number entered was negative update its root accordingly
                root = -root
            print("root and pwr pair are:", root, pwr)
            print(str(root) + "**" + str(pwr), "=", num)
            isFound = True  # updating isFound variable to True
        root = abs(root) + 1  # increasing the root . (i.e Inner Loop Control)
    pwr += 1  # increasing the pwr. (i.e Outer Loop Control)

if not isFound:
    print("None of such pairs were found")

# Implementing Program to Find The Cube Root of A Number with A For Loop Statement
x = int(input("Enter a number: "))
for ans in range(0, abs(x) + 1):
    if ans ** 3 >= x:
        break

if ans ** 3 != abs(x):
    print(x, "is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print(ans, "is the cube root of ", x)

# Program to add all digits in a string
total = 0
for c in "12345678":
    total += int(c)
print("1+2+3+4+5+6+7+8 =", total)

# Finger Exercise on Page 30
s = "1.23,2.4,3.123"
lastComma = -1  # object holding the index of the last comma
summation = 0.0  # object storing the sum
i = 0  # object keeping track of the index of c in s
for c in s:  # for loop to loop through all characters in the string
    if c == ",":  # if the character is a comma, then get characters between the last comma and newly found comma
        summation += float(s[lastComma + 1:i])
        lastComma = i  # updating the last comma
    if i == len(s) - 1:  # if c is the last character in s, then get characters between the last comma and end of string
        summation += float(s[lastComma + 1])  # can also be written as summation += float(s[lastComma+1:len(s)]
    i += 1

print(summation)


# Approximation Algorithm to find the square root of a number
square = 36  # var to hold the square of a variable
epsilon = 0.01  # epsilon, a region where the actual answer and approximate answer lies
increment = epsilon**2  # increment, increasing our square root by the sqr of epsilon
num_of_Guesses = 0  # var to hold num of guesses
sqr_root = 0.0  # var to hold the square root

while abs(sqr_root**2 - square) >= epsilon and sqr_root*sqr_root <= square:
    sqr_root += increment
    num_of_Guesses += 1

print("Number of Guesses:", num_of_Guesses)
if abs(sqr_root**2 - square) >= epsilon:
    print("Couldn't calculate the square root")
else:
    print(sqr_root, "is close enough to be the square root of", square)

# Finger Exercise on page 34 : Using Bisection search Algo to find the Cube Root of a number
cube = -125
epsilon = 0.01
low = 0
high = max(1.0, abs(cube))  # max func handles if cube lies btwn 0 and 1 and abs func handles negative cubes
guess = (high + low) / 2.0  # bisection search

while abs(guess**3 - abs(cube)) >= epsilon:
    if guess**3 < abs(cube):
        low = guess
    else:
        high = guess
    guess = (low + high) / 2.0  # update your guess

if cube < 0:  # if the cube was -ve
    guess = -guess
print("The cube root of", cube, "is approximately", guess)

# Finger Exercise on Page 38 : Newton-Raphson Algo, Successive Aprrox for finding square root of a num "num_sqr"
num_sqr = 10000
epsilon = 0.01
num_root = num_sqr / 2.0
num_iters = 0
while abs(num_root**2 - num_sqr) >= epsilon:
    num_root = num_root - (((num_root**2) - num_sqr)/(2*num_root))  # guess - f(guess)/f'(guess)
    num_iters += 1

print("Number of iterations = ", num_iters)
print(num_root, "is close enough to be the square root of", num_sqr)
