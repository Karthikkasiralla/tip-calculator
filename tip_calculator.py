print("Hola, Welcome to Tip Calculator")
print("I will help you to split the Bill")
bill = float(input("What was the total bill\n"))
tip = int(input("What percentage tip would you like to give?\n"))
people = int(input("How many people to split the bill ?\n"))
tip_as_percent = tip / 100
total_tip_amount = tip_as_percent * bill
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)
print(f"Each person should pay : {final_amount}")