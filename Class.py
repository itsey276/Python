class vec(object):
  def __init__(self, x, y):  # class constructor
    self.x = x
    self.y  = y

  def __add__(self, other):  # special method
    
    x = self.x + other.x
    y = self.y + other.y
    return vec(x, y)
  
  def __str__(self):
    return str(self.x) + ' , ' + str(self.y)
  
  def printrec(self):
    print(str(self.x), ',' , str(self.y))









