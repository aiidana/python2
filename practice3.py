#strings

#1
# s=input()
# print(len(s))

#2
# s=input()
# cnt=0
# dict={}
# for i in s:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)

        
#3
# s=input()
# def strng(s):
#     if not isinstance(s,str):
#         raise TypeError("input is not a string")
#     if len(s)<2:
#         raise ValueError("length is less than 2")
#     a=s[:2]+s[-2:]
#     return a
# try:
#     print(strng(s))
# except TypeError as error:
#     print(error)
# finally:
#     print("done")
#4
# s=input()
# for i in range(1,len(s)):
#     if s[0]==s[i]:
#         s=s[0]+s[1:i]+'&'+s[i+1:]
#         print(s[i])
# print(s)


#5
# s,st=input(),input()
# a=st[0]+s[1:-1]+s[-1]
# b=s[0]+st[1:-1]+st[-1]
# print(a,b)

#6
# s=input()
# for i in range(0,len(s)):
#     if len(s)==2 or len(s)==1:
#         s=s+'ing'
#         break

#     elif  (s[-3]+s[-2]+s[-1]=='ing') :
#         s=s+'ly'
#         break
#     else:
#         s=s+'ing'
#         break
# print(s)

#7
# s=input()
# def check(s):
#     if not isinstance(s,str):
#         raise TypeError("input must be a string")

#     if s.find('not')!=-1 and s.find('poor')!=-1 and s.find('not')<s.find('poor'):
#         s=s[:(s.find('not'))]+'good'+s[(s.find('poor')+4):]
    
#     return s
# try:
#     print(check(s))
# except TypeError as error:
#     print(error)

#8
# s=input("input words: ").split()
# maxi=-99999
# for i in s:
#     length=len(i)
#     if length>maxi:
#         maxi=length
# print("the length of the longest one:",maxi)

#9
# s=input()
# n=int(input())
# def nth(s):
#     for i in range(0,len(s)):
#         i=n
#         return s[:i]+s[i+1:]
# try:
#     print(nth(s))
# except TypeError as error:
#     print(error,'index out of range')
# else:
#     print(s[n])
# finally:
#     print('done')
#10
# s=input()
# a=str()
# if len(s)>2:
#     a=s[-1]+s[1:-1]+s[0] 
# else:
#         print("try again")
# print(a)

#11
# s=input()
# for i in range(0,len(s)):
#     if i%2==0:
#         print(s[i])

#12
# s=input()
# words=s.split()
# dict={}
# for i in words:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# for word,count in dict.items():
#     print(word,':',count)

#13
# s=input()
# upp=s.upper()
# print(upp)
# low=s.lower()
# print(low)

#14
# s=input()
# st=s.split()
# list1=[]
# list2=[]
# for i in st:
#     if i not in list1:
#         list1.append(i)
#     else:
#         list2.append(i)
# sort=sorted(list1)
# print(sort)

#15
# st='[[]]'
# s=input()
# def insert(s):
#     mid=len(st)//2
#     return st[:mid]+s+st[mid:]
# print(insert(s))

#16
# s=input()
# a=4*s[-2::1]
# print(a)

#17
# s=input()
# if len(s)%4==0:
#     s=s[::-1]
#     print(s)
# else:
#     print("it's length is not a multiple of 4.")

#18
# s=input()
# cnt=0
# for i in range(0,4):
#     if s[i].isupper():
#         cnt+=1
    
# if cnt>=2:
#     print(s.upper())
# else:
#     print("no uppercase")

#19
# s=input()
# start=input()
# st=s.split()
# for i in range(0,len(st)):
#     if st[0]==start:
#         print('the string starts with',start)
#         break
#     else:
#         print('the string does not start with',start)
#         break

