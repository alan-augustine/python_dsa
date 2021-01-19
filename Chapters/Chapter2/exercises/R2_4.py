class Flower:
    def __init__(self, name, petals, price):
        # let's make the members protected using single underscore
        self._name = str(name)
        self._petals = int(petals)
        self._price = float(price)

    def get_name(self):
        return self._name

    def get_petals(self):
        return self._petals

    def get_price(self):
        return self._price

    def set_name(self, name):
        self._name = name

    def set_petals(self, petals):
        self._petals = petals

    def set_price(self, price):
        self._price = price