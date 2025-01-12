'''
87.	**Class** Point
•	Represent a point in 2D space. 
    Add methods to set coordinates and calculate distance from another Point object.
'''
class co_ordinates:
    def __init__(self,x,y):                 # Take input for x and y coordinate
        self.x_coordinate = x
        self.y_coordinate = y
    def distance(self,obj2):                # Apply the distance formula
        dist = (((self.x_coordinate) - (point2.x_coordinate))**2 + ((self.y_coordinate)- (point2.y_coordinate))**2)**0.5
        return dist

point1 = co_ordinates(4,3)                  # point1 object created
point2 = co_ordinates(0,0)                  # point2 object created

print(point1.distance(point2))      # Calling the distance function with point2 as the parameter