#21
# s=input()
# prefixx=input("prefix:")
# words=s.split()
# def prefix(words):
#     for i in words:
#         st=prefixx+i
#         print(st)
# prefix(words)
#22
# numbers=[3.141596,5.5678,45.889,57.0012]
# def num(numbers):
#     for i in numbers:
#         a=str(i).find('.')+3
#         if int(str(i)[a])>=5:
#             i=str(i)[:a-1]+str(int(str(i)[a-1])+1)
#             print(i)
#         elif(int(str(i)[a])<5):
#             i=str(i)[:a]
#             print(i)
# num(numbers)

#23
# numbers=[1,34,65,678,45]
# n=int(input())
# def num(numbers):
#     for i in numbers:
#         if len(str(i))<n:
#             s='0'*(n-len(str(i))) +str(i)
#             print(s)
#             # return s
#         else:
#             return ("try again")

# num(numbers)

#24
# numbers=[1,22,33,4343,45]
# n=int(input())
# def num(numbers):
#     for i in numbers:
#         if len(str(i))<n:
#             s=str(i)+'*'*(n-len(str(i)))
#             print(s)
#         elif len(str(i))==n:
#             print(str(i))
#         else:
#             print("try again")
# num(numbers)

#26
# s=input()
# a=s[::-1]
# print(a)
#27
# s=input()
# st=s.split()
# reversed=st[::-1]
# print(reversed)

#28
# s=input()
# dict={}
# for i in s:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]+=1
# for i,cnt in dict.items():
#     if cnt>1:
#         print(i, cnt)

#29
# length=float(input("length: "))
# width=float(input("width: "))
# radius=float(input("radius: "))
# height=float(input("height: "))
# area_rec=length*width
# volume_cyl=3.14*radius**2 *height
# print("The area of the rectangle is",area_rec,"cm²")
# print("The volume of the cylinder is",volume_cyl,"cm3")
#30
# s=input()
# for i in range(0,len(s)):
#     print("Current character",s[i], "position at", i)
    
#31
# s=input()
# st=s.split()
# list=[]
# list.append(st)
# print(list)

#32
# s=input()
# n=int(input())
# for i in range(0,len(s)):
#     low=s[:n].lower()
#     st=low+s[n:]
# print(st)
#33
# s=input()
# a=' '
# st_1=s.replace('.',a)
# st_2=st_1.replace(',','.')
# st_3=st_2.replace(a,',')
# print(st_3)

#34
# s=input()
# dict={}
# for i in s:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]+=1
# for i,cnt in dict.items():
#     if cnt==1:
#         print(i)
#35
# s=input()
# list=[]
# for i in s:
#     if i in list:
#         print(i)
#     list.append(i)

#36
# s=input()
# words=s.split()
# list=[]
# for i in words:
#     if i in list:
#         print(i)
#     list.append(i)

#39
# s=input()
# word=s.split()
# for i in word:
#     if len(i)>2:
#         st=i[0].upper()+i[1:-1]+i[-1].upper()
#         print(st)
#     else:
#         st=i.upper()
#         print(st)



#LISTS
#1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in range(0,len(a)):
#     if a[i]<=5:
#         print(a[i])

#2
# s=input()
# def pal(s):
#     s=s.upper()
#     st=s.upper()
#     return s==st[::-1]
# if pal(s):
#     print(s,"is a palindrome")
# else:
#     print(s,'is not palindrome')
#3
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# list=[]
# for i in range(0,len(a)):
#     if a[i]%2==0:
#         list.append(a[i])
# print(list)

#4

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# listt=list(a and b)

# print(listt)

#5
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# listt=list(set(a).intersection(set(b)))
# print(listt)

#6
# a = [5, 10, 15, 20, 25]
# s=a[0]
# b=a[-1]
# listt=[]
# listt.append((s,b))
# print(listt)

#7
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# listt=[]
# def lt(a):
#     for i in a:
#         if i not in listt:
#             listt.append(i)
#     return listt
# print(lt(a))

#extra
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# def lt(a):
#     sett=set(a)
#     unique=list(sett)
#     return unique
# print(lt(a))