#3
# import tkinter as tk
# wind=tk.Tk()
# wind.geometry('400x400')
# f_name=tk.Entry(wind,font=('Arial',15),width=13)
# f_name.place(x=250,y=10)
# l_name=tk.Entry(wind,font=('Arial',15),width=13)
# l_name.place(x=250,y=40)
# phone=tk.Entry(wind,font=('Arial',15),width=13)
# phone.place(x=250,y=70)
# email=tk.Entry(wind,font=('Arial',15),width=13)
# email.place(x=250,y=110)
# birthday=tk.Entry(wind,font=('Arial',15),width=13)
# birthday.place(x=250,y=140)
# last=tk.Entry(wind,font=('Arial',15),width=13)
# last.place(x=70,y=240)
# fr=tk.Entry(wind,font=('Arial',15),width=3)
# fr.place(x=180,y=90)

# fname=tk.Label(wind,text='First name:')
# fname.place(x=180,y=10)
# lname=tk.Label(wind,text='Last name:')
# lname.place(x=180,y=40)
# lastt=tk.Label(wind,text='Last Name:')
# lastt.place(x=0,y=240)
# ph=tk.Label(wind,text='Phone #:')
# ph.place(x=180,y=70)
# em=tk.Label(wind,text='Email:')
# em.place(x=180,y=110)
# birth=tk.Label(wind,text='Birthday:')
# birth.place(x=180,y=140)
# cont_list=tk.Label(wind,text='Contact List')
# cont_list.place(x=60,y=0)
# res=tk.Label(wind,text='Result:')
# res.place(x=270,y=250)
# lf=tk.Label(wind,text='Last,First:')
# lf.place(x=270,y=280)
# php=tk.Label(wind,text='Phone:')
# php.place(x=270,y=310)
# fre=tk.Label(wind,text='Friend')
# fre.place(x=200,y=90)


# add=tk.Button(wind,text='Add Contact')
# add.place(x=300,y=170)
# disp=tk.Button(wind,text='Display Contact')
# disp.place(x=50,y=190)
# search=tk.Button(wind,text='Search')
# search.place(x=120,y=340)
# wind.mainloop()

# 4 cnx^n+ cn-1x^n-1    + c1x+ c0
class MyPolynomial:
    def __init__(self,c,n):
        self.n=n
        self.c=c
    def get_c(self,c):
        return c
    def get_degree(self):
        return self.n
    def add():
        for i in range(n,0):
                def __add__(self,pv):
                   return MyPolynomial(self.c+pv.c,self.n+pv.n)
    def __mul__(self,pv):
          return MyPolynomial(self.c*pv.c,self.n*pv.n)
    
    


    
    
pol1=MyPolynomial(3,2)
pp=MyPolynomial(3,2)
pp.get_degree()
print(pp)
pol2=MyPolynomial(3,2)
# pol=pol1+pol2
pol3=pol1*pol2
# pol.get_c(3)
pol3.get_c(3)
print(pol3)

#2
import re
# n,m=int(input()),int(input())
# for i in range(n):
#     for j in range(m):
        
#1
import math
n=int(input())
for i in range(0,int(math.sqrt(n))):
    for j in range(0,n):
        s=input()
        br=s.split()
    



