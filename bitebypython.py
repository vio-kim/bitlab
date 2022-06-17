"""age = 26
name = 'Swaroop'
print('Возраст {} -- {} лет.'.format(name, age))

#{0} и {1} через format означают: {0}=name, {1} = age
#команда format прописывать внутри print('asd'.FORMAT)

print('Почему {0} забавляется с этим Python?'.format(name))


n = input()
n_list = list(n)
print(n_list)
n_list.reverse()
print(n_list)
n2 = ''.join(n_list)
print(n2)

n = int(input())
k = 250
print(n*k)


a = int(input('Расход топлива на 100 км: '))
b1 = int(input('Стоимость АИ-92: '))
b2 = int(input('Стоимость АИ-95: '))
b3 = int(input('Стоимость АИ-98: '))
c = int(input('Бюджет: '))
print(c/b1*a, "км" )
print(c/b2*a, "км")
print(c/b3*a, "км")

a = int(input())
b = int(input())
c = int(input())
if a + b>c:
    print("True")
else:
    print("False")




num = int(input())
num1 = num//100
num2 = (num%100)//10
num3 = num%100%10
print(num1+num2+num3)



n = int(input())
if n % 2==0:
    print("EVEN")
else:
    print("ODD")




k = input()
d0 = 0
d1 = 1
d2 = 2
d3 = 3
d4 = 4
d5 = 5
d6 = 6
for k in range(1,366):
    if k %


n = int(input())
if n>0 and n%2==0:
    print("YES")
else:
    print("NO")

n = int(input())
m = int(input())
c = int(input())
if n<m and n<c:
    print(n)
elif m<n and m <c:
    print(m)
elif c<n and c<m:
    print(c)

a = int(input())
if a < 100 or a>200:
    print("Yes")
else:
    print("NO")

n = int(input())
if n %3==0 or n %5==0:
    print("YES")
else:
    print("NO")

n = int(input())
m = int(input())
if n-m>100 or n-m==100:
    print("YES")
else:
    print("NO")
"""

"""
arr = list('botsad')
arr1 = list(('fidelity','izumrud'))
print(arr)
print(len(arr))
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\n"+arr[0])
print(len(arr)+len(arr1))
print(arr1)
print(arr + arr1)

l1 = [1,2,3,4,5]
l2= ['Botsad', 'Almaty', ['F', 'O', 'N', 'T', 'A', 'N'], 25, True, False]
print(l1)
print(l2)
print(len(l1))
print(len(l2))
l3 = []
l3.append(l1)
print(l3)
c = [c* 2 for c in 'aziz' 'qaziz']
print(c)
print(c[0])
print(c[1])
print(c[0:])
print(c[:3])
for i in c:
    print(i, end="")
c[0] = ['gaziz']
print(c[0])
if 'alamaty' in c:
    print("YES")
else:
    print("NO")
if 'a' in c:
    print("YES")
else:
    print("No 'a' in c")
print(len(c))#azizqaziz = 9 букв
print("____----____")
for ind in range(1,5):
    print("последовательность от одного до 5 не включительно", ind)
for p in range(1,5,2):#2 это шаг(1,3,5,7,9...)
    print(p)
print('_______')
d = ['almaty', 1995, 'aziz', 15]
for a in d :
    print(len(d))
print(d)
print(d[:2])

'''
"""
'''num_count = int(input())
for i in input().split():
    number = int(i)
    print(i)
index_count = int(input())
for i in input().split():
    index = int(i)


shoplist = ['water', 'coca-cola', 'sprite']
print('я должен сделать', len(shoplist), 'покупок')#я должен сделать 3 покупок
print(shoplist[:])#['water', 'coca-cola', 'sprite']
print(range(len(shoplist)))#range(0, 3)

print('Покупки:', end=' ')
for item in shoplist:
    print(item, end=' ')
'''

#a = 0
#while True:
   # N = int(input())
    #a = a+N
    #if N==0:
    #    break
#print(a)

'''sum = 0
k = 0
while True:
    N = int(input())
    sum = sum+N
    if N==0:
        break
    k = k+1
print(sum//k)
'''
'''a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a,b+1):
    if i % d == c:
        print(i, end = " ")
'''
#ЦИКЛЫ БОНУСНОЕ ЗАДАНИЕ 2
''''
k = int(input('k стоимость одного банана: ', ))#3 цена за один
n = int(input('n кол-во долларов: ', ))#17 в наличии
w = int(input('w кол-во бананов: ', ))#4 кол-во бананов

t = sum((i + 1) * k for i in range(w))
o = t - n
if o >= 0:
    print(o)
else:
    print(0)'''


"""shoplist = ['apple', 'orange', 'cucumber']
print('1', 'I should buy', len(shoplist), 'items')
print('2', 'Покупки:', end = "")
for item in shoplist:
    print(item, end= " ")
print('3', '\n Also need to buy rice.')
shoplist.append('rice')
print(shoplist)
print('4', 'sort list: ')
shoplist.sort()
print(shoplist)
print('First item to by is', shoplist[0])
del shoplist[0]
print('Now my shoplist looks like:', shoplist)
"""


