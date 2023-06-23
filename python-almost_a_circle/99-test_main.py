#!/usr/bin/python3
""" test main """
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    r1 = Rectangle(2, 3) #GOOD
    r2 = Rectangle(2, 3, 1, 99, 4281426)
    print(r1.id)
    print(r2.id)
    #print(Base.__nb_objects)
    print(Base.num_obj())
    
