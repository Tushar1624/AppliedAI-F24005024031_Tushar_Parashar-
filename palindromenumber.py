a=int(input("Enter a number: "))
temp=a
rev=0
while temp>0:
    dig=temp%10
    rev=rev*10+dig
    temp=temp//10
if a==rev:
    print(a, "is a palindrome.")
else:
    print(a, "is not a palindrome.")