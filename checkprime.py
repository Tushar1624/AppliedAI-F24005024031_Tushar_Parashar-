num=int(input("Enter a number:"))
check=0
if num==1 or num<=0:
    print("Enter correct value")
    exit()
for i in range(num-1,1,-1):
    if num%i==0:
        check+=1
if check==0:
    print("Number is prime")
else:
    print("Number is composite")