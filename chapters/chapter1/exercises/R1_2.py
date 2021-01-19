def is_even(k):
    return not bool(k & 1) # bit wise AND operation with 1 (001)

n = 1
print("Is", n, "even?", is_even(n))
n = 2
print("Is", n, "even?", is_even(n))
n = 3
print("Is", n, "even?", is_even(n))
n = 1111111
print("Is", n, "even?", is_even(n))
n = 1111112
print("Is", n, "even?", is_even(n))
