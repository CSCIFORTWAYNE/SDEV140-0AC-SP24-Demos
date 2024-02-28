from student import Student
import random


s = Student("Juan", 5)
for num in range(1,6):
    s.setScore(num,random.randint(0,100))
print(s)
print(s.getAverageScore())
print(s.getHighScore())
