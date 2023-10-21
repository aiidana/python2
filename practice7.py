
# import tkinter as tk
# master=tk.Tk()
# msg=tk.message(master,text='The best way to predict the future is to invent it')
"""
import re
# d={'Ali':'ali','Sam':'sam'}
print('Welcome')
action=input('Enter what do you want to do: 1.show db \n 2add user \n 3change password \n 4change name \n')

with open('t2.txt','r')as f:
    x=f.read()
def show_db():
    print(x)
def add_user(name, passw):
    while name in x:
        name = input("Name already exists, enter another name: ")
    while not check_pass(passw):
        passw = input('Invalid password. Enter another password: ')
    x[name] = passw
    print('Congratulations, user added!')

# def check_pass(passw):
#     cnt=0
#     for i in passw:
#         if i  in '@#$%':
#             return True
#     for i in passw:
#         char=ord(i)
#         if ((char>=65 and char<=90) and (char>=97 and char<=122)):
#             return True
#     for i in passw:
#         char=ord(i)
#         if (char>=48 and char<=57):
#             return True
#     return False
def check_pass(passw):
    if re.search(r'[a-z]+', passw) and re.search(r'[A-Z]+', passw) and re.search(r'[0-9]+', passw) and re.search(r'[@!#$%&*]+', passw):
        return True
    return False
    # if re.search(r'[a-z]+',passw):
    #     return True
    # if re.search(r'[A-Z]+',passw):
    #     return True
    # if re.search(r'[0-9]+',passw):
    #     return True
    # if re.search(r'[@!#$%&*]+',passw):
    #     return True
    # return False
def change_pass(x,name,passw):
    if name in x:
        while not check_pass(passw):
            new_passw = input('Invalid new password. Enter another password: ')
        x[name]=new_passw
        print('password changed!')
    else:
        print('user with name',name,'has not found!')
if action=='show db':
    show_db()
elif action=='add user':
    name=input("enter name: ")
    passw=input('enter pass: ')
    add_user(name,passw)
elif action=='change password':
    name=input('Enter your name:')
    passw=input('enter password')
    change_pass(x,name,passw)

"""

# import tkinter as tk
# master=tk.Tk()
# l1=tk.Label(master,text='user name')
# l1.pack()
# e1=tk.Entry()
# e1.pack()
# def F():
#     print(e1.get())
# b1=tk.Button(master,text='ok',command=F)
# b1.pack()
# master.mainloop()

import tkinter as tk
import re
import tkinter as ttk
wind=tk.Tk()
d={'Ali':'ali','Sam':'sam'}
l1=tk.Label(wind,text='welcome!')
l1.pack()
def show():
    wind2 = tk.Toplevel(wind)  # Используйте Toplevel для создания всплывающего окна
    wind2.title('Database')
    all_text = ""
    for name, passw in d.items():
        all_text += f"{name}: {passw}\n"
    wind_label = tk.Label(wind2, text=all_text)
    wind_label.pack()
show_db=tk.Button(wind,text='show db',command=show)
show_db.pack()

def add():
    wind2=tk.Tk()
    txt=tk.Label(wind2,text='Enter name and password')
    txt.pack()
    e1=tk.Entry(wind2)
    e2=tk.Entry(wind2)
    d={'Aidana':'qwer123','Sam':'sam'}
    def check_name():
        key_to_check=e1.get()
        key_check=e2.get()
        if key_to_check in d:
          result=tk.Label(wind2,text='Name already exists, enter another name:')
          result.pack()
        else:
            if re.search(r'[a-z]+', key_check) and re.search(r'[A-Z]+', key_check) and re.search(r'[0-9]+', key_check) and re.search(r'[@!#$%&*]+', key_check):
              cong=tk.Label(wind2,text='congratulations, user added!')
              cong.pack()
            else:
               result=tk.Label(wind2,text='Invalid password. Enter another password:')
               result.pack()

    bt=tk.Button(wind2,text='registration',command=check_name)
    bt.pack()
    e1.pack()
    e2.pack()
    wind2.mainloop()

add_user=tk.Button(wind,text='add user',command=add)
add_user.pack()

def change_passw():
   wind3=tk.Tk()
   e1=tk.Entry(wind3)
   e2=tk.Entry(wind3)
   def update():
      name=e1.get()
      new_password=e2.get()
      

      if name in d and re.search(r'[a-z]+', new_password) and re.search(r'[A-Z]+', new_password) and re.search(r'[0-9]+', new_password) and re.search(r'[@!#$%&*]+', new_password):

         d[name] = new_password
         result=tk.Label(wind3,text='Password has been successfully updated')
         result.pack()
      else:
          result=tk.Label(wind3,text='this name is not in the database or you entered the wrong password')
          result.pack()
    
      new_password.pack()
   change=tk.Button(wind3,text='change password',command=update)
   change.pack()
   e1.pack()
   e2.pack()
   wind3.mainloop()
change_pas=tk.Button(wind,text='change password', command=change_passw)
change_pas.pack()

wind.mainloop()