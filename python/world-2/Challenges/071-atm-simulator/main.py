withdrawal_amount = int(input("Enter the withdrawal amount: $"))

current_bill = 100
bill_count = 0
remaining_amount = withdrawal_amount

while True:
    if remaining_amount >= current_bill:
        remaining_amount -= current_bill
        bill_count += 1
    else:
        if bill_count > 0:
            if bill_count == 1:
                print(f"Total of {bill_count} bill of ${current_bill}")
            else:
                print(f"Total of {bill_count} bills of ${current_bill}")

        if current_bill == 100:
            current_bill = 50
        elif current_bill == 50:
            current_bill = 20
        elif current_bill == 20:
            current_bill = 10
        elif current_bill == 10:
            current_bill = 5
        elif current_bill == 5:
            current_bill = 1

        bill_count = 0

        if remaining_amount == 0:
            break

print("-" * 35)
print("Thank you for using our ATM simulator!")
