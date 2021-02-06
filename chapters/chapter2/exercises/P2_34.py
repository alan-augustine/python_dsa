# based on hints - a bar chart created using charts

import os

p = os.path.dirname(__file__)
print(p)
f = open(p + '/P2_34_text.txt')

s = f.read()
s = s.lower()

count = dict()
for i in range(ord('a'), ord('z')+1):
    i = chr(i)
    count[i] = s.count(i)

print(count)

for i in count:
    print(i, ' ', end='')
    for j in range(count[i]):
        print('*', end='')
    print()
