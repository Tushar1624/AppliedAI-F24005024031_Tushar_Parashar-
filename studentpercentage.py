number=int(input('Number of subjects:'))
total=0
a=[]
for i in range(number):
    marks=int(input("Enter marks of subject "+str(i+1)+": "))
    a.append(marks)
    total+=marks
percentage=(total/(number*100))*100
print("The percentage of the student is: ", percentage)