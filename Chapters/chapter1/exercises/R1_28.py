# assume v is list of numbers
# p=2 --> Euclidean
# i**p = pow(i, p)
def norm(v, p=2):
    return pow(sum([i**p for i in v]), 1/p)

l = [4, 3]
print(norm(l))
print(norm(l, 1))
print(norm(l, 3))
