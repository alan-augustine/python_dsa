# Sequence types - order of elements are important - i.e they have index:
# list, tuple, str 
def minmax(data):
    min_num = max_num = data[0]
    # print(min_num, max_num)
    for i in data:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
    return min_num,max_num

# tuple
sequence = (4,3,5,6,1,7)
minimum , maximum = minmax(sequence)
print("maximum =", minimum, "maximum =", maximum)

# list
sequence = [4,3,5,6,1,7]
minimum , maximum = minmax(sequence)
print("maximum =", minimum, "maximum =", maximum)

# one element tuple
sequence = (4,)
minimum , maximum = minmax(sequence)
print("maximum =", minimum, "maximum =", maximum)

# one element list
sequence = [4]
minimum , maximum = minmax(sequence)
print("maximum =", minimum, "maximum =", maximum)
