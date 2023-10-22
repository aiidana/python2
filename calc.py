import tkinter as tk
import math
wind=tk.Tk()
wind.geometry('480x260+100+200')
wind.title('calculator')

calc=tk.Entry(wind,justify=tk.RIGHT,font=('Arial',15),width=15)
calc.insert(0,'0')
calc.grid(row=0,column=0,columnspan=8,stick='we')
entry_y = tk.Entry(wind, font=('Arial', 15), width=5)
entry_y.grid(row=0, column=0, sticky='wens')
def calculation():
    val=calc.get()
    calc.delete(0,tk.END)
    calc.insert(0,eval(val))
def clear():
    calc.delete(0,tk.END)
    calc.insert(0,'0')
def sinus():
    value=float(calc.get())
    calc.insert(0,math.sin(value))
def coss():
    value=float(calc.get())
    calc.insert(0,math.cos(value))
def tann():
    value=float(calc.get())
    calc.insert(0,math.tan(value))
def x2():
    value=float(calc.get())
    result=pow(value,2)
    calc.delete(0,tk.END)
    calc.insert(0,result)
def sqr():
    value=float(calc.get())
    result=math.sqrt(value)
    calc.delete(0,tk.END)
    calc.insert(0,result)
def pi():
    value=math.pi
    calc.delete(0, tk.END)
    calc.insert(0,value)
def div():
    value=float(calc.get())
    result=1/value
    calc.delete(0,tk.END)
    calc.insert(0,result)
def pwer():
    value=float(calc.get())
    y=float(calc.get())
    result=pow(value,y)
    calc.delete(0,tk.END)
    calc.insert(0,result)
def e():
    value=math.e
    calc.delete(0,tk.END)
    calc.insert(0,value)
def ln():
    value=float(calc.get())
    if value>0:
        result=math.log(value)
        calc.delete(0,tk.END)
        calc.insert(0,result)
    else:
        calc.delete(0, tk.END)
        calc.insert(0, "error")
def abss():
    value = float(calc.get())
    result = abs(value)
    calc.delete(0, tk.END)
    calc.insert(0, result)
def xx():
    value=float(calc.get())
    if value<0:
        result = abs(value)
        calc.delete(0, tk.END)
        calc.insert(0, result)
    elif value>0:
        result=value*(-1)
        calc.delete(0,tk.END)
        calc.insert(0,result)
def pro():
    value=float(calc.get())
    result=value/100
    calc.delete(0,tk.END)
    calc.insert(0,result)
def fac():
    value = int(calc.get())
    result = math.factorial(value)
    calc.delete(0, tk.END)
    calc.insert(0, result)
def dot():
    value=calc.get()
    new=value+'.'
    calc.delete(0,tk.END)
    calc.insert(0,new)
def brace():
    value=calc.get()
    new=value+'()'
    calc.delete(0,tk.END)
    calc.insert(0,new)
def add(digit):
    val=calc.get()
    if val[0]=='0':
        val=val[1:]
    calc.delete(0,tk.END)
    calc.insert(0,val+digit)
def add_oper(operation):
    value=calc.get()
    if value[-1] in '+-/*':
        value=value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,value+operation)
def bttn(digit):
    return tk.Button(text=digit,command= lambda: add(digit),font=('Arial',15),bg='palevioletred1',fg='white')
def bttn_operation(oper):
    return tk.Button(text=oper,command=lambda: add_oper(oper),font=('Arial',15),bg='lightpink',fg='black')
def bttn_calc(operation):
    return tk.Button(text=operation,command=calculation, font=('Arial',15),bg='lightblue',fg='black')
def bttn_clear(operation):
    return tk.Button(text=operation,command=clear,font=('Arial',15),bg='lightblue',fg='red')
def bttn_sin(operation):
    return tk.Button(text=operation,command=sinus,font=('Arial',15),bg='pink',fg='black')
def bttn_cos(operation):
    return tk.Button(text=operation,command=coss,font=('Arial',15),bg='pink',fg='black')
def bttn_tan(operation):
    return tk.Button(text=operation,command=tann,font=('Arial',15),bg='pink',fg='black')
def bttn_xsq(operation):
    return tk.Button(text=operation,command=x2,font=('Arial',15),bg='pink',fg='black')
def bttn_sqrt(operation):
    return tk.Button(text=operation,command=sqr,font=('Arial',15),bg='pink',fg='black')
