"""temp conversion file output demo"""

lower = float(input("Enter the lower value for the conversion table: "))
upper = float(input ("Enter the upper value for the conversion table: "))
increment = float(input("What do you want to use for your increment: "))
c = "C"
f = "F"
n = "N"

file = open("conversion_table.txt",'w')
file.write("%10s%10s%10s\n"%(c.center(10), f.center(10), n.center(10)))
file.write("_"*30 + "\n")
lower *= 100
upper *= 100
increment *= 100

for temp in range(int(lower), int(upper)+1, int(increment)):
    f = (temp/100)*9/5 + 32
    n = 33/100 * (temp/100)
    file.write("%0.2f".center(10)%(temp/100) + "%0.2f".center(10)%(f) + "%0.2f".center(10)%(n) + '\n')

file.close()
