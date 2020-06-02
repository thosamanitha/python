
class Truck(Car):
    def __init__(self,color="Red", max_speed=0, acceleration=0, tyre_friction=0, max_cargo_weight=0):
        super().__init__(self,color,acceleration,max_speed,tyre_friction)
        