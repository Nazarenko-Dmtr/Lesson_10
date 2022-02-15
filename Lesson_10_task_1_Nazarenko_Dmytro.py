from random import randint

def list_max (list):
    return (max(list))

print (list_max([randint(1, 100) for _ in range (30)]))
x = [1000, 899, 2022]
print (list_max(x))