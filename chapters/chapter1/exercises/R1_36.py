words = input("Enter words separated by spaces: ")
count = {}

# if no delimiter, split according to any whitespace
for word in words.split():
    if word in count.keys():
        count[word] += 1
    else:
        count[word] = 1
print(count)
