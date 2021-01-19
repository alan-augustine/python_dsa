def remove_punctuations(data):
    punctuations = "'\"?!.:;-_()[]/,"
    # print(punctuations)
    new_data=''
    for i in range(len(data)):
        if data[i] not in punctuations:
            new_data += data[i]
    return new_data

print('----------------------')
s="A?B"
print(remove_punctuations(s))

print('----------------------')
s="...?B()[]"
print(remove_punctuations(s))
