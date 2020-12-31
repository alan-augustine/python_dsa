def write_to_list_at_index(data, index, value):
    try:
        data[index] = value
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")

a = [0, 1, 2, 3, 4, 5]
print(a)

write_to_list_at_index(a, 0, 100)
print(a)

write_to_list_at_index(a, 6, 100)
print(a)
