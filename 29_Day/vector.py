#vector class
import math
from xmlrpc.client import FastMarshaller

class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    #called when + is used
    def __add__(self,oOther):
        return Vector(self.x + oOther.x, self.y + oOther.y)
    
    def __sub__(self,oOther):
        return Vector(self.x - oOther, self.y - oOther)
    
    def __mul__(self,oOther):
        #special code to allow for multiplying by a vector or a scalar .
        if isinstance(oOther,Vector):
            return Vector((self.x* oOther.x),(self.y*oOther.y))
        elif isinstance(oOther, Vector):
            return Vector ((self.x * oOther),(self.y*oOther))
        else:
            raise TypeError("The value must be a vector or a scalar.")
    
    def __abs__(self):
        return math.sqrt((self.x**2),(self.y**2))   
    
    def __eq__(self,oOther):
        return (self.x == oOther.x) and (self.y == oOther.y)
    
    def __ne__(self,oOther):
        return (self.x != oOther.x) and (self.y != oOther.y)

    def __lt__(self,oOther):
        if abs(self) < abs(oOther):
            return True
        else:
            return False
        
    def __gt__(self, oOther):
        if abs(self) > abs(oOther):
            return True
        else:
            return False
        
    def __str__(self):
        return "This vector has the value ("+ str(self.x) +","+ str(self.y)+")"
    