import datetime

# My first Python Class : The class Int Set

class IntSet(object):
    '''
    IntSet => a set of integers, Duplicates not contained
    '''
    # value of a set is represented by a list of ints, self.vals.
    # Each int in the set occurs in self.vals exactly once

    def __init__(self):
        '''
        Create an empty set of integers
        '''
        self.values = []

    def insert(self, element):
        '''
        element : int
        inserts e into the set(self)
        :return: None
        '''

        if element not in self.values:
            self.values.append(element)

    def isMember(self, element):
        '''

        :param element: an int
        Returns True if element is a member of the set(self)
        :return: Bool
        '''

        return element in self.values

    def remove(self, element):
        '''

        :param element: an int
        removes element from set, raises Value error if element isn't in set
        :return: None
        '''

        try:
            self.values.remove(element)
        except:
            raise ValueError(str(element) + " not found in set")

    def getMembers(self):
        '''

        :return: a list containing the elements of set(self)
        Nothing can be assumed about the order of elements
        '''
        return self.values[:]

    def __str__(self):
        '''

        :return: a string representation of self
        '''

        self.values.sort()
        result = ""
        for e in self.values:
            result += str(e) + ","
        return "{" + result[:-1] + "}"  # -1 excludes the trailing comma


# Testing my first class
my_set = IntSet()

my_set.insert(4)
my_set.insert(4)
my_set.insert(5)
my_set.insert(3)
my_set.insert(2)
my_set.insert(7)

print(my_set.getMembers())
print(my_set.isMember(3))
my_set.remove(7)
print(my_set)


# Person Class Page 116

class Person(object):
    def __init__(self, name):
        '''
        Creates a Person
        :param name: a str
        '''
        self.name = name
        try:
            lastBlank = name.rindex(' ')  # finds the last blank space
            self.lastname = name[lastBlank+1:]
        except:
            self.lastname = name
        self.birthday = None

    def getName(self):
        '''
        returns self's full Name
        :return: str
        '''
        return self.name

    def getLastName(self):
        '''
        returns self's last name
        :return: str
        '''
        return self.lastname

    def setBirthday(self, birthdate):
        '''
        Assumes birthdate is of type datetime.date
        Sets self's birthday to birthdate
        :return: None
        '''
        self.birthday = birthdate

    def getAge(self):
        '''
         Returns self's current age in days
        '''
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() -  self.birthday).days

    def __lt__(self, other):
        '''
        Returns True if self precedes other in alphabetical order, and False otherwise.
        Comparison is based on Last Names, but if Last names are the same, full names are compared
        '''

        if self.lastname == other.lastname:
            return self.name < other.name
        return self.lastname < other.lastname

    def __str__(self):
        '''

        Returns self's full name
        '''
        return self.name


# Testing my Person Class
print("----------------------------------- \n Testing Person Class")
me = Person("Sam Davis Omekara")
him = Person("Lionel Messi")
her = Person("Ngozi Okonjo-Iweala")
print(her.getLastName())
him.setBirthday(datetime.date(1987, 6, 24))
her.setBirthday(datetime.date(2954, 6, 13))
print(him, "is", him.getAge(), "days old")

person_list = [me, him, her]
for person in person_list:
    print(person)
print("---- sorted by last name ---------")
person_list.sort()
for person in person_list:
    print(person)


#  Learning Inheritance

class PSCPerson(Person):
    nextIdNum = 0  # class variable <-> Identification Number

    def __init__(self, name):
        Person.__init__(self, name)  # calls Parent __init__ function to initialize inherited var(i.e name)
        self.idNum = PSCPerson.nextIdNum
        PSCPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def isStudent(self):
        return isinstance(self, Student)

    def __lt__(self, other):
        return self.idNum < other.idNum


# Testing Inheritance Class
print("--------------------------------------")
print("Experimenting Inheritance ")
p1 = PSCPerson('Mark Joseph')
print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))

person1 = PSCPerson("John Dumelo")  # Creating(instantiating) a PSC Person
person2 = PSCPerson("Andrew Yung")  # Creating(instantiating) a PSC Person
person3 = PSCPerson("Andrew Yung")  # Creating(instantiating) a PSC Person
person4 = Person("Andrew Yung")  # # Creating(instantiating) a Person

print('person1 < person2', person1 < person2)  # comparing two PSC people(i.e id Numbers)
print('person3 < person2', person3 < person2)  # comparing two PSC people(i.e id Numbers)
print('person4 < person1', person4 < person1)  # comparing a Person with a PSCPerson(i.e id Last Name)


