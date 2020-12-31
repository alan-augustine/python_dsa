def count_vowels(data):
    vowel_count = 0
    for i in range(len(data)):
        if data[i] in ['a', 'e', 'i', 'o', 'u']:
            vowel_count+=1
    return vowel_count

s = 'abcdefghi'
print(s)
print(count_vowels(s))

s = 'aeiou'
print(s)
print(count_vowels(s))

s = 'bcdfghjk'
print(s)
print(count_vowels(s))
