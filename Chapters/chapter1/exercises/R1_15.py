# check if all numbers are distinct from each other
# in other words, check if there are duplicates
def check_if_distinct_numbers(data):
    l = len(data)
    distinct_flag = True
    # loop is similar to the one in R1.14
    for i in range(l-1):
        for j in range(i+1, l):
            # print(i,j)
            if data[i] == data[j]:
                distinct_flag = False
                break
    return distinct_flag

# Sequence - collections where order is important - ie.elements can be accessed
# using index - list, tuple, string

# distinct example - list
a = [1, 2, 3, 4, 5]
print(a,"has distinct elements ?", check_if_distinct_numbers(a))
# duplicate example - list
a = [1, 2, 3, 4, 1]
print(a,"has distinct elements ?", check_if_distinct_numbers(a))

# distinct example - tuple
a = (1, 2, 3, 4, 5)
print(a,"has distinct elements ?", check_if_distinct_numbers(a))
# duplicate example - tuple
a = (1, 2, 3, 1, 5)
print(a,"has distinct elements ?", check_if_distinct_numbers(a))

# distinct example - string
a = 'abcdefg'
print(a,"has distinct elements ?", check_if_distinct_numbers(a))
# duplicate example - string
a = 'aacdefa'
print(a,"has distinct elements ?", check_if_distinct_numbers(a))
