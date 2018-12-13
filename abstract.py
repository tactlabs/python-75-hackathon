from abc import ABC,abstractmethod
class new(ABC):
    def display(self):
        print("example of abstract class and methods")
    @abstractmethod
    def calculate(self,x):
        pass
       
class sub1(new):
    def calculate(self,x):
        print("square value is:",x*x)
        
class sub2(new):
    def calculate(self,x):
        print("square root value is:",x**0.5)
        
s1=sub1()
s1.calculate(16)
s1.display()

s2=sub2()
s2.calculate(2564)
s2.display()
       
