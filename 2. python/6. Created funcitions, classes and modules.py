####Created a funcition####
def squre(x) :
    return x*x

for x in range(10):
    print(f"the squre of {x} is {squre(x)}")


####Created a class####
class Computer():   #rule : capitialize the initial letter as create a specific class.
    def __init__(self,brand,storage):
        self.brand = brand
        self.year = storage

your_pc = Computer("apple","1T")
print(your_pc.brand)
print(your_pc.year)