"""zoo = ('питон', 'слон', 'пингвин') # помните, что скобки не обязательны print('Количество животных в зоопарке -', len(zoo))
new_zoo = 'обезьяна', 'верблюд', zoo
print('Количество клеток в зоопарке -', len(new_zoo))
print('Все животные в новом зоопарке:', new_zoo)
print('Животные, привезённые из старого зоопарка:', new_zoo[2])
print('Последнее животное, привезённое из старого зоопарка -', new_zoo[2][2])
print('Количество животных в новом зоопарке -', len(new_zoo) -1 + len(zoo))
"""

"""""arr = ['BITLAB', 'Academy', 'Almaty', 'Kazakhstan']
for x in arr:
    print(x)
print('___')
for x in range(len(arr)):
    print(arr[x])
for x in range(len(arr)):
    print(x)
    print(arr)
for x in arr:
    del arr[0]
print(arr)
if 'Almaty' in arr:
    print("YES")
print(len(arr))#кол-во элементов в списке: 1,2,3...
for i in range(len(arr)):# индесы элементов: 0,1,2,3...
    print(i)

arr1 = ['Almaty', 'Kazakhstan', 'botsad', 'fidelity']
for index in range(len(arr1)):
    print(arr1[len(arr1) - index - 1])

print('-------------------------')

arr = [4, 2, 6, 1, 8, 13, 7]
print(sorted(arr))

arr = [4, 2, 6, 1, 8, 13, 7]
arr.sort()
print(arr)

n = int(input())
a = []
for i in range(n):
    number = int(input())
    a.append(number)
    print(a)

n = int(input())#size of array
arr = list(map(int, input().split()[:n]))

k = 0
c = 0
mx = arr[0]
mn = arr[0]
for i in range(len(arr)):
    if arr[i]>mx:
        mx = arr[i]
    if arr[i]<mn:
        mn = arr[i]
arr.remove(mx)
arr.remove(mn)

for i in arr:
    k = k+1
    c = c+i
print(c, c/k)
"""""
"""n = int(input("Размер списка:", ))
arr = list(map(int, input("элементы списка: ", ).split()[:n]))
m = int(input("число M: ", ))
for i in range(len(arr)):
    if m == arr[i]:
        print("YES")
        print(i)
        break
else:
    print("NO")

n = int(input())#size of array
arr = list(map(int, input().split()[:n]))
k = 0
c = 0
mx = arr[0]
mn = arr[0]
for i in range(len(arr)):
    if arr[i]>mx:
        mx = arr[i]
    if arr[i]<mn:
        mn = arr[i]

arr.remove(mx)
arr.remove(mn)

for i in arr:
    k = k+1
    c = c+i
print(c, c/k)

n = int(input())
arr = list(map(int,input().split()[:n]))
k = 0
c = 0
for i in arr:
    k = k+1
    c = c + i
for i in range(len(arr)):
    if arr[i] > c/k:
        print(arr[i])


n = int(input())
arr = list(map(int,input().split()[:n]))
m = int(input())
c = 0
k = 0
for i in arr:
    if i > m:
        c = c + i
        k = k + 1
print(c/k)


n = int(input())
arr = list(map(int, input().split()[:n]))
c = 0
k = 0
for i in arr:
    if i % 2 == 0:
        c = c +i
        k = k+1
print(c//k)

n = int(input())
arr = list(map(int, input().split()[:n]))
m = int(input())
for i in arr:
    if i % m ==0 and i !=0:
        print(i, end = " ")
        

A = [[1, 2, 3], [4, 5, 6]]
for i in A:
    for j in i:
        print(j, end = " ")
    print()
print('_____')

for i in A:
    print(' '.join(map(str, i)))
print('__________')
S = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        S += A[i][j]
        print(S)
print("____")
P = 0
for i in A:
    for j in i:
        P = P + j
        print(P)
print("_____")



n = int(input())
a = []
arr = list(map(int, input().split()[:n]))
for i in arr:
        if i % 2 == 0:
            a.append(i)
for j in a:
    print(j, end = " ")


n = int(input("KZT: "))
m = int(input("Choose [1-3]: "))
if m == 1:
    print("USD: ", n/420)
elif m == 2:
    print("EUR: ", n/510)
elif m == 3:
    print("RUB: ", n/5.8)

a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < a+b:
    print("YES")
else:
    print("NO")

n = int(input())
arr = list(map(int, input().split()[:n]))
c = 0
a = []
for i in arr:
    if i != 0:
        a.append(i)
    print(a)

#Пусть дан квадратный массив из n строк и n столбцов. 
# Необходимо элементам, находящимся на главной диагонали, 
# проходящей из левого верхнего угла в правый нижний 
# (то есть тем элементам a[i][j], для которых i==j) присвоить значение 1, 
# элементам, находящимся выше главной диагонали – значение 0, 
# элементам, находящимся ниже главной диагонали – значение 2.
# То есть необходимо получить такой массив (пример для n==4):
 
n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
        print(a[i][j], end = " ")
    print()
#for row in a:
    #print(' '.join([str(elem) for elem in row]))




n = int(input())
m = int(input())
a = []
b = []
for i in range(n):
    a.append((input().split()))
for i in range(len(a)):
    if i % 2 == 0:
        b.append(a[i])
for i in b:
    for j in i:
        print(j, end = " ")
    print()


n,m = map(int,input().split())
a = []
for i in range(n):
    a.append((input().split()))
k = int(input("выберите строку: "))

for i in a[k]:
    print(i, end = " ")
print()
  
    #или 

# b.append(a[k])
# b = []
# for i in b:
#   for j in i:
    #print(j, end = " ")
#print()


n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input().split())
for i in range(n):
    for j in range(m):
        a[i][j] = int(a[i][j])
        if a[i][j] % 2 == 0:
            print(a[i][j], end = " ")
    print()


n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input().split())
for i in range(n):
    for j in range(m):
        a[i][j] = int(a[i][j])
        if a[i][j] >= 0:
            print(a[i][j], end = " ")
    print()


n, m = map(int, input(). split())
a = []
for i in range(n):
    a.append(input(). split())
for i in range(n):
    for j in range(m):
        a[i][j] = int(a[i][j])
        if a[i][j] % 2 ==0 and a[i][j] >= 0:
            print(a[i][j], end = " ")
    print()

n, m = map(int, input(). split())
a = []
for i in range(n):
    a.append(input().split())
for i in range(n):
    for j in range(m):
        a[i][j] = int(a[i][j])
        a[i][j] = a[i][j] ** 2
        print(a[i][j], end = " ")
    print()


n = 2
m = 3
a = [
    [1,2,3,5],
    [6,7,8,9],
    [10,11,12,13,14]
]
for i in a:
    for j in i:
        if j % 2==0:
            print(j, end = " ")
    print()


n, m = map(int, input(). split())
a = []
for i in range(n):
    a.append(input().split())
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = int(a[i][j])
        if a[i][j] < 0:
            print(i,j)


n, m = map(int, input().split())
a = []
s = 0
for i in range(n):
    a.append(input().split())
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = int(a[i][j])
        if i % 2 == 0 and j % 2 == 0:
            s = s + a[i][j]
print(s)

n, m = map(int, input(). split())
a = []
b = []
s = 0
for i in range(n):
    a.append(input().split())
for i in range(n):
    for j in range(m):
        a[i][j] = int(a[i][j])
        s += a[i][j]
    print(s)
    s = 0


n, m = map(int,input().split())
a = []
mx = 0
for i in range(n):
    a.append(input().split())
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = int(a[i][j])
        if a[i][j] > mx:
            mx = a[i][j]
            imax = i
            imx = j
print(mx)
print(imax, imx)


n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input().split())
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = int(a[i][j])
        if a[i][j] % 2 !=0:
            a[i][j] = 0
        print(a[i][j], end = " ")
    print()


#Задание 15

n, m = map(int, input().split())
a = []

for i in range(n):
    a.append(input().split())
k = int(input())
for i in range(len(a)):

    for j in range(len(a[i])):

        a[i][j] = int(a[i][j])
        if a[i][j] % k == 0:
            a[i][j] = a[i][j] // k
        print(a[i][j], end = " ")
    print()



n, m = map(int, input(). split())
a = []
for i in range(n):
    a.append(input().split())
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = int(a[i][j])
        mx = 0
        mx = int(mx)
        if a[i][j] > mx:
            mx = a[i][j]
            print(mx)

n, m = map(int, input(). split())
a = []
for i in range(n):
    a.append(input().split())
for j in range(m):
    mx = 0
    for i in range(n):
        a[i][j] = int(a[i][j])
        if a[i][j] > mx:
            mx = a[i][j]
    print(mx)

n, m = map(int, input().split())
a = []
mx = 0
mn = 9000
max_i = 0
max_j = 0
min_i = 0
min_j = 0
for i in range(n):
    a.append(input().split())
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = int(a[i][j])
        if a[i][j] > mx:
            mx = a[i][j]
            max_i = i
            max_j = j
        if a[i][j] < mn:
            min_i = i
            min_j = j
            mn = a[i][j]
a[max_i][max_j] = mn
a[min_i][min_j] = mx
for i in a:
    for j in i:
        print(j, end=' ')
    print()


n = int(input())
a = []
for i in range(n):
    a.append(input().split())
a[0], a[-1] = a[-1], a[0]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = " ")
    print()



n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    a.append(input(). split())
for i in range(n):
    mx = 0
    for j in range(m):
        a[i][j] = int(a[i][j])
        if a[i][j] > mx:
            mx = a[i][j]
    b.append(mx)
print(min(b))



#Задание 19
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input(). split())
for i in range(len(a)):
    avg = 0
    for q in range(len(a[i])):
        avg += int(a[i][q])
    avg = avg/m
    for j in range(len(a[i])):
        a[i][j] = int(a[i][j])
        if avg > a[i][j]:
            a[i][j] = 0
        print(a[i][j], end = " ")
    print()
"""
