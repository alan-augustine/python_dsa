import random

s = list("I will never spam my friends again")
typo_count = 8

# choose 8 random line numbers to make typos
# keeping typo_lines as a separate list is easier to use like below:
# if i in typo_lines:
typo_lines = []
while len(typo_lines) < typo_count:
    n = random.randint(1,100) # start and stop inclusive for randint()
    if n not in typo_lines:   # lets assume all lines should be different
        typo_lines.append(n)
        
print(typo_lines)

# generate [(typo_index, typo_letter),..8 elements] , if typo_count = 8 
typo_details = []
while len(typo_details) < typo_count:
    typo_index = random.randint(0, len(s)-1) # start,stop inclusive for randint()
    typo_letter = chr(random.randint(97, 122)) # ASCII to char
    if s[typo_index] != typo_letter and \
       s[typo_index] != ' ' and \
    (typo_index, typo_letter) not in typo_details:
        typo_details.append((typo_index, typo_letter))
print(typo_details)

c = 0
for i in range(1, 101):
    temp = s[::]
    if i in typo_lines:
        temp[typo_details[c][0]] = typo_details[c][1]
        c += 1
        print('--')
    print(i, ''.join(temp))
        
