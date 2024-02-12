nums = [1,2,3,4]

def addToList():
    number = input("Enter a number to add to the list: ")
    if number == "" or not number.isnumeric():
        print("Value entered is not a number and cannot be added.")
    else:
        nums.append(int(number))


def findlargest(numLargest = 1):
    largest = nums[0]
    largestList = []
    for j in range(numLargest):
        largest = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > largest and not nums[i] in largestList:
                largest = nums[i]
        largestList.append(largest)
    print(i,j)
    return largestList
    

addToList()
print(findlargest(3))

    