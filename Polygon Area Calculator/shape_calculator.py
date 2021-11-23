class Rectangle:

  def __init__(self,width,height):
    self.width = width
    self.height = height

  def set_width(self,width:int):
    self.width = width

  def set_height(self,height:int):
    self.height = height

  def get_area(self) -> int:
    return int(self.width * self.height)

  def get_perimeter(self) -> int:
    return int(2 * self.width + 2 * self.height)

  def get_diagonal(self) -> int:
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self) -> str:
    printstring = ""
    if (self.width < 50 and self.height < 50):
      for row in range(self.height):
        printstring += "*" * self.width + "\n"
    else:
      printstring = "Too big for picture."
    return printstring

  def get_amount_inside(self,shape) -> int:
    #this function assumes the passed shape is smaller, return -1 as you did not pass a object of class square or rectangle 
      return int(self.get_area()//shape.get_area())

  def __str__(self):
    return("Rectangle(width={0}, height={1})".format(self.width,self.height))

class Square(Rectangle):
  def __init__(self,side:int):
    self.width = side
    self.height = side
  
  def set_side(self,side:int):
    self.width = side
    self.height = side

  def __str__(self):
    return("Square(side={0})".format(self.width))