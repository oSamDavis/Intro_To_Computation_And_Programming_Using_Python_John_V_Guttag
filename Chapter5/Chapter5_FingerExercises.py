# Repetition on tuples :
print(3 * ("a", 45))

# Function that finds similar elements in two tuples t1 and t2
def intersect(t1, t2):
    result = ()
    for e in t1:  # for every element in t1
        if e in t2:  # if such element is in t2
            result += e  # add such an element to the result tuple
    return result  # return the result

# Function that finds extreme divisors of two numbers
def findExtremeDivisor(n1, n2):  # finding extreme divisors of two numbers
    minVal, maxVal = None, None  # firstly initialize both to min and max Value to None
    for i in range(2, min(n1,n2) + 1):  # starting @ 2 to the minimum of the two numbers...
        if n1 % i == 0 and n2 % i == 0:  # if i is a common divisor of the two numbers ...
            if minVal is None:  # if minVal is None ...
                minVal = i  # ... then initialize min val with i
            maxVal = i  # let maxVal be equal to i
        return (minVal, maxVal)

# Function to remove dublicates in a list
def removeDups(L1,L2):
    '''

    :param L1: A List Object
    :param L2: A List Object
    Removes any element from L1 that also occurs in L2
    :return: None
    '''

    for e in L1[:]:  # iterating over a cloned version of L1
        if e in L2:
            L1.remove(e)


L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
removeDups(L1, L2)
print("L1 =", L1)

# Intro to Higher Order Functions : Functions that have functions as arguments
def applyToEach(f, L):
    '''
    :param f: a function
    :param L: a list
    Mutates L by replacing each element, e, of L by f(e)
    :return: None
    '''
    for i in range(len(L)):
        L[i] = f(L[i])


L3 = [1, -2, -3.33]
print("L3 =", L3)
print("Applying abs to each element of L3 ...")
applyToEach(abs, L3)
print("L3 is now = ", L3)


# Intro to in built higher order function: map
print("Higher Order Function : MAP")
print("\n Applying absolute...")
for i in map(abs, [-6, -8, -10]):  # map applies the func abs to the list [-6, -8, -10]
    print(i)

L4 = [43, 57, 12]
L5 = [2, 10, 55]
print("\n Applying max in two lists")
for i in map(min, L4, L5):
    print(i)

# Lamda Expression
L6 = []
for i in map(lambda x, y: x**y, [1, 2, 3, 4], [3, 2, 1, 0]):  # labda expression
    L6.append(i)
print(L6)

# Using the built in split function:
string = "Doyin,Acapella,Funsho,Liam,Ian,Brian"
print(string.split(","))

# Dictionaries

my_first_dict = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6}  # month / monthNumbers Pair
print("February occurs as Month Number ", my_first_dict["Feb"])
dist = my_first_dict["Jun"] - my_first_dict["Feb"]
print("June and February are", dist, "Months apart")

my_first_dict["July"] = 7

