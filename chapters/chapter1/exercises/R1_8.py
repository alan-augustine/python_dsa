# get positive index corresponding to a negative index
def get_positive_index(sequence, negative_index):
    return len(sequence) + negative_index

s = "0123456789"

negative_index = -1
print(s[negative_index] == s[get_positive_index(s,negative_index)])

negative_index = -2
print(s[negative_index] == s[get_positive_index(s,negative_index)])

negative_index = -10
print(s[negative_index] == s[get_positive_index(s,negative_index)])
