class car:
   def __init__(self,color,acceleration):
      self.color=color
      self.acceleration=acceleration
      self.speed=0
      
   def accelerate(self):
      print("Speeding Up!!!")
      self.speed+=self.acceleration
      return self.speed
      
      
   def apply_brakes(self):
       print("Applying Brakes!!!")
       self.speed-=10
       return self.speed