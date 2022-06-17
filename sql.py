#
# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="bitlab"
# )
# mycursor = mydb.cursor()
#
# while True:
#     print("Press 1 to add player")
#     print("Press 2 to list players")
#     print("Press 3 to Update")
#     print("Press 0 to exit")
#
#     choice = input()
#
#     if choice == "1":
#         print("INSERT NAME:")
#         name = input();
#         print("INSERT NUMBER:")
#         number = int(input())
#         print("INSERT PRICE:")
#         price = int(input())
#
#         sql = "INSERT INTO bitlab.players(id, name, number, price) VALUES(NULL, %s, %s, %s)"
#         val = (name, number, price)
#         mycursor.execute(sql, val)
#         mydb.commit()
#
#     elif choice == "2":
#         sql = "SELECT * FROM bitlab.players"
#         mycursor.execute(sql)
#         result = mycursor.fetchall()
#
#         for player in result:
#             print(str(player[0])+" "+player[1]+" "+str(player[2])+" "+str(player[3]))
#
#     elif choice == "3":
#         sql = "UPDATE bitlab.players SET name = %s, number = %s, price = %s WHERE id = 1"
#         val = ("Batman", 0, 0000)
#         mycursor.execute(sql,val)
#         mydb.commit()
#
#
#     elif choice == "0":
#         mycursor.close()
#         mydb.disconnect()
#         break

# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = "univer"
# )
#
# mycursor = mydb.cursor()
#
# sql = "SELECT dorm.id \
#     dorm.name \
#     dorm.age \
#     FROM dorm \
#     INNER JOIN sex ON dorm.name=sex.name"
#
# mycursor.execute(sql)
# result = mycursor.fetchall()
# for user in result:
#     print(user)

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'example'
)

mycursor = mydb.cursor()

def addUser(login,name,surname,age):
    sql = "insert into example.table (id, login, name, surname, age) values(NULL, %s, %s, %s, %s)"
    values = (login, name, surname, age)
    mycursor.execute(sql,values)
    mydb.commit()

def getUsers():
    sql = "select * from example.table ORDER BY age DESC" #показать всех из таблицы по уменьшению возраста
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

def deleteUser(id):
    sql = "delete from example.table where id = "+str(id)
    mycursor.execute(sql)
    mydb.commit()

def updateUser(id,login,name,surname,age):
    sql = "update example.table set login = %s, name = %s, surname = %s, age = %s where id="+ str(id)
    values = (login, name, surname, age)
    mycursor.execute(sql,values)
    mydb.commit()

while True:
    print("PRESS 1 TO ADD USER")
    print("PRESS 2 TO LIST USERS")
    print("PRESS 3 TO DELETE USER")
    print("PRESS 4 TO UPDATE USER")
    print("PRESS 0 TO EXIT")

    choice = input()

    if choice == "1":
        print("insert login:")
        login = input()
        print("insert name:")
        name = input()
        print("insert surname:")
        surname = input()
        print("insert age:")
        age = int(input())

        addUser(login,name,surname,age)

    elif choice == "2":
        users = getUsers()
        for user in users:
            for j in user:
                print(j, end = " ")
            print()


    elif choice == "3":
        users = getUsers()
        for user in users:
            print(user)

        print("choose id of user to delete:")
        id = input()
        deleteUser(id)

    elif choice == "4":
        users = getUsers()
        for user in users:
            print(user)

        print("choose id of user to update:")
        id = input()

        print("insert new login:")
        login = input()
        print("insert new name:")
        name = input()
        print("insert new surname:")
        surname = input()
        print("insert new age:")
        age = input()

        updateUser(id, login, name, surname, age)

    elif choice == "0":
        break

