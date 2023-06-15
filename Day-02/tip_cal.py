print(" welcome to the tip calculator ")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the people? "))

bill_with_tip = total_bill * (1+(tip_percentage/100))
bill_per_person = round((bill_with_tip/people),2)
print(f"Each person should pay {bill_per_person} $")