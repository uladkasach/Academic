""" 
    Uladzimir Kasacheuski
    6/19
"""

class Rectangle(object):
  def __init__(self, w = "10", h = "10"):
    object.__init__(self)
    self.width = w;
    self.height = h;
    self.setStats();
    
  def sayHi(self):
    print "Hi, may name is %s!" % self.name;
    
  def setStats(self):
    self.area = int(self.width) * int(self.height);
    self.perimeter = 2 * int(self.width) + 2 * int(self.height);
    
  def getStats(self):
    self.setStats();
    string = "";
    string += "width:      %d" % self.width
    string += "\nheight:     %d" % self.height
    string += "\narea:       %d" % self.area
    string += "\nperimeter:  %d" % self.perimeter
    
    return string;
    
def main():
    print "Rectangle a:"
    a = Rectangle(5, 7)
    print "area:      %d" % a.area
    print "perimeter: %d" % a.perimeter
    
    print "Rectangle b:"
    b = Rectangle()
    b.width = 10
    b.height = 20
    print b.getStats()
    
    
main();    