age=int(input("Enter your age: "))
if age<=0:
    print("Invalid age entered.")
elif age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")