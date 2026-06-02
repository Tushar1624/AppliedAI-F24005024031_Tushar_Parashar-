balance=float(input("Enter your account balance: "))
withdrawal_amount=float(input("Enter the amount you want to withdraw: "))
if withdrawal_amount <= balance:
    print("Withdrawal successful.")
    print("Remaining balance: ", balance - withdrawal_amount)
else:
    print("Insufficient funds.")