from rational import Rational
import random

r = Rational(random.randint(1,10),random.randint(1,100))
print(r)
s = Rational(random.randint(1,10), random.randint(1,100))
print(s)
print(r + s)
print(r - s)
print(r * s)
print(r / s)
print(r < s)
print(r <= s)
print(r != s)
