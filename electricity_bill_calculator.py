units = int(input("Enter number of units: "))
bill = 0

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.5)
else:
    bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)

print("Total Electricity Bill: ₹", bill)
