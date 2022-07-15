class Car:
    def __init__(self, make, year, color, narh):
        self.make = make
        self.year = year
        self.color = color
        self.__narh = narh

    def show_narh(self):
        return self.__narh
    
a = Car("Mercedess", 2022, "Black", 2500)    
print(a.show_narh)

