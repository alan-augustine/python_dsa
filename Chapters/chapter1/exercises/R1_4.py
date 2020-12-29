def sum_squares_smaller_than_n(n):
    # we have usesgenerator comprehension - not tuple comprehension
    # generator comprehension are more efficient for large
    # data-sets due to their lazy evaluation
    # refer page.43
    return sum((pow(i,2) for i in range(n)))

k = 1
print("Sum of squares of all positive integers smaller than", k,
      "=", sum_squares_smaller_than_n(k))

k = 2
print("Sum of squares of all positive integers smaller than", k,
      "=", sum_squares_smaller_than_n(k))

k = 3
print("Sum of squares of all positive integers smaller than", k,
      "=", sum_squares_smaller_than_n(k))

k = 4
print("Sum of squares of all positive integers smaller than", k,
      "=", sum_squares_smaller_than_n(k))

k = 5
print("Sum of squares of all positive integers smaller than", k,
      "=", sum_squares_smaller_than_n(k))
