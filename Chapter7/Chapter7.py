import string
# Handling my first exception page 102:
numSuccesses = 14
numFailures = 0
try:
    successFailureRatio = numSuccesses / numFailures  # tries this statement
    print("The success/failure ratio is", successFailureRatio)
except ZeroDivisionError:  # handles an exception if a zero division occurs
    print("No failures recorded so Success/Failure ratio is undefined")

print("Control Here Now.")

# Finger Exercise on Page 102: Implement a function that meets the specification below. Use a try-except block
def sumDigits(s):
    '''
    :param s: a string
    :return: returns sum of digits in the string s
    E.g if string is a2b3c it return 5
    '''
    try:
        res = 0
        for char in s:  # for each char in s
            if char.isdigit():  # if char is a digit
                res += int(char)  # add it to res var
        return res  # return res at the end of the loop
    except TypeError:  # if s is not a string, I raise an error
        print("Function sumDigits called with bad arguments")  # Error message

        return None  # returns None


print(sumDigits("a2b3c"))

# Function to read an Integer Number from user with exception handling
def readInt():
    while True:
        val = input("Enter an integer")
        try:
            return int(val) # converts str from input to int before returning
        except ValueError:
            print(val, "is not an integer")

# Generalized(Polymorphic) Function to read a value from user with exception handling:
def readVal(valType, requestMsg, errorMsg):
    while True:
        val = input(requestMsg + " : ")
        try:
            return valType(val)  # converts val from str to valType before returning
        except (ValueError, TypeError):
            print(val, errorMsg)


readVal(float,"Enter a Float","Not a float")  # readVal function call

# Finger Exercise on page 105
def findAnEven(L):
    '''
    :param L: A list of integers
    :return: first even number in L
    Raises value Error if L doesn't contain an even number
    '''
    for e in L:  # for each element in list L
        try:  # try ...
            if e % 2 == 0 and e != 0:  # if an even number exists...
                return e  # return such an even number
        except TypeError:  # except if a Type Error is encountered
            print("Function called with bad arguments")  # function was called with a bad argument
            return float('nan')  # return not a number
    raise ValueError("List doesn't contain an even number")  # raise a Value error is list doesn't have an even number


print(findAnEven(['c', '3', 'c', 'b', 'a']))  # function findAnEven invocation

# Get Ratios Function on Page 106:
def getRatios(vect1, vect2):
    '''

    :param vect1: a list of length n
    :param vect2: a list of same length n
    :return: a list containing meaningful values vect1[i]/vect2[i]
    '''

    ratios = []  # list to hold ratios
    for i in range(len(vect1)):  # for i from 0 to length of vect1 - 1
        try:  # try...
            ratios.append(vect1[i]/vect2[i]) # ... appending vact1[i]/vect2[i]
        except ZeroDivisionError:  # except if a zero division error is encountered...
            ratios.append(float('nan'))  # append the float not a number
        except:  # except if any other error is encountered e.g lists aren't the same length...
            raise ValueError("Function getRatios called with bad arguments") # raise a value error

    return ratios


#  getRatios function invocations ...
try:
    print(getRatios([1.0, 2.0, 7.0, 6.0], [1.0, 2.0, 0.0, 3.0]))
    print(getRatios([], []))
    print(getRatios([1.0, 2.0], [3.0]))
except ValueError as msg:  # prints the string associated with value Error
    print(msg)


# Get Grades Function on page 108:
def getGrades(fname):
    '''

    :param fname: a string that represents a file name
    :return: a list containing the grades
    '''
    try:  # try ...
        gradesFile = open(fname, 'r') # open file for reading
    except IOError:  # except an IOError is encountered
        raise ValueError('getGrades could not open ' + fname)  # raise a value error
    grades = []  # to store the grades
    for line in gradesFile:  # for each line in the gradesFile
        try:  # try...
            grades.append(float(line))  # appending the he grade as a float
        except:  # except if an error is encountered
            raise ValueError("Unable to convert line to float")  # raise a value error

    return grades  # return the list grades


# getGrade Function Invocation
try:
    grades = getGrades('testGetGrades.txt')
    grades.sort()
    median = grades[len(grades) // 2]
    print("Median grade is", median)
except ValueError as errorMsg:
    print("Whoops.", errorMsg)


# My first Assert Statement
def getAverage(grades):
    '''

    :param grades: a list of grades
    :return: the average of grades
    '''

    assert list(grades)  # asserting that the function argument is a list
    assert len(grades) != 0  # asserting that the lsit is not empty

    return sum(grades)/len(grades)  # returns the average of grades

# getAverage Function Invocation
print(getAverage(grades))
