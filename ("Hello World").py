
""""name = 'George Washington'
print('The first president of USA is' + name)

country = 'Great britain'
capital = 'London'
print(capital + ' is the capital of ' + country + '!')

brand = 'Apple'
product = 'iPhone'
model = '13 Pro Max'
price = '1500$'
print('Brand: ' + brand)
print('Product: ' + product)
print('Model: ' + model)
print('Price: ' + price)

number = 5
print(number**3)

almaty = 1927700
astana = 1228800
print('Total =', almaty + astana)

soup = 850
salad = 530
tea = 245
print('TO PAY:')
print('Soup -', soup)
print('Salad -', salad)
print('Tea -',tea)
print('- - -')
print('Total -',soup + salad + tea)


a = 80.5
b = 55.7
print ((a+b)/2)

distance = 2703
print(distance/5, 'km per day')

a = 14940
b = 0.12
print('Tax is',a*b,'dollars')

#text = input()
#text2 = input()
#print('Country: ' + text)
#print('City: ' + text2)

#T = 6*'R'
#R = 1
#text = input ()
#print(T*R)

a = int(input ())
b = int (input())

if a > b:
    print(a)
else:
    print(b)


n = int(input())
if n>=10 and n<=20:
	print("Yes")
else:
    print("No")


n = int(input())
if n%2==0:
    print("EVEN")
else:
    print("ODD")


n = int(input())
if n == 1:
    print('Monday')
if n == 2:
    print("Tuesday")
if n == 3:
    print("Wendsday")
if n == 4:
    print("Thursday")
if n == 5:
    print("Friday")
if n == 6:
    print("Sadurday")
if n == 7:
    print("Sunday")


n = int(input())
if n>100 or n<-100:
    print('0')
else:
    print(n+1)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a%2==0 and a>b and a>c and a>d:
    print(a)
elif b%2==0 and b>a and b>c and b>d:
    print(b)
elif c%2==0 and c>a and c>b and c>d:
    print(c)
elif d%2==0 and d>a and d>b and d>c:
    print(d)
else:
	print('Not Found')


a = int(input())
b = int(input())
c = int(input())
if a == b and b == c and c == a:
    print('YES')
else:
    print('NO')


a = int(input())
b = int(input())
c = int(input())
if a>10 and a%5==0:
    print("Yes")
elif b>10 and b%5==0:
    print("Yes")
elif c>10 and b%5==0:
    print("Yes")
else:
    print("NO")

n = int(input())
if n>0:
    print(n+1)
elif n<0:
    print(n-2)
elif n==0:
    print(10)

   



a = int(input())
b = int(input())
if a!=b:
	print((a+b),(b+a))
if a==b:
	print((a*0),(b*0))
__________
a = int(input())
b = int(input())
if a!=b:
    a = a + b
    b = a
else:
    a = 0
    b = 0
print(a)
print(b)


a = int(input())
b = int(input())
c = int(input())
if a > 10 and a%5==0 and b>10 and b%5==0 and c > 10 and c%5==0:
        print("Yes")
else:
        print("NO")

a = int(input())
b = int(input())
print("YES" if a - b == 100 or b -a ==100 else "NO")

a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
    print(a)
if b>a and b>c:
    print(b)
if c>a and c>b:
    print(c)

a = int(input())
b = int(input())
print ("Yes" if a <=12 and a>=1 and b <=2022 and b >=1 else "No")

a = int(input())
b = int(input())
c = int(input())
print ("Yes" if (a**2+b**2 == c**2) else"No")

a = int(input())
b = int(input())
c = int(input())
if a > b and a> c and b<c:
    print(a-b)
elif a>b and b>c and b>c:
    print(a-c)
elif b>a and b>c and a<c:
    print(b-a)
elif b>a and b>c and a>c:
    print(b-c)
elif c>a and c>b and b<a:
    print(c-b)
elif c>a and c>b and b>a:
    print(c-a)


a = int(input())
b = int(input())
c = int(input())
print("Yes" if a==b or a==c or b==c else ("No"))

n = int(input())
if n >20:
    print(n/6)
else:
    print(n*6)

n = int(input())
if n>0:
    print(n+1)
else:
    print(n)


a = int(input())
b = int(input())
if a%b==0:
    print("divisible")
else:
    print("not divisible")

a = int(input())
if a >=1 and a <=5:
    print(a+10)
elif a>=10 and a<=20:
    print(a-5)
elif a<0 or a>1000:
    print(a*3)
else:
    print(0)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a>5 and b>5 and c>5 and d>5 and b%4==0 and d/3:
    print("Yes")
else:
    print("No")

a = int(input())
b = int(input())
if a>b:
    print("Yes")
else:
    print(b)
    print(a)

n = int(input())
if n == 1:
    print('January')
if n == 2:
    print("February")
if n == 3:
    print("March")
if n == 4:
    print("April")
if n == 5:
    print("May")
if n == 6:
    print("June")
if n == 7:
    print("July")
if n == 8:
    print("August")
if n == 9:
    print("September")
if n == 10:
    print("October")
if n == 11:
    print("November")
if n == 12:
    print("December")


a = int(input())
if a%4==0 and a%100!=0 or a%400==0:
    print("Yes")
else:
    print("No")


Login = str(input())
Password = str(input())
if Login == 'user' and Password == 'qwerty':
    print("Authentification completed")
else:
    print("Invalid login or password")


a = int(input())
b = 6
print(a * b)


a = str(input())
b = 145900
c = 8
d = 142854
e = 5.8
if a == 'P&G':
    print('145900')
    print('8')
    print("Company Procter and Gamble earns",b/c,"dollars in a month")
if a == 'AirAstana':
    print('1142854')
    print('5.8')
    print("Company AirAstana earns",d/e,"dollars in a month")


text = str(input())
print('Name:',text)
text = str(input())
print('Surname:',text)
text = int(input())
print('Age:',text)
text = str(input())
print('Country:',text)


a = int(input())
b = int(input())
c = int(input())
if a+b>c:
    print(True)
else:
    print(False)

L = int(input())
b = 100
print(L//b)

R = int(input())
print(2*3.14*R)
print(3.14*(R**2))


a = int(input())
b = int(input())
from math import sqrt
if a>0 and b>0:
    print(sqrt(a*b))
else:
    print('Error')


x = int(input())
print(4*(x-3)-7*(x-3)+2)


a = int(input())
b = int(input())
c = int(input())
print(a*b*c)
print(2*(a*b+b*c+a*c))


x = int(input())
y = int(input())
z = int(input())
print(x**4+4*x*y**2-4*y*z+z**4)


a = int(input())
b = int(input())
c = int(input())
print(a*2+b-3+c**2)

a = int(input())
b = int(input())
c = int(input())
print(a+b)
print(c-a)
print(a+b+c)

a = 0
while a<10:
    print("Hello, World!")
    a+=1


x = int(input())
a = 0
while a<10:
    print(x)
    a+=1


x = 1
a = int(input())
for a in range(a):
    print(a+1)


a = int(input())
for i in range(a+1):
    if i % 2 == 1:
        print(i, end=" ")


n = int(input())
m = int(input())
for i in range (n, m+1):
    if i%2!=0:
        print(i, end=" ")

n = int(input())
m = int(input())
for i in range (n, m+1):
    if i%3==0:
        print(i, end=" ")


n = int(input())
m = int(input())
sum = 0
for i in range (n, m+1):
    sum = sum + i
print(sum)


n = int(input())
ans = 0
k = 3
for i in range(n):
    ans=ans+k
    k=k+3
print(ans)


m = 0
while True:
    n=int(input( ))
    m = m + 1
    if n==0:
        m = m- 1
        print(m)
        break

a = int(input())
for i in range(1,a+1):
    print(i,end=" ")



mx = 0
while True:
    n=int(input())
    if n!=0:
        if mx<n:
            mx = n
    if n==0:
     break
print(mx)


n = int(input())
m = int(input())
for i in range(n,m+1):
    print(i,end=" ")


n = int(input())
for i in range(0,n+1):
        if i%2==0:
            print(i,end=" ")


n = int(input())
m = int(input())
for i in range(n,m+1):
    if i%2==0:
        print(i,end=" ")

n = int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")


N = int(input())
for i in range(1,N+1):
    print(i,i**2)


n = int(input())
sum = 0
for i in range(1,n+1):
    sum = sum+i
print(sum)


n = int(input())
sum=0
for i in range(1,n+n,2):
    sum=sum+i
print(sum)

n = int(input())
m = int(input())
sum=0
for i in range(n, m + 1):
    if i % 2 == 0:
        sum = sum + i
print(sum)

n = int(input())
m = int(input())
count=0
for i in range(n,m+1):
    if i%2==0:
        count=count+1
print(count)

n= int(input())
m= int(input())
sum = 0
count = 0

for i in range(n,m+1):
    sum=sum+i
    count=count+1
print(sum/count)


N = int(input())
a = 1
while True:
    N = int(input())
    a = a + N
    if N==0:
        break
print(a)


n = int(input())
sum = 1
k = 0
while True:
    n=int(input())
    k=k+1
    sum=sum+n
    m=sum//k
    if n==0:
        break
print(m)


n = int(input())
f = 1
for i in range(1,n+1):
    f = f*i
print(f)

nums = [6,19,26,9,46,8,5,65,90,25]
n=int(input())
print(nums[n])


n = int(input())
arr = list(map(int, input().split()[:n]))
for i in arr:
    print(i**2, end=" ")


n = int
a = 0
while n!=0:
    n=int(input())
    if n%2!=0: #если остаток деления n на 2 не равняется 0
        a=a+n #новая "а"=старая"а"+n
print(a)


n = int(input())
sum=0
for i in range(1,n+1):
    sum = sum+i*i
print(sum)


n = int(input()) #кол-во символов в массиве
arr = list(map(int, input().split()[:n]))

# input() возвращает строку (например: "1 2 3")
# split() преобразует строку в list по разделителю -
#по умолчанию это пробел (результат: ["1", "2" ,"3"])
# map преобразует список в соответствие с функцией -
#в данном случае int(elem) (результат: [1, 2 , 3]

for i in arr:
    if i%2==0: print(i, end=" ")

n=int(input())
arr = list(map(int, input().split()[:n]))
for i in arr:#для функции i в массиве arr
    if i%2==0: #если остаток деления функции на 2 равен 0
        print(i, end=" ") #вывести значения функции i у которых остаток деления на 2 = 0

n=int(input())
arr = list(map(int, input().split()[:n]))
c = 0 #кол-во элементов в массиве
for i in arr: #для функции i в массиве arr
    if i>0:
        c = c+1 #кол-во элементов в массиве, значения которого больше 0
print(c, end=" ")


n=int(input())
arr = list(map(int, input().split()[:n]))
c = 0
for i in arr:
    c=c+i #новая С = старая С + i(элемент массива)
print(c)


n = int(input())
arr = list(map(int, input().split()[:n]))
for i in range(len(arr)):
#for i in range( ) - только числвове значение;
#for i in range(len( )) - бежать по всей длине массива. По индексам(i)
    if i%2==0:
        print(arr[i], end=" ")


n = int(input())
arr = list(map(int, input().split()[:n]))
mx = arr[0] #допустим что самый минимальный элемент массива - это максимальный
                #далее начинаем сравнивать минимальный элемент с остальными элементами
                #тем самым, если вводимый элемент больше максимального, то он становится новым максимумом
index = 0
for i in range(len(arr)):
        if arr[i] > mx:
                mx=arr[i]
                index = i
print(mx,index)


n = int(input())
arr = list(map(int, input().split()[:n]))
c=1
for i in range(len(arr)):
        if arr[i]!=0:
                c =c*arr[i] #формула умножения элемента не равного 0 на след. элемент
print(c)


n = int(input())
arr = list(map(int, input().split()[:n]))
mx = arr[0]
mn = arr[0]
for i in range(len(arr)):
        if arr[i] > mx:
                mx=arr[i]
        if arr[i]<mn:
                mn=arr[i]
print(mn,mx)


n = int(input())
arr = list(map(int, input().split()[:n]))

for i in range(len(arr)):

        print(i,"-",arr[i])


n = int(input())
arr = list(map(int, input().split()[:n]))
for i in range(len(arr)):
        print(arr[len(arr) - i - 1], end=" ")#print(arr[len(arr) - i - 1] выводит массив в обратном порялке



n = int(input())
arr = list(map(int, input().split()[:n]))
for i in range(len(arr)): #по индексам
        if i%2!=0:
                print(arr[i], end= " ")



#Напишите программу, которая запрашивает дробные числа (double d). Программа должна остановиться запрашивать,
# когда мы вводим 0. Программа должна вывести умножение всех введенных чисел.
N = float
a = 1
while True:
        N = float(input())

        if N == 0:
                break
        a = a * N
        print(a)


n = int(input())
arr = list(map(int, input().split()[:n]))
for i in arr:
    if i > 0:
        print(i,end=" ")


n = int(input()#Программа запрашивает число n. Далее, мы вводим n чисел и
                # сохраняем все введенные числа в массив.
                # Программа должна вывести сумму и среднее значение введенных чисел.
arr = list(map(int, input().split()[:n]))
c = 0
k = 0 #кол-во элементов в массиве
for i in arr:
    c = c + i #формула сложения элементов
    k = k + 1
    m = c/k #формула сложения/ кол-во элементов = ср. арифмет.
print(c,m,end=" ")


#Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем
# все введенные числа в массив.
# Выведите в конце разность между максимальным и минимальными элементами.
n = int(input())
arr = list(map(int, input().split()[:n]))
mx = arr[0]
mn = arr[0]
for i in range(len(arr)):
    if arr[i]>mx:
        mx = arr[i]
    if arr[i]<mn:
        mn = arr[i]
print(mx-mn,end=" ")

!!! 88888888888888
n = int(input())
arr = list(map(int, input().split()[:n]))
c = 0
k = 0
mx = arr[0]
mn = arr[0]

##Выводим сумму всей последовательности
for i in arr:
    c = c + i
    k = k + 1
for i in range(len(arr)):
    if arr[i]>mx:
        mx = arr[i]
    if arr[i]<mn:
        mn = arr[i]
##Удаляем наименьший и наибольший элемент
arr.pop(arr.index(mx))
arr.pop(arr.index(mn))
##Выводим среднее арифмитическое
print(c,c/k)
!!!


#Программа запрашивает число n.
#Далее, мы вводим n чисел и сохраняем все введенные числа в массив.
#Программа должна заменить местами максимальный и минимальный элементы.
n = int(input())
arr = list(map(int, input().split()[:n]))
max=0
min=0
for i in  range(len(arr)):
   if arr[i]>arr[max]:
       max=i #максимальный элемент
   if arr[i] < arr[min]:
       min=i #минимальный элемент

arr[min],arr[max] = arr[max],arr[min] #формула чтобы поменять местами макс и мин
for i in range(len(arr)):
    print(arr[i], end=' ')





n = int(input())
arr = list(map(int, input().split()[:n]))
c = 0
k = 0

for i in range(len(arr)):
    if arr[i]<0:
        c = c + arr[i]
        k = k + 1
        m = c / k
print(m,end=" ")

text = 'BITLAB'
text2 = str(input())
if text2==text:
    print("Yes")
else:
    print("No")


#Напишите программу которая принимает текст и сранивает его со словом "python".
#Если они равны без учета регистров (заглавные и строчные буквы) выведите "YES", иначе "NO"
text = "python".upper()
text2 = input().upper()
if text2==text:
    print("Yes")
else:
    print("No")

text = input()
for i in range(len(text)):
    print(text[i])

text= input()
for i in range(len(text)):
    print(text[i]*2,end="")


#Программа должна принимать текст и букву, затем подсчитать сколько раз буква встречается в тексте.
text = input().upper()
text2 = input().upper()
c=0
for i in range(len(text)):
    if text2==text[i]: # если значение текст2= какомулибо значению текста
        c=c+1 #включается формула подсчета данного элемента. Сколько раз он появляется в строке
print(c)


#Напишите программу которая показывает принятый текст в обратном порядке.
text = input()
for i in range(len(text)):
    print(text[len(text)-i-1], end ="")

s1 = input()
s2 = input()
if s1.__contains__(s2):
        print("YES")
else:
        print("NO")


#Мы вводим строку (текст) в нашу программу.
#Программа должна вывести количество гласных букв. (Гласные буквы: a, e, i, o, u)
text = input()
char = 'aeiuo'
c = 0
for i in range(len(text)):
    if text[i] in char:
        c = c+1
print(c)



#Напишите программу которая выводит сумму всех цифр в тексте.
n = input()
suma = 0
for digit in n:
    if digit.isdigit():
        suma =suma+ int(digit)
print(suma)


#Мы вводим строку (текст) в нашу программу. Программа должна определить,
# является ли наш текст "Палиндром"-ом или нет.
# Палиндром - это когда текст читается так же одинаково если ее читать в обратном порядке.
text = input().upper()
while text[::-1]==text[0:]:
    print("YES")
    break
else: print( "NO")



#Ваша задача вывести данные тех сотрудников, у которых зарплата больше 350000.
employee =[
    {"id": 1, "name": "Emily", "age": 35, "salary": 500000},
    {"id": 1, "name": "Jack", "age": 46, "salary": 450000},
    {"id": 1, "name": "Tom", "age": 29, "salary": 350000},
    {"id": 1, "name": "Fin", "age": 31, "salary": 400000},
    {"id": 1, "name": "Amanda", "age": 24, "salary": 250000},
    {"id": 1, "name": "Kate", "age": 30, "salary": 340000}
]


for i in employee:
    if i["salary"] > 350000:
        print(i["name"])


#Программа запрашивает логин и пароль пользователя,
#если данные введены правильно и они совпадают,
#то программа выведет сообщение “Hello, ” и имя пользователя, иначе “Try again”.
users = {
    "user1": {"id": 1, "name": "Emily", "login": "emily@gmail.com", "password": "qwerty"},
    "user2": {"id": 2, "name": "Jack", "login": "jack@gmail.com", "password": "qwerty2"},
    "user3": {"id": 3, "name": "Tom", "login": "tom@gmail.com", "password": "qwerty3"}
}


login = input()
password = input()
for i in users.values():
    if login==i["login"] and password == i["password"]:
        print("Hello "+ i[ 'name'])
        break
    else:
        print("Try again")

l = input()
p = input()
for i in users.keys():
    if users[i]["login"] == l and users[i]["password"] == p:
        print("Hello "+users[i]["name"])
    else:
    print("Try again")


#Ниже представлена корзина продуктов пользователя.
#Ваша задача найти сумму, которую пользователь должен оплатить.
#(Цена указана для одного продукта, учитывайте количество тоже)
cart = {
 "orderID": 12345,
 "shopperName": "Ilyas Zhuanyshov",
 "shopperEmail": "ilyas@gmail.com",
 "products": [
   {
     "productID": 34,
     "productName": "apple",
     "price": 100,
     "quantity": 2
   },
   {
     "productID": 56,
     "productName": "banana",
     "price": 300,
     "quantity": 3
   },
  {
   "productID": 56,
   "productName": "ice-cream",
   "price": 1000,
   "quantity": 2
  },
  {
   "productID": 56,
   "productName": "cake",
   "price": 4000,
   "quantity": 1
  }
 ]
}
t = 0
q = 1
total = 0
for i in cart.get(('products'[:])):
    print (i["productName"])
    print(i["quantity"])
    print(i["price"])
    print(i)
    q = i["quantity"]*i["price"]
    total = total + q
    print(total)


#Даны два списка. Напишите программу для преобразования их в словарь таким образом,
#чтобы элемент из списка 1 был ключом, а элемент из списка 2 - значением
keys = ['Десять', 'Двадцать', 'Тридцать']
values = [10, 20, 30]
#Вывод:
#{'Десять': 10, 'Двадцать': 20, 'Тридцать': 30}
#dict = {'Десять':'10', 'Двадцать':'20','Тридцать':'30'}
#print(dict)
#print("__________")
#d = dict.fromkeys(['10','20','30'], Десять, Двадцать, Тридцать)
#print(d)

d = dict.fromkeys(keys, values)
print(d)


#С консоли примите два числа N и M, и покажите на экране значение которое хранится по этому индексу
n = int(input())
m = int(input())
a = [[12,5,7,6],[4,0,2,7],[9,1,3,2],[10,-2,4,6]]
print(a[n][m])


#Создайте двумерный массив размером 2xN из целых чисел и
# с помощью цикла выведите элементы каждого одномерного массива в отдельной строке

n = int(input())
arr = list(map(int, input().split()))
arr1 = []
arr2 = []
for i in range(n):
    arr1.append(arr[i])

for i in range(n, len(arr)):
    arr2.append(arr[i])

arr = [arr1,arr2]
for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()
"""

b = input().split()
n = int(b[0])
m = int(b[1])
arr = []

for i in range(n):
    b = list(map(int,input().split()))
    arr.append(b)

k = int(input())
# a = [[1, 6, 10],
#      [2, 5, 9]]
# for i in range(len(arr[k])):
#     print(arr[k][i])
for elem in arr[k]:
    print(elem, end = " ")