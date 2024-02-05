"""
calories program using lists
"""

sum = 0
avg = 0
count = 8
calData = []

for day in range(1,count+1):
    cal = float(input("Enter the number of calories burned day #" + str(day) + ": "))
    if cal in calData:
        print(cal, " already in list.")
    else:
        #calData.insert(-1 ,cal )
        calData.append(cal)
    sum += cal #sum = sum + cal
avg = sum / count
print("The average number of calories burned is ", avg)

print(calData)

calData.sort()

print(calData)

print("The least number of calories burned per day is ", calData[0])
print("The most number of calories burned per day is ", calData[-1])

midpoint = len(calData) // 2
if len(calData) % 2 == 1:
    median = calData[midpoint]
else:
    median = (calData[midpoint] + calData[midpoint-1])/2

print("The median number fo calories burned per day is ", median)

