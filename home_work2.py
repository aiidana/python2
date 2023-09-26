#1
# n=7
# for i in range(n):
#     for j in range(n):
#         if (i==0 and j==0 )or(i==n-1 and j==0)or(j==n-1 and i==0)or(j==n-1 and i==n-1):
#             print(" ",end=' ')
#         elif i==0 or i==n-1 or j==0 or j==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#2
# n=7
# for i in range(n):
#     for j in range(n):
#         if (j==(n-2) and i==0 ) or i==n-1 or (i==0 and j==(n-1)):
#             print(" ",end=' ')
#         elif(j==0 or(i==0)or (i==j and i>(n/2) )or (i==(n//2) and j<(n/2))  or (i==1 and j==(n-3)) or(i==2 and j==(n-3))):
#             print('*',end=' ')
#         else:
#             print(" ",end=' ')
#     print()
#3
# age=int(input("a dog's age in human years:"))
# dog_year=2*10.5 + (age-2)*4
# print("The dog's age in dog's years is",dog_year)

#4
# def vowell(s):
#     vowel=['a','e','u','i','o','A','E','U','I','O']
#     if s in vowel:
#         return True
#     else:
#         return False
# s=input("a letter of the alphabet:")

# if(vowell(s)):
#     print(s,"is a vowell")
# else:
#     print(s,"is a consonant")

#5
"""January 31, February 28-29, March 31, April30, May 31, June 30, July 31, August31

, September 30, October 31, November 30, December31"""
# s=input("the name of Month:")
# if s=="January":
#     print("number of days: 31 day")
# elif s=="February":
#     print("number of days : 28/29 days")
# elif s=="March":
#     print("number of days : 31 days")
# elif s=="April":
#     print("number of days : 30 days")
# elif s=="May":
#     print("number of days : 31 days")
# elif s=="June":
#     print("number of days : 30 days")
# elif s=="July":
#     print("number of days : 31 days")
# elif s=="August":
#     print("number of days : 31 days")
# elif s=="September":
#     print("number of days : 30 days")
# elif s=="October":
#     print("number of days : 31 days")
# elif s=="November":
#     print("number of days : 30 days")
# elif s=="December":
#     print("number of days : 31 days")

#6
# a,b=int(input()),int(input())
# sum=a+b
# if sum>=15 and sum<=20:
#     print('20')
# else:
#     print(sum)

#7
# s=input("input a string: ")
# def check(s):
#     for i in s:
#         char=ord(i)
#         if(char>=48 and char<=57):
#             return True
#     return False
# if check(s):
#     print("The string is an integer.")
# else:
#     print("The string is not an integer.")

#8
# x=int(input("x: "))
# y=int(input("y: "))
# z=int(input("z: "))
# if x==y==z:
#     print("Equilateral triangle")
# elif x==y or x==z or z==y:
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle")

#9
# month=int(input("input the month: "))
# day=int(input("input the day: "))
# s=str()
# def season(month):
#     if month == 12 or month==1 or month ==2:
#         return 'winter'
#     elif month==3 or month==4 or month==5:
#          return "spring"
#     elif month==6 or month==7 or month ==8:
#         return "summer"
#     else:
#         return "autumn"
    
# month_12={
#     1:"January",
#     2:"February",
#     3:"March",
#     4:"April",
#     5:"May",
#     6:"June",
#     7:"July",
#     8:"August",
#     9:"Sdptember",
#     10:"November",
#     11:"October",
#     12:"December"
# }
# prt_month=month_12[month %12]
# if month in month_12:
#     print(prt_month,',',day)

# print("Season is",season(month))

