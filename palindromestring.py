a=input("Enter a string: ")
rev=a[::-1]
if a==rev:
    print(a, "is a palindrome.")
else:
    print(a, "is not a palindrome.")