#Tip calculator

print("Welcome to the tip Calculator\n")
total_bill=float(input ("What is your total bill"))
tip=int(input ("How much tip you want to give 10 12 15"))
people=int(input("How many to split the bill !! "))
#formula
bill_with_tip= (tip/100 * total_bill + total_bill)
print (bill_with_tip)
print(f"Each person should pay: ${bill_with_tip}")