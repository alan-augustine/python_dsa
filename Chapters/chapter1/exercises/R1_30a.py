# as per hint - This is the same as the logarithm, but you can use recursion here
# rather than calling the log function.
import sys
import math
def times_to_divde_by_two(n):
    if n < 2:
        print("Number must be greater than two")
        sys.exit(1)
         # n should also be an integer
    t = 1
    while True:
        q = n / 2
        if q >= 2:
            t += 1
            n = q
        else:
            break
    return t

print(times_to_divde_by_two(2))
print(times_to_divde_by_two(3))
print(times_to_divde_by_two(4))
print(times_to_divde_by_two(5))
print(times_to_divde_by_two(6))
print(times_to_divde_by_two(8))
print(times_to_divde_by_two(100))

print(int(math.log(2,2)))
print(int(math.log(3,2)))
print(int(math.log(4,2)))
print(int(math.log(5,2)))
print(int(math.log(6,2)))
print(int(math.log(8,2)))
print(int(math.log(100,2)))
