def my_reverse(data):
    n = len(data)
    for i in range(n//2):
        # simultaenous assignment - Page.45
        data[i], data[-1-i] = data[-1-i], data[i]
        
# odd number of elements
l = [0,1,2,3,4]
print(l)

my_reverse(l)
print(l)

l.reverse()
print(l)

print('---------------')
# even number of elements
l = [0,1,2,3]
print(l)

my_reverse(l)
print(l)

l.reverse()
print(l)