# Multiple Levels pf Inheritance
class Student(PSCPerson):
    def __init__(self, name, classYear):
        PSCPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

class Faculty(PSCPerson):
    def __init__(self, name, department):
        PSCPerson.__init__(self, name)
        self.faculty = department

    def getFaculty(self):
        return self.faculty


class CitizenStudent(Student):
    def __init__(self, name, classYear, state):
        Student.__init__(self, name, classYear)
        self.state = state

    def getState(self):
        return self.state

class InternationalStudent(Student):
    def __init__(self, name, classYear, country):
        Student.__init__(self, name, classYear)
        self.country = country

    def getCountry(self):
        return self.country


person5 = CitizenStudent("Tariq St.Patrick", 2022, 'North Carolina')
person6 = InternationalStudent("Adamu Adeyeye", 2021, 'Nigeria')
person7 = Faculty("Yeray Brown", 'Computer Science')

print(person5, 'is a citizen of USA is', type(person5) == CitizenStudent)
print(person6, 'is a citizen of USA is', type(person6) == CitizenStudent)

print(person5, 'is a student is', person5.isStudent())
print(person6, 'is a student is a ', person6.isStudent())
print(person7, 'is a student is a ', person7.isStudent())


# Grades Class
class Grades(object):

    def __init__(self):
        '''Creates an empty gradebook'''
        self.students = []  # a list of student
        self.grades = {}  # a dict that maps student id to list of grades
        self.isSorted = True  # var to keep track of whether or not students is sorted(avoids sorting extra cost)

    def addStudent(self, student):
        '''
        :param student: of type student
        Adds student to grade book
        :return: None
        '''

        if student in self.students:
            raise ValueError("Student already in grade Book")
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        '''

        :param student: a student
        :param grade: a float
        Adds grade to a list of grades for student
        :return: None
        '''

        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError("Student is not in grade book")

    def getGrades(self, student):
        '''

        :param student: a student
        :return: a list of student's grades
        '''

        try:
            return self.grades[student.getIdNum()][:]  # returns a vopy of student's grade
        except KeyError:
            raise ValueError("Student is not in grade book")

    # def getStudent(self):
    #     '''
    #
    #     :return:  a sorted list of students in grade book
    #     '''
    #
    #     if not self.isSorted:
    #         self.students.sort()
    #         self.isSorted = False
    #     return self.students[:]  # returns a copy of students

    def getStudent(self):  # get student function using Generator Instead
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s

def gradeReport(course : Grades):
    '''
    Assumes course is of type Grades
    :param course: of type Grades
    :return: a report of grades in a particulat course(a str)
    '''

    report = ''
    for student in course.getStudent():
        total = 0.0
        numofGrades = 0

        for grades in course.getGrades(student):
            total += grades
            numofGrades += 1

        try:
            average = total/numofGrades
            report += "\n" + str(student) + "\'s mean grade is " + str(average)
        except ZeroDivisionError:
            report += "\n" + str(student) + " has no grades"

    return report


# Testing Grades Class and GradeReport Function
print("------------------------------------------")
print("Testing Grade and Grade Report")
student1 = InternationalStudent("Shwrester Bwergen", 2023, 'Denmark')
student2 = CitizenStudent("Alan Smith", 2023, 'Kentucky')
student3 = CitizenStudent("Gabriel Brown", 2021, 'New York')
student4 = CitizenStudent("Kendall Tucker", 2020, 'South Dakota')
student5 = InternationalStudent("Betty Butter", 2024, 'Nigeria')

Intro_To_Comp_Sci = Grades()

Intro_To_Comp_Sci.addStudent(student1)
Intro_To_Comp_Sci.addStudent(student2)
Intro_To_Comp_Sci.addStudent(student3)

Intro_To_Comp_Sci.addStudent(student5)

for student in Intro_To_Comp_Sci.getStudent():
    Intro_To_Comp_Sci.addGrade(student, 87)

Intro_To_Comp_Sci.addGrade(student2, 89)
Intro_To_Comp_Sci.addGrade(student5, 99)

Intro_To_Comp_Sci.addStudent(student4)

print(gradeReport(Intro_To_Comp_Sci))


# Testing Encapsulation and Info Hiding
class InfoHiding(object):
    def __init__(self):
        self.visible_var = 'Look at me! Accessible'
        self.__anotherVisible_var__ = "Also Look at me now"
        self.__invisible_var = " John Cena-esque. You can't see me"

    def printVisible(self):
        print(self.visible_var)

    def printInvisible(self):
        print(self.__invisible_var)


