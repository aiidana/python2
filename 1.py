x=input()
#1
print(type(x))
#2
print(len(x))
#3
def test_variable(x):
    if isinstance(x,list):
        print("is a list")
    elif isinstance(x,tuple):
        print("is a tuple")
    elif isinstance(x,set):
        print("is a set ")
    else:
        print("the variable is not  a list, tuple, nor a set")
test_variable([1, 2, 3])
test_variable((1, 2, 3))
test_variable({1, 2, 3})

#4
y=int(input())
sum=0
if y>=0:
    for i in range(1,y):
        sum+=i
print(sum)

#5
n=input().split()
n=[float(num) for num in n ]
summ=sum(n)
print(summ)

#6 
x=int(input())
y=int(input())
z=pow((x+y),2)
print(z)

#7
name=input()
age=input()
add=input()
detail=f"{name}\n{age}\n{add}"
print(detail)

#8
height=int(input())
base=int(input())
area=(height*base)/2
print(area)

#circle
import math
x1,y1,r1,x2,y2,r2=int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), 
# distance=math.sqrt((x1-x2)**2 - (y1-y2)**2)
def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 - (y1-y2)**2)
def check(x1,y1,r1,x2,y2,r2):
    checking=distance(x1,y1,x2,y2)
    if checking <= r1-r2:
        return ("C2 is in C1")
    elif checking<=r2-r2:
        return ("c1 is in c2")
    elif checking<r1+r2:
        return ("circumference of c1 and c2 intersect")
    else:
        return ("c1 and c2 don't overlap")

print(check(x1,y1,r1,x2,y2,r2))


#9
string="""Twinkle, twinkle, little star,
 How I wonder what you are!
Up above the world so high, 
Like a diamond in the sky. 
Twinkle, twinkle, little star, 
How I wonder what you are"  
 """

print(string)

#10
