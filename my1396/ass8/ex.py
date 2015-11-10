'''
Created on Nov 10, 2015

@author: ds-ga-1007
'''
class Coordinate():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def sed(self):
        self.a=self.x+2
        
instance=Coordinate(3,4)
instance.sed()
print instance.a
    