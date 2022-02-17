import random
import my_module

random_int = random.randint(1, 10)
print("this is random int")
print(random_int)

random_float = random.random()
print("this is random float from 0 to 1")
print(random_float)

random_float3 = random.random()*10
print("this is random float pure")
print(random_float3)

random_float2 = random.uniform(1.0, 5.0)
print("this is random float from 1 to 5")
print(random_float2)

# external module
print(my_module.pi)
