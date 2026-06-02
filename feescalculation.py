tuition_fess=float(input("Enter the tuition fees: "))
hostel_fees=float(input("Enter the hostel fees: "))
food_fees=float(input("Enter the food fees: "))
uniform_fees=float(input("Enter the uniform fees: "))
total_fees=tuition_fess+hostel_fees+food_fees+uniform_fees
print("The total fees is: ",total_fees)
scholarship_discount=total_fees*0.15
final_fees=total_fees-scholarship_discount
print("The final fees after scholarship discount is: ",final_fees)