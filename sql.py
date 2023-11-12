import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",

    user = "root",

    passwd = "niktoneznaet",
    database = "test")


# cursor = db.cursor()
# cursor.execute("CREATE TABLE userrs (name VARCHAR(255), password VARCHAR(255))")

import tkinter as tk
import re
wind=tk.Tk()
wind.geometry('300x200')
wind.title('db')

l1=tk.Label(wind,text='welcome!')
l1.place(x=140,y=10)
l2=tk.Label(wind,text='what do you want to do?')
l2.place(x=120,y=40)


def add():
    wind2 = tk.Tk()
    wind2.geometry('300x200')
    txt = tk.Label(wind2, text='Enter name and password')
    txt.pack()
    ll = tk.Label(wind2, text='name', width=5)
    ll.place(x=20, y=50)
    ll2 = tk.Label(wind2, text='password', width=7)
    ll2.place(x=10, y=70)
    e1 = tk.Entry(wind2, font=('Arial', 15), width=15)
    e2 = tk.Entry(wind2, font=('Arial', 15), width=15)

    def check_name():
        cursor = db.cursor()
        key_to_check = e1.get()
        key_check = e2.get()
        sql = "SELECT COUNT(*) FROM userrs WHERE name = %s"
        cursor.execute(sql, (key_to_check,))
        res = cursor.fetchone()

        if res[0] > 0:
            result = tk.Label(wind2, text='Name already exists, enter another name:')
            result.pack()
        else:
            if re.search(r'[a-z]+', key_check) and re.search(r'[A-Z]+', key_check) and re.search(r'[0-9]+', key_check) and re.search(r'[@!#$%&*]+', key_check):
                cong = tk.Label(wind2, text='congratulations, user added!')
                sql = "INSERT INTO userrs (name, password) VALUES (%s, %s)"
                cursor.execute(sql, (key_to_check, key_check))
                db.commit()
                cong.pack()
            else:
                result = tk.Label(wind2, text='Invalid password. Enter another password:')
                result.pack()

    bt = tk.Button(wind2, text='registration', command=check_name, bg='skyblue')
    bt.pack()
    e1.pack()
    e2.pack()
    wind2.mainloop()

add_us=tk.Button(wind,text='add user',command=add,width=15,bg='skyblue')
add_us.place(x=10,y=60)

def show_database():
    wind4 = tk.Tk()
    wind4.title('Database Contents')
    cursor = db.cursor()

    # Fetch data from the 'users' table
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    # Create a Listbox to display the data
    listbox = tk.Listbox(wind4, width=30)
    listbox.pack()

    # Insert data into the Listbox
    for row in data:
        listbox.insert(tk.END, row)

    wind4.mainloop()
showdb=tk.Button(wind,text='show database',command=show_database,width=15,bg='skyblue')
showdb.place(x=10,y=90)


def change_passw():
    wind3 = tk.Tk()
    wind3.geometry('300x200')
    nnn=tk.Label(wind3,text='name:')
    nnn.place(x=10,y=10)

    psss=tk.Label(wind3,text='new password:')
    psss.place(x=10,y=50)
    e1 = tk.Entry(wind3,font=('Arial',15))
    e1.place(x=100,y=10)
    e2 = tk.Entry(wind3,font=('Arial',15))
    e2.place(x=100,y=50)
    def update():
        namee = e1.get()
        cursor = db.cursor()
        sql = "SELECT COUNT(*) FROM userrs WHERE name = %s"
        cursor.execute(sql, (namee,))
        res = cursor.fetchone()
        new_password = e2.get()
        if res[0] > 0 and re.search(r'[a-z]+', new_password) and re.search(r'[A-Z]+', new_password) and re.search(r'[0-9]+', new_password) and re.search(r'[@!#$%&*]+', new_password):
            sql = "UPDATE userrs SET password = %s WHERE name = %s"
            cursor.execute(sql, (new_password, namee))
            db.commit()
            result = tk.Label(wind3, text='Password has been successfully updated')
            result.place(x=10,y=130)
        else:
            result = tk.Label(wind3, text='This name is not in the database or you entered the wrong password')
            result.place(x=10,y=130)
    
    change = tk.Button(wind3, text='change password', command=update, bg='skyblue')
    change.place(x=100,y=100)
    
    wind3.mainloop()

changeps=tk.Button(wind,text='change password',command=change_passw,width=15,bg='skyblue')
changeps.place(x=10,y=120)

def change_name():
    wind5=tk.Tk()
    wind5.geometry('300x200')
    crnm=tk.Label(wind5,text='ENTER current and last name')
    crnm.place(x=100,y=10)
    cr=tk.Label(wind5,text='current name')
    cr.place(x=10,y=30)
    nm=tk.Label(wind5,text='new name')
    nm.place(x=10,y=60)
    cur=tk.Entry(wind5,font=('Arial',15))
    cur.place(x=100,y=30)
    new=tk.Entry(wind5,font=('Arial',15))
    new.place(x=100,y=60)

    def updatee():
        cur_name=cur.get()
        new_name=new.get()

        cursor=db.cursor()
        sql = "SELECT COUNT(*) FROM userrs WHERE name = %s"
        cursor.execute(sql, (cur_name,))
        res = cursor.fetchone()
        if res[0]>0:
            sql = "UPDATE users SET name = %s WHERE name = %s"
            cursor.execute(sql, (new_name, cur_name))
            db.commit()
            result = tk.Label(wind5, text='Name has been successfully updated')
            result.place(x=10,y=130)
        else:
            result = tk.Label(wind5, text='Current name not found in the database')
            result.pack()
    but=tk.Button(wind5,text='change name',command=updatee,bg='skyblue')
    but.place(x=100,y=100)



    wind5.mainloop()
changenm=tk.Button(wind,text='change name',command=change_name,width=15, bg='skyblue')
changenm.place(x=10,y=150)
wind.mainloop()