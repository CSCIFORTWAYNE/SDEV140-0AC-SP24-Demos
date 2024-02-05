"""number converter program"""


hexDigits = {'0':"0000",'1':"0001",'2':"0010",'3':"0011",'4':"0100",'5':"0101",'6':"0110",'7':"0111",'8':"1000",'9':"1001",'A':"1010",'B':"1011",'C':"1100",'D':"1101",'E':"1110",'F':"1110","0000":'0',"0001":'1',"0010":'2',"0011":'3',"0100":'4',"0101":'5',"0110":'6',"0111":'7',"1000":'8',"1001":'9',"1010":'A',"1011":'B',"1100":'C',"1101":'D',"1110":'E',"1110":'F'}
binaryNum = input("Enter a binary string: ")
decimalNum = 0
exponent = len(binaryNum) - 1
for digit in binaryNum:
    if digit == '0' or digit == '1':
        decimalNum += int(digit) * 2 ** exponent
        exponent -= 1
    else:
        print("Error: The string contains non binary digits")
        break
print("%0s in decimal is %0d" %(binaryNum,decimalNum))

while len(binaryNum) % 4 != 0:
    binaryNum = "0" + binaryNum

hexNum = ""
for group in range(0, len(binaryNum),4):
    something = binaryNum[group:group+4]
    hexNum += hexDigits[something]
print("%0s in hexadecimal is %0s"%(binaryNum, hexNum))

decimalNum = input("Enter a decimal: ")
originalNum = decimalNum

decimalParts = decimalNum.split('.')
if decimalParts[0].isdigit() and decimalParts[-1].isdigit():
    decimalNum = int(decimalParts[0])
    fractionPart = float("." + decimalParts[-1])
    binaryNum = ""
    if decimalNum == 0:
        binaryNum = "0"
    else:
        while decimalNum > 0:
            remainder = decimalNum % 2
            decimalNum = decimalNum // 2
            binaryNum = str(remainder) + binaryNum
    binaryNum += "."
    for digits in range(0,16):
        x = fractionPart * 2
        parts = str(x).split('.')
        binaryNum += parts[0]
        fractionPart = float("." + parts[1])
        if fractionPart == 0:
            break


    print("%0s in binary is %0s" %(originalNum,binaryNum))

hexNum = input("Enter a hexadecimal number: ")
binaryNum = ""

for digit in hexNum:
    if digit.upper() in hexDigits:
        binaryNum += hexDigits[digit.upper()]
    else:
        print("Error: The string contains non hexadecimal digits")
        break
print("%0s in binary is %0s" %(hexNum,binaryNum))

