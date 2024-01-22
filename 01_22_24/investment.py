startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the rate as a %: "))

rate /= 100
totalInterest = 0.0

print("+" + "-" * 4 + "+" + "-" * 18 + "+" + "-" * 10 + "+" + "-" * 16 + "+")
print("|%-4s|%-18s|%-10s|%-16s|" % ("Year", "Starting Balance", "Interest", "Ending Balance"))
print("+" + "-" * 4 + "+" + "-" * 18 + "+" + "-" * 10 + "+" + "-" * 16 + "+")

for year in range (1, years + 1):
    interest = startBalance * rate
    endBalance = startBalance + interest
    print("|%4d|$%-17.2f|$%-9.2f|$%-15.2f|" % (year, startBalance, interest, endBalance))
    totalInterest += interest
    startBalance = endBalance
    print("+" + "-" * 4 + "+" + "-" * 18 + "+" + "-" * 10 + "+" + "-" * 16 + "+")

