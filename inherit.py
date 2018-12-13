class square:
    def __init__(self,x):
        self.x=x
    def area(self):
        print("area of square is:",self.x*self.x)
class rectangle(square):
    def __init__(self,x,y):
        super(). __init__(x)
        self.y=y
    def area(self):
        super().area()
        print("area of rectangle is",self.x*self.y)
        
r=rectangle(10,5)
r.area()
