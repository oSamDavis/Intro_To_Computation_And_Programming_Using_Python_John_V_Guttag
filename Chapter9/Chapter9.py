# Exhaustive Method of Finding sqr root (pg. 138)
def squareRootExhaustive(x, epsilon):
    '''

    :param x: a positive float
    :param epsilon: a a positive float
    :return: returns y such that y*y is within epsilon of x
    '''

    step = epsilon**2  # step: to be sued to update our ans
    ans = 0.0  # ans var : to store the ans
    while abs(ans**2 - x) >= epsilon and ans**2 <= x:  # while the square of ans less x is greater than epsilon
                                                       # and the square of ans is less than x
        ans += step  # update the answer
    if ans**2 > x:  # after the loop ... if the square of the answer is greater than x
        raise ValueError("Square Root Not Found")  # raise a value error
    else:  # otherwise ...
        return ans  # return the answer

# Finding square root using bisectional search
def squareRootBisectional(x, epsilon):
    '''

    :param x: a positive float
    :param epsilon: a positive float
    :return: returns y such that y*y is within epsilon of x
    '''

    low = 0.0  # lower bound is 0
    high = max(1.0, x)  # upper bound is the max of 1 and 0
    ans = (high + low) / 2.0  # define ans by taking the average of low and high
    while abs(ans**2 - x) >= epsilon:  # while the square of the answer isn't epsilon units away from x
        if ans**2 < x:  # if the square of the answer is less than x ...:
            low = ans  # update low to the be the answer
        else:  # else the square of the answer is greater than x ...:
            high = ans  # update high to be the answer
        ans = (high + low) / 2.0  # update the answer
    return ans

# Function to Convert Int to String
def intToStr(x):
    '''

    :param x: x is a non-negative integer
    :return: returns the decimal string representation of x
    Time complexity : O(log x)
    '''

    digits = '0123456789'
    if x == 0:
        return '0'
    res = ''
    while x > 0:
        res = digits[x % 10] + res
        x = x // 10
    return res


print(intToStr(42932))  # function invocation

def addDigits(num):
    '''

    :param num: is a non-negative integer
    :return: the sum of digits in n
    Time complexity : O(log num)
    '''
    stringRep = intToStr(num)
    ans = 0
    for char in stringRep:
        ans += int(char)
    return ans


# Implementation of subset test on page 144
def isSubset(L1: list, L2: list) -> bool:
    '''

    :param L1: a list object
    :param L2: a list object
    :return: Returns True if each element in L1 is also in L2, otherwise False
    '''

    for e1 in L1:  # for each element in L1
        matched = False  # a flag
        for e2 in L2:  # and for each element in L2
            if e1 == e2:  # if element 1  is equal to element 2
                matched = True  # update the flag tp true
                break  # break the inner loop
        if not matched:  # if the flag is False
            return False  # return False
    return True  # return True

def intersect(L1, L2):
    '''

    :param L1: a list object
    :param L2: a list object
    :return: Returns a list without duplicates that is the intersection of L1 and L2
    '''
    temp = []  # a list storing all common elements
    for e1 in L1:  # for each element in L1 ...
        for e2 in L2:  # and for each element in L2
            if e1 == e2:  # if e1 == e2
                temp.append(e1)  # append e1 to the temp list
                break  # break inner for loop

    res = []  # res var to contain only distinct values
    for elem in temp:  # for each element in temp
        if elem not in res:  # if element is not in res
            res.append(elem)  # append such element to result
    return res

# Generating a Power Set on page 146
def getBinaryRep(n : int, numDigits :int) -> str:
    '''

    :param n: a non negative int object
    :param numDigits: a non negative int object
    :return: Returns a str of length numDigits that is a binary representation of n
    '''
    result = ''  # var to store result
    while n > 0:  # while n is greater than 0
        result = str(n % 2) + result  # get the binary rep of n by using n % 2
        n = n // 2  # update n by floor dividing it by 2

    if len(result) > numDigits:  # if the length of the the result is greater than numDigits ...
        raise ValueError("not enough digits")  # ... raise a Value

    for i in range(numDigits - len(result)):  # for i in the range of the difference btwn numDigits and len of result
        result = '0' + result  # fill the result with trailing zeros

    return result

def genPowerset(L : list) -> list:
    '''

    :param L: a list
    :return: Returns a list of lists that contains all possible combinations of the elements of L
    E.g., if L is [1, 2] --> [ [], [1], [2], [1,2] ]
    '''

    power_set = []  # var to hold power set
    for i in range(2**len(L)):  # for i in range 2^len(L) (i.e there can be 2^n subsets in a list of n elements)
        binStr = getBinaryRep(i, len(L))  # binary rep of i (i.e 0 and 1 represents absence and presence respectively
        subset = []  # var to hold sub set
        for j in range(len(L)):  # for j in range of len of the list ...
            if binStr[j] == '1':  # if the binary string @ j is 1
                subset.append(L[j])  # append List at j to the subset
        power_set.append(subset)  # append subset to powe_set

    return power_set  # return the power set

# genPowerset Function Invocation
print(genPowerset(['s', 'a', 'm', 'e']))
