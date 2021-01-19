class C():
    def __init__(self):
        self._i = 1

    def __next__(self):
        self._i += 1
        return self._i

    def __iter__(self):
        return self

for i in C():
    print(i)