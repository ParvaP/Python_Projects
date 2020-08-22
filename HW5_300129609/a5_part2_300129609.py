# COPYRIGHT 2019, Vida Dujmovic. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:
    '''Class that represents a rectangle on a plane'''

    def __init__(self,p1,p2,col):
        '''(Rectangle,Point,Point,str)-> None
        initializes the rectangle on the plane'''
        self.p1 = p1
        self.p2 = p2
        self.col = col

    def __repr__(self):
        '''(Rectangle) -> None
        returns a string the represents the rectangle'''
        return 'I am a '+self.get_color()+' rectangle with bottom left corner at ('+str(self.p1.get()[0])+','+str(self.p1.get()[1])+') and top right corner at ('+str(self.p2.get()[0])+','+str(self.p2.get()[1])+').'

    def __eq__(self, other):
        '''(Rectangle,Rectangle) -> bool
        returns true if the two rectangles have the same 2 points defining them and the same color'''
        return self.p1 == other.p1 and self.p2 == other.p2 and self.col == other.col

    def get_bottom_left(self):
        '''(Rectangle) -> Point
        retuns the bottom left point'''
        return self.p1

    def get_top_right(self):
        '''(Rectangle) -> Point
        returns the top right point'''
        return self.p2

    def get_color(self):
        '''(Rectangle) -> str
        returns the color'''
        return self.col

    def reset_color(self,col):
        '''((Rectangle,str) -> None
        changes the color'''
        self.col = col

    def get_perimeter(self):
        '''(Rectangle) -> float
        returns the perimeter'''
        return 2*(self.p2.get()[0]-self.p1.get()[0])+2*(self.p2.get()[1]-self.p1.get()[1])

    def get_area(self):
        '''(Rectangle) -> float
        returns the area'''
        return (self.p2.get()[0]-self.p1.get()[0])*(self.p2.get()[1]-self.p1.get()[1])

    def move(self,dx,dy):
        '''(Rectangle,float,float) -> None
        moves the top right and bottom left points'''
        self.p1.move(dx,dy)
        self.p2.move(dx,dy)

    def intersects (self,rect):
        '''(Rectangle,Rectangle) -> bool
        checks if the two rectangles intersect'''
        return not (self.get_top_right().get()[0] < rect.get_bottom_left().get()[0] or self.get_bottom_left().get()[0] > rect.get_top_right().get()[0] or self.get_top_right().get()[1] < rect.get_bottom_left().get()[1] or self.get_bottom_left().get()[1] > rect.get_top_right().get()[1])

    def contains (self,x,y):
        return self.get_bottom_left().get()[0] <= x and self.get_bottom_left().get()[1] <= y and self.get_top_right().get()[0] >= x and self.get_top_right().get()[1] >= y 

class Canvas:
    '''Class that stores rectangles'''
    def __init__(self):
        '''(Canvas) -> None
        initializes the rectangle'''
        self.rects = []

    def __len__(self):
        '''(Canvas) -> int
        returns the number of rectangles on th canvas'''
        return len(self.rects)

    def __repr__(self):
        '''(Canvas) -> str
        returns a string that reresents the Canvas'''
        prin = 'Canvas(['
        for i in range(len(self.rects)):
            if i == len(self.rects)-1:
                return prin + 'Rectangle('+str(self.rects[i].p1.get())+',' + str(self.rects[i].p2.get())+',\'' + str(self.rects[i].get_color()) + '\')])'
            else:
                prin = prin + 'Rectangle('+str(self.rects[i].p1.get())+','+str(self.rects[i].p2.get())+',\''+str(self.rects[i].get_color())+'\'), '



    def add_one_rectangle (self,rect):
        '''(Canvas,Rectangle) -> None
        adds a rectngle to the canvas'''
        self.rects.append(rect)

    def count_same_color(self,col):
        '''(Canvas,str) -> int
        returns the number of rectangles that are a certain color'''
        self.same_col = 0
        for i in self.rects:
            if i.get_color() == col:
                self.same_col+=1
        return self.same_col

    def total_perimeter(self):
        '''(Canvas) -> None
        returns the total perimeter of all the rectangles'''
        self.total_p = 0
        for i in self.rects:
            self.total_p += i.get_perimeter()
        return self.total_p

    def min_enclosing_rectangle(self):
        '''(Canvas) -> Rectangle
        returns the minimum rectangle that contains all of the other rectangles'''
        min_x = self.rects[0].get_bottom_left().get()[0]
        min_y = self.rects[0].get_bottom_left().get()[1]
        max_x = self.rects[0].get_top_right().get()[0]
        max_y = self.rects[0].get_top_right().get()[1]
        
        for i in self.rects:
            if i.get_bottom_left().get()[0] < min_x:
                min_x = i.get_bottom_left().get()[0]

            if i.get_bottom_left().get()[1] < min_y:
                min_y = i.get_bottom_left().get()[1]
                
            if i.get_top_right().get()[0] > max_x:
                max_x = i.get_top_right().get()[0]

            if i.get_top_right().get()[1] > max_y:
                max_y = i.get_top_right().get()[1]
        return Rectangle(Point(min_x,min_y),Point(max_x,max_y),'red')

    def common_point(self):
        '''(Canvas) -> bool
        returns True if all of the rectangles intersect'''
        for i in self.rects:
            for ii in self.rects:
                if not i.intersects(ii):
                    return False
        return True
        
            
        
        
        
            
            