def bttn_pi(operation):
    return tk.Button(text=operation,command=pi,font=('Arial',15),bg='pink',fg='black')
def bttn_brace(operation):
    return tk.Button(text=operation,command=brace,font=('Arial',15),bg='pink',fg='black')
def bttn_dot(operation):
    return tk.Button(text=operation,command=dot,font=('Arial',15),bg='pink',fg='black')
def bttn_1x(operation):
    return tk.Button(text=operation,command=div,font=('Arial',15),bg='pink',fg='black')
def bttn_xy(operation):
    return tk.Button(text=operation,command=pwer,font=('Arial',15),bg='pink',fg='black')
def bttn_e(operation):
    return tk.Button(text=operation,command=e,font=('Arial',15),bg='pink',fg='black')
def bttn_ln(operation):
    return tk.Button(text=operation,command=ln,font=('Arial',15),bg='pink',fg='black')
def bttn_abs(operation):
    return tk.Button(text=operation,command=abss,font=('Arial',15),bg='pink',fg='black')
def bttn_xx(operation):
    return tk.Button(text=operation,command=xx,font=('Arial',15),bg='pink',fg='black')
def bttn_pr(operation):
    return tk.Button(text=operation,command=pro,font=('Arial',15),bg='pink',fg='black')
def bttn_fac(operation):
    return tk.Button(text=operation,command=fac,font=('Arial',15),bg='pink',fg='black')
def press(event):
    if event.char.isdigit():
        add(event.char)
wind.bind('<Key>',press)

bttn('1').grid(row=1,column=3,stick='wens')
bttn('2').grid(row=1,column=4,stick='wens')
bttn('3').grid(row=1,column=5,stick='wens')
bttn('4').grid(row=2,column=3,stick='wens')
bttn('5').grid(row=2,column=4,stick='wens')
bttn('6').grid(row=2,column=5,stick='wens')
bttn('7').grid(row=3,column=3,stick='wens')
bttn('8').grid(row=3,column=4,stick='wens')
bttn('9').grid(row=3,column=5,stick='wens')
bttn('0').grid(row=4,column=4,stick='wens')
bttn_operation('+').grid(row=1,column=6,stick='wens')
bttn_operation('/').grid(row=2,column=6,stick='wens')
bttn_operation('-').grid(row=3,column=6,stick='wens')
bttn_operation('*').grid(row=4,column=6,stick='wens')
bttn_clear('C').grid(row=4,column=7,stick='wens')
bttn_calc('=').grid(row=4,column=5,stick='wens')
bttn_sin('sin').grid(row=1,column=0,stick='wens')
bttn_cos('cos').grid(row=1,column=1,stick='wens')
bttn_tan('tan').grid(row=1,column=2,stick='wens')
bttn_xsq('x^2').grid(row=2,column=0,stick='wens')
bttn_sqrt('sqrt').grid(row=2,column=1,stick='wens')
bttn_pi('π').grid(row=2,column=2,stick='wens')
bttn_brace('()').grid(row=1,column=7,sticky='wens')
bttn_dot('.').grid(row=2,column=7,sticky='wens')
bttn_1x('1/x').grid(row=4,column=0,stick='wens')
bttn_xy('^').grid(row=3,column=0,stick='wens')
bttn_e('e').grid(row=3,column=1,stick='wens')
bttn_ln('log').grid(row=3,column=2,stick='wens')
bttn_abs('|x|').grid(row=4,column=2,stick='wens')
bttn_xx('+/-').grid(row=4,column=1,stick='wens')
bttn_pr('%').grid(row=3,column=7,stick='wens')
bttn_fac('x!').grid(row=4,column=3,stick='wens')



wind.grid_columnconfigure(0,minsize=60)
wind.grid_columnconfigure(1,minsize=60)
wind.grid_columnconfigure(2,minsize=60)
wind.grid_columnconfigure(3,minsize=60)
wind.grid_columnconfigure(4,minsize=60)
wind.grid_columnconfigure(5,minsize=60)
wind.grid_columnconfigure(6,minsize=60)
wind.grid_columnconfigure(7,minsize=60)

wind.grid_rowconfigure(1,minsize=60)
wind.grid_rowconfigure(2,minsize=60)
wind.grid_rowconfigure(3,minsize=60)
wind.grid_rowconfigure(4,minsize=60)
wind.grid_rowconfigure(5,minsize=60)
wind.grid_rowconfigure(6,minsize=60)

wind.mainloop()
