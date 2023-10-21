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