#10
# birth_day=int(input("input birthday: "))
# birth_month=input("input month of birth: ")
# if((birth_day>=20 and birth_day<=31)and birth_month=='January' ) or((birth_day>=1 and birth_day<=18)and birth_month=="February"):
#     print("Your Astrological sign is: Aquarius")
# elif((birth_day>=19 and birth_day<29)and birth_month=="February")or((birth_day>=1 and birth_day<=20)and birth_month=="March"):
#     print("Your Astrological sign is: Pisces")
# elif((birth_day>=21 and birth_day<=31)and birth_month=="March")or((birth_day>=1 and birth_day<=19 )and birth_month=="April"):
#     print("Your Astrological sign is: Aries")
# elif((birth_day>=20 and birth_day<=30) and birth_month=="April") or ((birth_day>=1 and birth_day<=20) and birth_month=="May"):
#     print("Your Astrological sign is: Taurus")
# elif((birth_day>=21 and birth_day<=31) and birth_month=="May") or ((birth_day>=1 and birth_day<=20)and birth_month=="June"):
#     print("Your Astrologic sign is: Gemini")
# elif((birth_day>=21 and birth_day<=30) and birth_month=="June") or ((birth_day>=1 and birth_day<=22)and birth_month=="July"):
#     print("Your Astrologic sign is: Cancer")
# elif((birth_day>=23 and birth_day<=31) and birth_month=="July") or ((birth_day>=1 and birth_day<=22)and birth_month=="August"):
#     print("Your Astrologic sign is: Leo")
# elif((birth_day>=23 and birth_day<=31) and birth_month=="August") or ((birth_day>=1 and birth_day<=22)and birth_month=="September"):
#     print("Your Astrologic sign is: Virgo")
# elif((birth_day>=23 and birth_day<=30) and birth_month=="September") or ((birth_day>=1 and birth_day<=22)and birth_month=="October"):
#     print("Your Astrologic sign is: Libra")
# elif((birth_day>=23 and birth_day<=31) and birth_month=="October") or ((birth_day>=1 and birth_day<=21)and birth_month=="November"):
#     print("Your Astrologic sign is: Scorpio")
# elif((birth_day>=22 and birth_day<=30) and birth_month=="November") or ((birth_day>=1 and birth_day<=21)and birth_month=="December"):
#     print("Your Astrologic sign is: Sagittarius")
# elif((birth_day>=22 and birth_day<=31) and birth_month=="December") or ((birth_day>=1 and birth_day<=19)and birth_month=="January"):
#     print("Your Astrologic sign is: Capricorn")
# else:
#     print("noo")


#11
# n=int(input("Input your birth year: "))
# if n%12==0:
#     print("Your Zodiac sign: Monkey")
# elif n%12==1:
#     print("Your zodiak sign: Rooster")
# elif n%12==2:
#     print("Your zodiak sign: Dog")
# elif n%12==3:
#     print("Your zodiak sign: Pig")
# elif n%12==4:
#     print("Your zodiak sign: Rat")
# elif n%12==5:
#     print("Your zodiak sign: Ox")
# elif n%12==6:
#     print("Your zodiak sign: Tiger")
# elif n%12==7:
#     print("Your zodiak sign: Rabbit")
# elif n%12==8:
#     print("Your zodiak sign: Dragon")
# elif n%12==9:
#     print("Your zodiak sign: Snake")
# elif n%12==10:
#     print("Your zodiak sign: Horse")
# elif n%12==11:
#     print("Your zodiak sign: Goat")

#12
# a=int(input("input first number: "))
# b=int(input("input second number: "))
# c=int(input("input third number: "))
# if a<=b<=c or c<=b<=a:
#     print("The median is",b)
# elif a<=c<=b or b<=c<=a:
#     print("The median is",c)
# else:
#     print("The median is",a)

#13
# import datetime
# year=int(input("input a year: "))
# month=int(input("input a month: "))
# day=int(input("input a day: "))
# date=datetime.date(year,month,day)
# next=date+datetime.timedelta(days=1)
# print("The next date is ",next)

#14
# sum=0
# cnt=0
# while True:
#     n=int(input())
#     if n==0:
#         break
#     sum+=n
#     cnt+=1

# print("sum=",sum)
# print("average=",sum/cnt)

#15
# n=int(input("input a number: "))
# for i in range(1,10+1):
#     print(n,"*",i,"=",i*n)

#16
# n=9
# for i in range(1,n+1):
#     for j in range(i):
#       print(i,end=' ')
#     print()

#17
# datalist = [1452, 11.23, 1+2j, True, 'student', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# for i in datalist:
#     print(i,type(i))

#18
# n=6
# for i in range(0,n):
#     if i==3:
#         continue
#     print(i)