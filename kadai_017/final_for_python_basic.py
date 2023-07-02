class Human:
  def __init__ (self):
    self.name = ""
    self.age = ""

  def set(self, name, age):
    self.name = name
    self.age = age
  
  def check_adult(self):
    if self.age >= 20:
      print (f"{self.name} is adult.")
    
    else:
      print (f"{self.name} is child.")

data1 = Human()
data2 = Human()
data3 = Human()

data1.set("Hirotoshi", 37)
data2.set("Haruto", 12)
data3.set("Yuhi", 7)

family = [data1, data2, data3]

for i in family:
  Human.check_adult(i)
