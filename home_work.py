#1 already installed

#2 ok

#3
"""
1 10/3=3.3333333333335(float), 10//3=3 
2 10**3=1000(** means degree)
3 x=1 after x+=2 => x=3
4 float(1) => 1.0
5 bool("False") => True
  bool(False) => False
6 False, None, empty:strings,lists, tuples,dictionaries,sets; 0
7 The result of the expression 10 == "10" => False, 10 is not a string 
8 "bag">"apple" => True, b greater than a(unicode symbols)
9 not(True or False) => True, or operation True or False-> True
10 18 <= age < 65 => True, from 18(inclusive) to 65(not including 65)
11 range(1,10,2) => 1,3,5,7,9 from 1 to 10 with a step of 2
12 lists, tuples, dictionaries

"""

#4
#4.1
# import sys
# print(sys.version)

#4.2
# x=int(input())
# y=x*2
# area=x*y
# print(y)
# print(area)

#4.3
# first_name=input("first name: ")
# last_name=input("last name: ")
# reverse_fn=first_name[::-1]
# reverse_ln=last_name[::-1]
# print(reverse_fn,reverse_ln )
# print(last_name,first_name)

#4.4
# numbers=input().split(',')
# x=int()
# lists=[x for x in numbers]
# tuples=tuple(lists)
# print(lists)
# print(tuples)

#4.5
# subjects=["calculus","numerical methods","differential equations","python"]
# print(subjects[0])
# print(subjects[-1])

#4.6
# n=int(input())
# nn=n**2
# nnn=n**3
# print(n+nn+nnn)

#4.7
# radius=8
# volume=(4/3)*3.14*(radius**3)
# print(volume)

#4.8
# n=int(input())
# def check(n):
#     if abs(n-1000)<=100 or abs(n-2000)<=100:
#         return True
#     else:
#         return False

# if(check(n)):
#     print("a number is within 100 of 1000 or 2000.")
# else:
#     print("a number is not within 100 of 1000 or 2000.")

#4.9
# value=int(input())
# test=[1, 5, 8, 3]
# if value in test:
#     print(True)
# else:
#     print(False)

#4.10
# base=int(input())
# height=int(input())
# area=(base*height)/2
# print(area)

#4.11
# import math
# def distance(x1,y1,x2,y2):
#     return math.sqrt((x1-x2)**2 - (y1-y2)**2)
# x1,y1,x2,y2=int(input()),int(input()),int(input()),int(input())
# print(distance(x1,y1,x2,y2))

#4.12
"""
5x+8y=6
7x+9y=4
 
"""
# import numpy as np
# a,b,c,d,e,f=5,8,6,7,9,4
# A=np.array([[a,b],[d,e]])
# B=np.array([c,f])
# print(np.linalg.solve(A,B))

#4.13
# import math 
# x1, y1, x2, y2, x3, y3=int(input()),int(input()),int(input()),int(input()),int(input()),int(input())
# def distance(x1,y1,x2,y2):
#     return math.sqrt((x1-x2)**2 + (y1-y2)**2)
# slope1=(y2-y1)/(x2-x1)
# slope2=(y3-y2)/(x3-x1)
# x = (slope1 * x1 - slope2 * x2 + y2 - y1) / (slope1 - slope2)
# y = slope1 * (x - x1) + y1
# radius=distance(x, y, x1, y1)
# print(radius)
# print(x,y)


