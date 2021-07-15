#create a class Point and initialize with the user defined values and write a method to calculate the distance of the point from the origin.
class point:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def dist_from_origin(n,m):
        t =((n**2)+(m**2))**(0.5)
        print("distance of the point from origin =",t)

q1 = point.dist_from_origin(6,15)



#OUTPUT:
#distance of the point from origin = 16.15549442140351
