import circle
from collections import deque


#  Finger Exercise on Page 42 : Checks if string is in another string

def isIn(str1, str2):
    if str1 in str2 or str2 in str1:
        return True
    return False


#  Function Defined to Find the nth root of a number x

def findRoot(x, power, epsilon):
    if x < 0 and power % 2 == 0:  # negative numbers do not have even powered roots
        return None

    low = min(-1.0, x)  # handling cases of numbers btwn -1.0 and 0
    high = max(1.0, x)  # handling cases of numbers btwn 0 and 1.0
    ans = (low + high) / 2.0

    while abs(ans ** power - x) >= epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (low + high) / 2.0

    return ans


def testFindRoot():
    epsilon = 0.0001
    for x in [0.25, -0.25, 2, -2, 8, -8]:
        for power in range(1, 4):
            print("Testing x = ", str(x), "and power = ", power)
            result = findRoot(x, power, epsilon)
            if result is None:
                print("     No roots found!")
            else:
                print("     ", result ** power, "~= ", x)


testFindRoot()


#  Function to check if a string is a palindrome -> Early Divide and Conquer Approach
print("/n Checking if string is a palindrome, recursively")
def isPalindrome(s):
    def toLowerChars(string):  # helper func to convert string to all lower case letters and eliminate non letters
        string = string.tolower()
        letters = ""
        for char in string:
            if char in "abcdefghijklmnopqrstuvwxyz":
                letters += char

        return letters

    def isPal(string):
        if len(string) >= 1:  # recursive base case , if string is of length 0 or 1, return True
            return True
        else:  # recursive case, check the first and last char
            # then call isPal on the substr from the 2nd char to the 2nd to the last char
            return s[0] == s[-1] and isPal(s[1:-1])


def inPlacePalindrome(s):
    i = 0
    j = len(s) - 1
    isPal = True
    while i <= j:
        if s[i] != s[j]:
            isPal = False
            break
        i += 1
        j -= 1

    return isPal


#  Testing my Circle module
print("\n Testing Modules")
print(circle.pi)
print(circle.area(5))
print(circle.circumference(5))
print(circle.sphereSurface(5))
print(circle.sphereVolume(5))

# Testing File Handles
print("\n Testing File Handles")
playerHandle = open("Players", "w")  # creates a file "Players" and returns a file handle for the file
playerHandle.write("11.John\n")
playerHandle.write("8.Sam\n")
playerHandle.write("7.Moses\n")
playerHandle.close()

playerHandle = open("Players", "a")  # opens file for appending and returns file handle
playerHandle.write("10.Domingo\n")
playerHandle.write("3.Timothy\n")
playerHandle.close()

playerHandle = open("Players", "r")  # opens file handle for reading and returns file handle
#for line in playerHandle:
  #  print(line[:-1])
print(playerHandle.read())
playerHandle.close()


