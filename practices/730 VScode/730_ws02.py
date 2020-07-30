class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

#p1 = Point(1,3) # p1은 포인트의 인스턴스
#p2 = Point(3,1)
#print(p1.x, p2.y)

class Rectangle: # 인스턴스?
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def get_area(self): # append를 더 잘알아야겠다.
        width = abs(self.p1.x - self.p2.x)  ## 접근법이 포인트 
        height = abs(self.p1.y - self.p2.y)
        return width * height
    
    def get_perimeter(self):
        width = abs(self.p1.x - self.p2.x)  ## 접근법이 포인트 
        height = abs(self.p1.y - self.p2.y)
        return 2*(width + height)

    def is_square(self):
        width = abs(self.p1.x - self.p2.x)  ## 접근법이 포인트 
        height = abs(self.p1.y - self.p2.y)
        return width == height

#        if witdh == height:
#            return True
#        else:
#            return False

p1 = Point(1,3)
p2 = Point(3,1)
r1 = Rectangle(p1,p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3,7)
p4 = Point(6,4)
r2 = Rectangle(p3,p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

