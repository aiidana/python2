# n=int(input("number: "))
# k=int(input('power: '))
# def power(n,k):
#     return n**k
# print(power(n,k))

#2
# n=int(input())
# lt=[]
# def fibonacci(n):
#     a=0
#     b=1
#     while len(lt)<n:
#         lt.append(a)
#         a,b=b,a+b
#     return lt
# cubes=lambda lt: [x**3 for x in lt]
# fibonacci(n)
# print(cubes(lt))
#3
# import re 
# n=int(input('input:'))
# lt=[]
# for i in range(n):
#     s=input()
#     if re.match(r'^[a-z0-9A-Z.-_]+@[a-z]+\.[a-z]{2,}$',s):
#         lt.append(s)
# lt.sort()
# print(lt)



#4
# import re

# n = int(input())
# lt = []
# for i in range(n):
#     s = input('enter text: ')
#     lt.append(s)
# def modify(s):
#     s = re.sub(r'\s*&&\s*', ' and ', s)
#     s = re.sub(r'\s*\|\|\s*', ' or ', s)
#     return s
# for i in lt:
#     print(modify(i))


#5  +7 707 348 63 63
# import re
# number = input()
# if re.match(r'^\+?7|8\s\d{3}\s\d{3}\s\d{2}\s\d{2}$', number) or re.match(r'^\+?\s\d{3}\s\d{3}\s\d{2}\s\d{2}$', number):
#     print('valid')
# else:
#     print('invalid')
#6
# import re
# n=int(input())
# for i in range(n):
#     s=input()
#     brr=s.split()
#     name=brr[0]
#     email=brr[1]
#     if re.match(r'^[a-z]+@[a-z]+\.[a-z]{2,}$',email):
#         print(email)
#     else:
#         print('enter another email')

#7
# import re
# n=int(input('how many times will you check card: '))
# for i in range(n):
#     s = input('Enter the credit card number: ')
#     if re.match(r'^(?!.*(\d)([ -]?\1){3,})([4-6]\d{3}([ -]?\d{4}){3})$',s):
#         print('valid')
#     else:
#         print('invalid')
# ?! - используется для того, чтобы в строке не выполнялось определенное условие
# .* используется для поиска по всей строке
# (\d)Эта часть фиксирует одну цифру 
#(-?\1) эта часть проверяет, повторяется ли одна и та же цифра с необязательными дефисами
# {3,} он проверяет, повторяется ли одна и та же цифра три или более раз подряд с необязательными дефисами
