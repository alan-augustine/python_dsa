def sum_of_square_odd_positive_integers(n):
    # added if condition to generator comprehension
    # return sum((i*i for i in range(n) if i%2!=0))
    # below is a better solution - again using generator comprehension
    return sum((i*i for i in range(1, n, 2)))


k = 1
print("Sum of odd positive integers smaller than", k,
      "=", sum_of_square_odd_positive_integers(k))

k = 2
print("Sum of odd positive integers smaller than", k,
      "=", sum_of_square_odd_positive_integers(k))

k = 3
print("Sum of odd positive integers smaller than", k,
      "=", sum_of_square_odd_positive_integers(k))

k = 4
print("Sum of odd positive integers smaller than", k,
      "=", sum_of_square_odd_positive_integers(k))

k = 6
print("Sum of odd positive integers smaller than", k,
      "=", sum_of_square_odd_positive_integers(k))
