lines=[]
print('Enter few lines, we will print it in reverse order!')
while True:
    try:
        lines.append(input())
    except EOFError: # Ctrl+D as user input is EOF
        break        # end loop for EOF

# print lines in reverse order
for line in lines[::-1]:
    print(line)
