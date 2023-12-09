


flower = ("rose")

price = 6.00

petal = 10


class Flower:
    
    def __init__ (self, flower, price, petal):

        self._flower = ("daffodil")
        self._price = 3.99
        self._petal = 100

    def get_flower(self):
        return self._flower

    def get_price(self):
        return self._price

    def get_petal(self):
        return self._petal
    
    


flower = Flower()



print(flower)