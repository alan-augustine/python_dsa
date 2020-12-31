# lets try doing it
def original_scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor

def new_scale(data, factor):
    for val in data:
        val *= factor


a = [0, 1, 2, 3, 4]
print(a)

original_scale(a,2)
print(a)

new_scale(a,2)
print(a)

# So, new_scale wont work, since val is immutable
