"""order processing file read demo"""

f = open("order1.txt",'r')

sum = 0.0

for line in f:
    splitLine = line.split()
    product = splitLine[0]
    quantity = int(splitLine[-1])
    if product == 'A':
        unitPrice = 17.46
    elif product == 'B':
        unitPrice = 10.13
    elif product == 'C':
        unitPrice = 2.11
    elif product == 'D':
        unitPrice = 23.13
    elif product == 'E':
        unitPrice = 74.56
    elif product == 'F':
        unitPrice = 1.11
    elif product == 'G':
        unitPrice = 9.34
    elif product == 'H':
        unitPrice = 3.45
    sum += unitPrice * quantity
    print(product, str(quantity), str(unitPrice*quantity))

print("Subtotal $%0.2f"%(sum))

f.close()









""" f2 = open("../conversion_table.txt", 'r')
f3 = open("../01_29_24/demo.cpp",'r')
text = f.read()
print(text)

text = f2.read()
print(text)

text = f3.read()
print(text) """
