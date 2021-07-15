#Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price. Assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and whose price is 25.0.


class Bike:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.color = initX
        self.price = initY

testone = Bike('blue',89.99)   
testtwo = Bike('purple',25.0)






