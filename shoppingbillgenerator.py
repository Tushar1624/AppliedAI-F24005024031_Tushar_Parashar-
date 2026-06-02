total_items=int(input("Enter total number of items: "))
price_per_item=[]
items=[]
for i in range(total_items):
    item_name=input("Enter name of item "+str(i+1)+": ")
    items.append(item_name)
    price=float(input("Enter price of item "+str(i+1)+": "))
    price_per_item.append(price)
total_price=sum(price_per_item)
discount=total_price*0.1
final_price=total_price-discount
print("A discount of 10% has been applied.")
print("The total price of the shopping bill after discount is: ", final_price)
print("The items purchased are: ", items)