bill_amount = float(input(f"What was the total bill?\t"))
tip = int(input(f"What % tip you want to give? (10, 12 or 15?)\t"))
n = int(input(f"How many people do you have to split bill with?\t"))

if (not isinstance(n, int)) or (n <= 0):
	print(f'{n} should be an integer value greater than 0.')

tip_to_pay = tip / 100
amount_after_tip = bill_amount * tip_to_pay
total_bill = bill_amount + amount_after_tip

bill_per_person = total_bill / n
final_amount = round(bill_per_person, 2)
print(f"Each person shall pay {final_amount}/-.")