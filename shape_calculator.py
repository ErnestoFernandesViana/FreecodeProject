class Rectangle:
    def __init__(self, width, height):#initialize with width and height
        self.width = width 
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return (self.width*2 + self.height*2)

    def get_diagonal(self):
        return ((self.width**2 + self.height**2)**0.5)

    def get_picture(self):
        #print figure with *, if w or h > 50, print it is too big 
        if (self.width <= 50) and (self.height <= 50): 
            return '\n'.join(['*'*self.width for x in range(self.height)]) + '\n'
        else:
            return 'Too big for picture.'

    def get_amount_inside(self, shape):
        #takes another shape and return number of times this shape could fit in main 
        shape_dimensions = (shape.width, shape.height)
        fit_width = int(self.width / shape_dimensions[0])
        fit_height = int(self.height / shape_dimensions[1])
        return fit_height*fit_width
        
    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)

class Square(Rectangle):
    #single side length is passed in 
    def __init__(self, side):
        self.side = side
        self.width = side 
        self.height = side
    
    def set_side(self, value):
        self.side, self.width, self.height = (value, value, value)#set the side of the square    

    def __str__(self):
        return 'Square(side={})'.format(self.side)

    def set_width(self, width):
        self.set_side(width)
    
    def set_height(self, height):
        self.set_side(height)



if __name__ == '__main__':
    rect = Rectangle(3, 6)
    q = Square(5)