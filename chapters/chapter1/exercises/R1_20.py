import random

def my_shuffle(data):
    l = len(data)
    for i in range(l):
        r = random.randint(0,l-1) # start and stop are inclusive for randint()
        data[i], data[r] = data[r], data[i] # swap all indices to a random index
        

a = [0, 1, 2, 3, 4, 5]
print(a)
random.shuffle(a)
print(a)
print('-------------------------------')
b = [0, 1, 2, 3, 4, 5]
print(b)
my_shuffle(b)
print(b)

# idea is to randomize indices, insteads of actual values
