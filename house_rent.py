house_rent=float(input("Enter the house rent: "))
water_cost=float(input("Enter the water cost: "))
electricity_cost=float(input("Enter the electricity cost: "))
people_in_house=int(input("Enter the number of people in the house: "))
total_cost=house_rent+water_cost+electricity_cost
cost_per_person=total_cost/people_in_house
print("The total cost of the house rent is: ", total_cost)
print("The cost per person is: ", cost_per_person)