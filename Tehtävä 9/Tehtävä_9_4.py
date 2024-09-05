# Täs menee vittu hulluksi
import random as r

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
        
cars = []
total_hours = 0
# Loop for car generation
for c in range(10):
    cars.append(Car("ABC-"+str(c+1), r.randint(100,200)))

# Hourly Race loop
racing = True
while racing == True:
    total_hours += 1
    for c in cars:
        acceleration = r.randint(-10,15)
        c.accelerate(acceleration)
        c.travel(1)
        if c.distance >= 10000:
            racing = False

# Sorts the cars by distance
def sorting(c):
    return c.distance

cars.sort(key=sorting, reverse=True)

# Prints sorted list of cars
for c in cars:
    print(f"Car: {c.register:8} Current Speed {c.current_speed:3.0f}; Top Speed {c.top_speed:3.0f}km/h; Distance {c.distance:7}km")
# How many hours to finish the race
print(f"Race took {total_hours} hours to finish.")