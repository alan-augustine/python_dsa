# initial thougts - cannot do without multi-threading

# below is not the correct solution

import sys

# a name
class Computer:
    def __init__(self, name):
        self.__name = name
        self.__data = None
    
    def get_data_packet(self):
        return self.__data

    def set_data_packet(self, a):
        self.__data = a


class Network:
    def __init__(self):
        pass

    def send_packet(self, a, b):
        if not isinstance(a, Computer):
            print('Instance should be of Type Computer')
            sys.exit(1)
        if not isinstance(b, Computer):
            print('Instance should be of Type Computer')
            sys.exit(1)
        
        b.set_data_packet(a.get_data_packet())
        a.set_data_packet(None)        

a = Computer('Alice')
b = Computer('Bob')
n = Network()

a.set_data_packet('a')
n.send_packet(a, b)
print(b.get_data_packet(), a.get_data_packet())