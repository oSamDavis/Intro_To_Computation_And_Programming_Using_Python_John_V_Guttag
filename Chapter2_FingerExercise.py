# Author: Sam Davis Omekara Jr.

# Finger Exercise on Page 18 :  program to find the largest odd number of three numbers
x = 7
y = 6
z = 8

result = 0  # initializing result to be 0

if x % 2 != 0:  # checking if x is odd
    result = max(result, x)  # if x is odd then result should be the max between result and x
if y % 2 != 0:
    result = max(result, y)  # if y is odd then result should be the max between result and y
if z % 2 != 0:
    result = max(result, z)  # if z is odd then result should be the max between result and z

if result == 0:  # if the result remains 0 then it means none of the numbers were odd
    print("No odd numbers found")
else:
    print(result)  # else print the result

# squaring an integer number using repetitive addition
num = int(input("Enter an number:"))
ans = 0
itersLeft = abs(num)

while itersLeft != 0:
    ans += abs(num)
    itersLeft -= 1

print(str(num), "*", str(num), "=", str(ans))

# Finger Exercise on page 24: Printing a Letter n number of times
numsXs = int(input("How many times do you wish to print the letter X? "))
toPrint = ""
while numsXs != 0:
    toPrint += "X"  # concatenating letter X to the variable toPrint
    numsXs -= 1  # reducing the numsXs

print(toPrint)

# Find a positive integer that is divisible by both 11 and 12
x = 12

while True:
    if x % 11 == 0 and x % 12 == 0:
        break
    x += 1

print(x, "is divisible by both 11 and 12")

# Finger Exercise on page 24: Largest odd of 10 integers
n = 10
largestOdd = 0
print("Enter 10 integer numbers :")
while n != 0:
    inputNum = int(input())
    if inputNum % 2 != 0:
        largestOdd = max(largestOdd, inputNum)
    n -= 1

if largestOdd == 0:
    print("No odd numbers were entered.")
else:
    print(largestOdd, "is the largest Odd number Entered")