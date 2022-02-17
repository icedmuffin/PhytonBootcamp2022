# program untuk random koin head or tail
import random

result = random.randint(0, 1)

if result == 1:
    print("heads")
else:
    print("tails")
