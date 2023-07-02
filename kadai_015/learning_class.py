class Human:
  def __init__(self):
   self.name = ""
   self.age = ""
  
  def set(self, name, age):
    self.name = name
    self.age = age

  def printinfo(self):
    print(self.name)
    print(self.age)

data1 = Human()
data1.set("Hirotoshi Naito",37)

data1.printinfo()
