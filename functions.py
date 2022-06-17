"""'''
def mx(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = int(input())
b = int(input())
c = int(input())
print(mx(a,b,c))


def find_Triangle(a,b,c):
    if a + b >c and b + c> a and a + c > b:
        return "YES"
    else:
        return "NO"
a = int(input())
b = int(input())
c = int(input())
print(find_Triangle(a,b,c,))


def countLetter(a,b):
    count = 0
    for i in range(len(a)):
        if a[i] == b:
            count += 1
    return count

a = input().upper()
b = input().upper()
print(countLetter(a,b))


def count_glasnie_bukvi(text):
    count = 0
    char = 'aeiou'
    for i in range(len(text)):
        if text[i] in char:
            count += 1
    return count

text = input()
print(count_glasnie_bukvi(text))


def contains_words(text1,text2):
    if text1.__contains__(text2):
        return "YES"
    else:
        return "NO"

s1 = input().lower()
s2 = input().lower()
print(contains_words(s1,s2))


def count_elem_non_zero(*arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            count += 1
    return count

n = int(input())
a = list(map(int, input().split()[:n]))
print(count_elem_non_zero(*a))


def mn_and_mx_in_array(arr):
    mn = arr[0]
    mx = arr[0]
    for i in range(len(arr)):
        if mx < arr[i]:
            mx = arr[i]
        elif mn > arr[i]:
            mn = arr[i]
    return [mn, mx]

n = int(input())
a = list(map(int, input().split()[:n]))
print(mn_and_mx_in_array(a)[0])
print(mn_and_mx_in_array(a)[1])


def sum_elem_no_5(arr):
    su = 0
    for i in range(len(arr)):
        if arr[i] % 5 != 0:
            su = su + arr[i]
    return su
n = int(input())
a = list(map(int, input().split()[:n]))
print(sum_elem_no_5(a))


def sum_elem_less_than_11(arr):
    s = 0
    for i in range(len(arr)):
        if arr[i] < 11 and arr[i] % 2 == 0:
            s += arr[i]
    return s

n = int(input())
x = list(map(int, input().split()[:n]))
print(sum_elem_less_than_11(x))





def s_greater_than_m_change(list,m):
    s = 0
    for i in range(len(list)):
        s += list[i]

    for i in range(len(list)):
        if list[i] > m:
            list[i] = s

n = int(input())
a = list(map(int, input(). split()[:n]))
m = int(input())
print(s_greater_than_m_change(a,m))


def div_2(n):
    if n % 2 == 0:
        return "Yes"
    else:
        return "NO"
n = int(input())
print(div_2(n))


def find_paliandr(text):
    if text == text[::-1]:
        return "YES"
    else:
        return "NO"
a = input()
print(find_paliandr(a))

#DOUBLE_LETTER
a = input()
def dbl_letter(a):
    s = ""
    for i in a:
        s = s + i*2
    return s

print(dbl_letter(a))


# ЗАДАНИЕ 10
def unique_elem(a):
    ans = []
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
                break
        else:
            ans.append(a[i])
    return ans
n = int(input())
a = list(map(int, input().split()[:n]))
x = unique_elem(a)
for i in x:
    print(i, end = " ")

class Phone:
    name = ""
    model = ""
    price = 0
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    def getData(self):
        return self.name, self.model, self.price


p1 = Phone("iPhone", "12", 500000)
p2 = Phone("Nokia", "3310", 10000)
p3 = Phone("Samsung", "Galaxy S", 500000)
p4 = Phone("Sony", "Sony Erixson", 15000)
p5 = Phone("Nokia", "8800",100000 )

phoneList = [p1, p2, p3, p4, p5]
for p in phoneList:
    print(p.getData(), end = ", ")



from Class import Student

s1 = Student(20221, "Aziz", 'Imangazin', 3)
s2 = Student(20222, 'Ivan', 'Ivanov', 1.5)
s3 = Student(20223, 'Alex', 'Shmak', 3)
s4 = Student(20224, 'Elon', 'Musk', 4)
s5 = Student(20225, 'Misha', 'Krug', 2)

sList = [s1, s2, s3, s4, s5]

#maxGpa = 0
#ind = 0

#for s in range(len(sList)):
 #   if maxGpa < sList[s].gpa :
  #     maxGpa = sList[s].gpa
   #     ind = s
#print(sList[ind].getStudentData())



from Class import Student1

s1 = Student1("Aziz", 'Imangazin', 3.0)

studList = [s1]
while True:
   n = int(input(''''PRESS [1] TO ADD STUDENT:\nPRESS [2] TO LIST STUDENTS: \nPRESS [0] TO EXIT:\n''''))
    if n == 1:
        a1 = str(input('Insert name: ', ))
        b1 = str(input('Insert surname:', ))
        c1 = float(input('Insert GPA: ', ))
        newStudent = Student1(a1,b1,c1)
        studList.append(newStudent)

    elif n == 2:
        for i in studList:
            print(i.getStudentData())

    else:
        break



#Задание 7
from Class import Employee
from Class import Programmer
from Class import DataAnalitic

p1 = Programmer('Elon', 27, 100000, 'Python')
p2 = Programmer('Ember', 35, 0, 'Pascal')

d1 = DataAnalitic('Tom', 50, 200000, 'tool 1')
d2 = DataAnalitic('Jerry', 45, 400000, 'tool 2')

e = [p1, p2, d1, d2]
sal = 0
k = 0
for i in range(len(e)):
    if sal < e[i].salary:
        sal = e[i].salary
        k = k + sal
    print(e[i].getEmployeeData())
print('среднее значение:',k / len(e))



#Исключения

n = input('Первое Значение:')
m = input('Второе Значение:')
try:
    print(float(n) + float(m))
except ValueError:
    print(n+m)


n = input('Insert your phone number:')
try:
    print("We will contact you by phone number:",int(n))
except ValueError:
    if n != int():
        print('Phone number can contain only digits!')


a = []
while True:
    n = int(input())
    if n == 0:
        break
    a.append(n)

m = int(input('insert index:'))

try:
    print(a[m])
except:
    print('There is no such element')


from Class import Book
b1 = Book(1, 'Title1', 'author1', 100)
b2 = Book(2, 'Title2', 'author2', 200)
b3 = Book(3, 'Title3', 'author3', 300)
b4 = Book(4, 'Title4', 'author4', 400)
b5 = None

b = [b5, b1, b2, b3, b4]

for i in b:
    try:
        print(i.getBookData())
    except:
        print('Book is empty')


from Class import User

u = []

for i in range(5):
    try:
        name = input('Insert name:')
        surname = input('Insert surname:')
        age = int(input('Insert age:'))
    except ValueError:
        age = 0

    u1 = User(name, surname, age)
    u.append(u1)

for i in range(len(u)):
    k = 0
    c = 0
    k += u[i].age
    c += 1
print(k/c)


class Student:
    id = 0
    name = ""
    surname = ""
    gpa = 0
    students = []

    def __init__(self, id, name, surname, gpa):
        self.id = id
        self.name = name
        self.surname = surname
        self.gpa = gpa

    def getStudentData(self):
        return self.id, self.name, self.surname, self.gpa

def getTopStudents(students):
    ind = 0
    mxGpa = 0
    for i in range(len(students)):
        if mxGpa < students[i].gpa:
            mxGpa = students[i].gpa
            ind = i
    return students[ind].getStudentData()


s1 = Student(20221, "Aziz", 'Imangazin', 3)
s2 = Student(20222, 'Ivan', 'Ivanov', 1.5)
s3 = Student(20223, 'Alex', 'Shmak', 3)
s4 = Student(20224, 'Elon', 'Musk', 4)
s5 = Student(20225, 'Misha', 'Krug', 2)

sList = [s1, s2, s3, s4, s5]

print(getTopStudents(sList))





class User:
    name = ''
    surname = ''
    age = 0

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def getUserData(self):
        return self.name, self.surname, self.age

u = []

for i in range(5):
    try:
        name = input('Insert name:')
        surname = input('Insert surname:')
        age = int(input('Insert age:'))
    except ValueError:
        age = 0

    u1 = User(name, surname, age)
    u.append(u1)

k = 0
c = 0

for i in range(len(u)):
    k += u[i].age
    c += 1
print(k/c)


from Class import Car
from Class import Toyota
from Class import Mercedes

c1 = Car('car1', 'model1', 180, 2000, 3.0)
t1 = Toyota('toyota', 'camry', 180, 2020, 3.0, 'Japan')
m1 = Mercedes('mercedes', 'g-500', 270, 2020, 5.5, 'g-class')
c1.ride()
t1.ride()
m1.ride()



def find_mx(arr):
    for i in range(len(arr)):
        mx = 0
        for j in range(len(arr[i])):
            arr[i][j] = int(arr[i][j])
            if mx < arr[i][j]:
                mx = arr[i][j]
        print(mx)

n = int(input())
m = int(input())
arr = []
for i in range(n):
    arr.append(input().split())

find_mx(arr)



def odds(arr):
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            if arr[i] == 23:
                break
            print(arr[i])

n = int(input())
a = list(map(int, input(). split()[:n]))
odds(a)



def lessThan50andDivides5(arr):
    for i in range(len(arr)):
        if arr[i] % 5 == 0 and arr[i] < 50:
            print(arr[i])

n = int(input())
a = list(map(int, input(). split()[:n]))
lessThan50andDivides5(a)



def seasons(n):
    if n == 1 or n == 2 or n == 12:
        return "Winter"
    elif n == 3 or n == 4 or n == 5:
        return "Spring"
    elif n == 6 or n == 7 or n == 8:
        return "Summer"
    elif n == 9 or n == 10 or n == 11:
        return "Autumn"

n = int(input())
print(seasons(n))


def changeMxAndMn(arr):
    mn = 0
    mx = 0
    for i in range(len(arr)):
        if arr[mx] <arr[i]:
            mx = i
        if arr[mn] > arr[i]:
            mn = i
    arr[mn], arr[mx] = arr[mx], arr[mn]
    return arr

n = int(input())
a = list(map(int, input().split()[:n]))
x = changeMxAndMn(a)
for i in x:
    print(i, end = ' ')



def sum_mx_mn(arr):
    mx = 0
    mn = 99999
    for i in range(len(arr)):
        if mx < arr[i]:
            mx = arr[i]
        if mn > arr[i]:
            mn = arr[i]
    return mx + mn

n = int(input())
a = list(map(int, input().split()[:n]))
mx = 0
mn = 9999
print(sum_mx_mn(a))


def numbers(n,m):
    if n % 2 == 0 and m % 2 ==0:
        return n*m
    elif n % 2 !=0 and m % 2 !=0:
        return n+m
    elif n % 2 ==0 and m % 2!=0:
        return m
    elif m % 2 ==0 and n % 2!=0:
        return n

print(numbers(20,12))
print(numbers(13,20))


def numbers(a):
    m = int(input())
    for i in range(len(a)):
        if a[i] == i:
            if a[i] % m != 0:
                print(a[i])

n = int(input())
a = list(map(int, input().split()[:n]))
numbers(a)
"""


