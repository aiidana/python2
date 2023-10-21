import math
class Point():
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y
    def get_x(self):
        return self.__x
    def set_x(self,x):
        self.__x=x
    def get_y(self):
        return self.__y
    def set_x(self,y):
        self.__y=y
    def get_position(self):
        return self.__x,self.__y
    def move(self,p,q):
        self.__x+=p
        self.__y+=q
    def __add__(self,point_ov):
        return Point(self.__x +point_ov.__x,self.__y+point_ov.__y)
    def __sub__(self,point_ov):
        return Point(self.__x - point_ov.__x, self.__y - point_ov.__y)
    def __mul__(self,pv):
        return Point(self.__x * pv.__x, self.__y * pv.__y)
    def __truediv__(self,ov):
        return Point(self.__x/ov.__x, self.__y/ov.__y)
    def __mod__(self,ov):
        return Point(self.__x%ov.__x,self.__y%ov.__y)
    def __pow__(self,ov):
        return Point(self.__x**ov.__x,self.__y**ov.__y)
    def __lt__(self,ov):
        return Point(self.__x<ov.__x,self.__y<ov.__y)
    def __gt__(self,ov):
        return Point(self.__x>ov.__x,self.__y>ov.__y)
    def __le__(self,ov):
        return Point(self.__x<=ov.__x,self.__y<=ov.__y)
    def __ge__(self,ov):
        return Point(self.__x>=ov.__x,self.__y>=ov.__y)
    def __eq__(self,ov):
        return Point(self.__x==ov.__x,self.__y==ov.__y)
    def __ne__(self,ov):
        return Point(self.__x !=ov.__x,self.__y!=ov.__y)
    
    def __str__(self):
        return f'The coordinates are: {self.__x,self.__y}'
class circle():
    def __init__(self, center, rad=5):
        self.__center=center
        self.__rad=rad   
    def get_rad(self):
        return self.__rad
    def set_rad(self,rad):
        self.__rad=rad
    def get_cent(self,center,rad):
        return f'coordinates {self.__center} rad:{self.__rad}'
    def area(self,rad):
        return math.pi * rad**2
    def length(self,rad):
        return 2 * math.pi *rad
    def distance(self,point1,point2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    def intersection():
        
    # def __str__(self):
    #     return f'The coordinates are: {self.__center,self.__rad}'
point1=Point(5,2)
circle1=circle(point1,2)
point2=Point(4,5)
circle2 = circle(point2)
area=circle(3)
length=circle(3)

print()
print('length=',length.length(3))
print("area=",area.area(3))
print(circle1.get_cent(point1,2))

# point3=point1+point2
# point4=point1-point2
# point5=point1*point2
# point6=point1%point2
# point7=point1**point2
# point8=point1<point2
# point9=point1>point2
# point10=point1<=point2
# point11=point1>=point2
# point12=point1==point2
# point13=point1!=point2
# point3.get_position()
# point4.get_position()
# point5.get_position()
# point6.get_position()
# point7.get_position()
# point8.get_position()
# point9.get_position()
# point10.get_position()
# point11.get_position()
# point12.get_position()
# point13.get_position()
# print(point3)    
# print(point4)
# print(point5)
# print(point6)
# print(point7)
# print(point8)
# print(point9)
# print(point10)
# print(point11)
# print(point12)
# print(point13)

