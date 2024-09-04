class Car:
    def __init__(self, register, top_speed,):
        self.register = register
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance = 0
    
    # Accelerate changes the Cars current speed
    def accelerate(self,kmh):
        # Checks if combined speed is less than 0
        if self.current_speed + kmh > 0:
            # Checks if current speed and new speed is more than top speed
            if self.current_speed + kmh < self.top_speed:
                self.current_speed += kmh
            # Checks how much left till top speed is met and adds it 
            else:
                top_to_curr = self.top_speed - self.current_speed
                self.current_speed += top_to_curr
        # if new speed would be less than 0, make speed 0
        else:
            self.current_speed = 0
    
    # Travel calculates how many km has been traveled in given amount of hours
    def travel(self,hour):
        self.distance += self.current_speed * hour 

charger = Car("ABC-123", 142)

charger.accelerate(80)
charger.travel(5)
print(f"Matkustettu {charger.distance} kilometriä")