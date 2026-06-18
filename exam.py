# #Write a program to check whether a number is positive, negative, or zero
# num=int(input("Enter a number="))
# if num==0:
#     print("Zero")
# elif num>0:
#     print("positive")
# else:
#     print("Negative")
#Write a program to check whether a number is even or odd.
# num=int(input("Enter a number="))
# if num<=0:
#     print("Neither Odd nor positive")
# elif num%2==0:
#     print("Number is Even")
# else:
#     print("Number is Odd")
#Write a program to find the largest among three numbers.
# num=int(input("Enter 1st number="))
# num2=int(input("Enter 2nd number="))
# num3=int(input("Enter 3rd number="))
# if num==num2==num3:
#     print("All are equal")
# elif num>num2 and num3:
#     print(num,"is greatest")
# elif num2>num and num3:
#     print(num2,"is greatest")
# else
#     print(num3,"is greatest")
#Write a program to check whether a given year is a leap year or not.
# days=int(input("Enter the number of days in the year:"))
# if days==365:
#     print('Normal Year')
# elif days == 366:
#     print("Leap Year")
# else:
#     print("Not Valid")
#Write a program to check whether a person is eligible to vote (age ≥ 18).
# age=int(input("Enter your age="))
# if age <=0:
#     print("Enter age correctly")
# elif age>=18:
#     print("Eligible")
# else:
#     print("Not Eligible")
#Print numbers from 1 to 50 using a loop.
# for i in range (1,51):
#     print(i,end=" ")
#Print the multiplication table of a number entered by the user.
# table=int(input('Enter the number of which table is required:'))
# for i in range(table):
#     print(table,"*",i,"=",table*i)
#Find the sum of first N natural numbers
# n=int(input("Enter the number of natural numbers whose sum you need:"))
# sum=0
# for i in range (1,n+1):
#     sum+=i
# print("The Sum of",n,"Natural numbers are:",sum)
#Find the factorial of a given number.
# num=int(input("Enter the number whose factorial you need:"))
# fact=1
# if num<=1:
#     print("No Factorial")
# else:
#     for i in range(1,num+1):
#         fact*=i
# print('The factorial is:',fact)
#Print all prime numbers between 1 and 100.Doubt
# check=0
# for i in range(2,100):
#     for j in range(i-1,1):
#         if i%j==0:
#             check+=1
#     if(check==0):
#          print(i)
# print("Above are the prime numbers between 1 and 100")
#Take 5 numbers in a list and print them.
# lst=[]
# for i in range(5):
#     value=int(input("Enter a number:"))
#     lst.append(value)
# print(lst)
#Find the largest and smallest element in a list.
# lst=[]
# for i in range(5):
#      value=int(input("Enter a number:"))
#      lst.append(value)
# print("Largest Value=",max(lst),"\nThe smallest value=",min(lst))
#Find the sum and average of elements in a list.
# lst=[]
# total=0
# for i in range(5):
#        value=int(input("Enter a number:"))
#        lst.append(value)
# for i in lst:
#        total+=i    
# print("The total is:",total,"\nThe Average is:",total/len(lst))
#Count the number of even and odd numbers in a list.
# lst=[]
# for i in range(5):
#     value=int(input("Enter a number:"))
#     lst.append(value)
# odd=0
# even=0
# zero=0
# for i in lst:
#     if i==0:
#         zero+=1
#     elif i%2==0:
#         even+=1
#     else:
#         odd+=1
# print("Even=",even,"Zero=",zero,"Odd=",odd)
#Reverse a list without using built-in reverse() function.
# lst=[]
# for i in range(5):
#     value=int(input("Enter a number:"))
#     lst.append(value)
# rev=[]
# for i in range(4,-1,-1):
#     rv[i]=i
# print(rev)
# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# for i in "ABCDE":doubt
#     for j in i:
#         print(i,end="")
#     print()
# for i in range(5,0,-1):
#     for j in range(i):
#         print("8",end="")
#     print()
        