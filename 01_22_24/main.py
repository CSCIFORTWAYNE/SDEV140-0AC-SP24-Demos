#program to calculate the avg num cals burned per day

sum = 0
avg = 0
count = 7

for day in range(1,count+1):
    #cal = float(input("Enter the number of calories burned day #" + str(day) + ": "))
    cal = day *7
    sum += cal #sum = sum + cal
avg = sum / count
print("The average number of calories burned is ", avg)

print(list(range(100,25,-25)))
