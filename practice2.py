#1
# lists=[]
# for x in range(1,100+1):
#     if x%7==0 and x%5==0:
#         lists.append(x)
# print(lists)

#2
# c=int(input())
# F=int(input())
# F_to_C=(F-32)/1.8
# C_to_F=(9/5)*c +32
# print(c,"°C is" , C_to_F, "in Fahrenheit ")
# print(F,"°F is" , F_to_C, "in Celsius  ")

#3
# lists=[1,2,3,4,5,6,7,8,9]
# x=int(input())
# for i in lists:
#     if x in lists:
#         print("Well guessed!")
#         break
#     else:
#         print("your guesses wrong")
        
#         # continue

#4
# x=int(input())
# for i in range(1,x+1):
#     for j in range(i):
#         print('*',end=' ')
#     print()

# for i in range(x-1,0,-1):
#     for j in range(i):
#         print('*',end=' ')
#     print()


#5
# s=input()
# print(s[::-1])

#6
# numbers=(1,2,3,4,5,6,7,8,9)

# cnt_odd=0
# cnt_even=0
# for i in numbers:
#     if i % 2 ==0:
#         cnt_even=cnt_even+1
#     else:
#         cnt_odd=cnt_odd+1
# print("Number of even numbers :",cnt_even)
# print("Number of odd numbers :",cnt_odd)

#7
# start=0
# end=50
# lists=[]

# def fibonacci(start,end):
#     a=0
#     b=1
#     while len(lists)<=50:
#         lists.append(a)
#         a,b=b,a+b
#     return lists

# lists=fibonacci(start,end)
# print(lists)

#8
# start=0
# end=50
# # lists=[]
# # numbers=()
# for num in range(start,end+1):
#     if num%3==0:
#         print("mcm")
#     elif num%5==0:
#         print("kbtu")
#     elif num%3==0 and num%5==0:
#         print("McmKbtu")
#     else:
#         print(num)

#9


#10
# s=input()
# print(s.lower())

#11
# numbers=input()
# x=int()
# binary_numbers=numbers.split(',')
# lists=[]
# lists2=[]

# for i in binary_numbers:
#     dec=int(i,2)
#     if dec % 5 ==0:
#        lists.append(str(dec))
#     else:
#         lists2.append(str(dec))

# print(lists)
# print("not divisible by 5",lists2)

#12
#48-57 65-90 97-122
# s=input()
# cnt_digits=0
# cnt_letters=0
# for i in s:
#     char=ord(i)
#     if (48<= char <=57):
#        cnt_digits+=1
#     elif((65<=char<=90 ) or (97<=char<=122)):
#        cnt_letters+=1

# print('letters', cnt_letters)
# print('digits',cnt_digits)

#13
# s=input()
# def check(s):
#     for i in s:
#         char=ord(i)
#         if(48<= char or char <=57) and (65<=char or char<=90) and (97<=char or char<=122) and (char==35 or char==36 or char==42) and (6<=len(s) or len(s)<=16):
#             return True
        
#     return False

# if check(s):
#     print("successful")
# else:
#     print("try again")

"""# for i in s:
#     char=ord(i)
#     if(48<= char or char <=57) and (65<=char or char<=90) and (97<=char or char<=122) and (char==35 or char==36 or char==42) and (6<=len(s) or len(s)<=16):
#         print("successful")
#     else:
#         print("try again")"""

#14
# start=100
# end=400
# lists=[]
# for i in range(start,end+1):
#     if i%2==0:
#         lists.append(i)

# print(lists)

#15
