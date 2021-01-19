import random

# sequence means a collection where order is important
# i.e the collection elements can be accesses using indices
def my_choice(sequence):
    length = len(sequence)
    random_index = random.randrange(length)
    return sequence[random_index]

# string is a sequence
s = "0123456789"

print(random.choice(s))

print(my_choice(s))
