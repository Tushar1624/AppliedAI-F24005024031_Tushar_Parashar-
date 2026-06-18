#Create an array and print
lst=[]
for i in range(5):
    a=int(input("Enter a number:"))
    lst.append(a)
for i in range(len(lst)):
    print(lst[i])
#Find the largest number in list
print("The largest number in the list is:",max(lst))
#Find the smallest number in list
print("The smallest number in the list is:",min(lst))
#Sorting a list
print(sorted(lst))
#Creating a dictionary
dict={"Hello":"World","Ram":"Shyam"}
print("The dictionary is:",dict)
#Create a function to add two numbers
def add(a,b):
    result=a+b
    return result
num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
print("The sum is:",add(num1,num2))