import math

def main():
    memorySize = 'A'
    while not isFloat(memorySize):
        memorySize = input("Enter the memory size: ")
    memorySize = float(memorySize)
    unit = 'X'
    while not checkUnits(unit):
        unit = input("Enter the memory unit: ")
    memorySize = calculateBytes(memorySize, unit)
    print(memorySize, " bytes")
    print("Minimum MAR size is", math.ceil(math.log2(memorySize)))

def calculateBytes(memSize, unit):
    """
    KB = 2^10 bytes
    MB = 2^20 bytes
    GB = 2^30 bytes
    TB = 2^40 bytes
    return mem size converted into bytes
    """
    memUnits = {'K':2**10,'M':2**20, 'G': 2**30, 'T':2**40, 'B':1}
    if unit.upper() in memUnits:
        memSize = memSize * memUnits[unit.upper()]
    else:
        print("Error: unknown memory units.")
    
    return memSize

def isFloat(x):
    x = x.replace("-","")
    parts = x.split('.')
    if len(parts) == 1 or len(parts) == 2:
        if parts[0].isdigit() and parts[-1].isdigit():
            return True
        else:
            return False
    return False

def checkUnits(u):
    units = ['B', 'K', 'M', 'G', 'T']
    if u.upper() in units:
        return True
    else:
        return False

if __name__ == "__main__":
    main()