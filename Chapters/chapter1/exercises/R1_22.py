def array_product(l1, l2):
    # assume len(l1) = len(l2)
    result = []
    for i in range(len(l1)):
        result.append(l1[i]*l2[i])
    return result

a = [1, 2, 3, 4, 5]
b = [2, 2, 2, 2, 2]
print(a)
print(b)

print(array_product(a, b))
