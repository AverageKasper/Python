import random as r
import time

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

class Race:
    def __init__(self, name, lenght_km, car_list):
        self.name = name
        self.lenght_km = lenght_km
        self.car_list = car_list
        

    def hour_passed(self):
        total_hours = 0
        while True:
            total_hours += 1
            for c in self.car_list:
                if c.distance < self.lenght_km:
                    acceleration = r.randint(-10,15)
                    c.accelerate(acceleration)
                    c.travel(1)
                else:
                    break
            if total_hours % 10 == 0:
                self.print_result(total_hours)
            if c.distance >= self.lenght_km:
                self.race_over(total_hours)
                break

    def print_result(self,hour):
        print(f"\nHours passed: {hour}")
        self.car_list.sort(key=lambda c: c.distance, reverse=True)
        for c in self.car_list:
            print(f"Car: {c.register:8} Current Speed {c.current_speed:3.0f}; Top Speed {c.top_speed:3.0f}km/h; Distance {c.distance:7}km")
        time.sleep(2)

    def race_over(self,hour):
        print(f"\nThe Race is over! Time to complete: {hour}.\nHere are the results:")
        self.car_list.sort(key=lambda c: c.distance, reverse=True)
        for c in self.car_list:
            print(f"Car: {c.register:8} Current Speed {c.current_speed:3.0f}; Top Speed {c.top_speed:3.0f}km/h; Distance {c.distance:7}km")
        
cars = []
total_hours = 0
# Loop for car generation
for c in range(10):
    cars.append(Car("ABC-"+str(c+1), r.randint(100,200)))


great_derby = Race("Great Derby", 8000, cars)

print("The race is starting, here are our cars!")
for c in cars:
    print(f"Car: {c.register:8} Top Speed {c.top_speed:3.0f}km/h")
time.sleep(2)

great_derby.hour_passed()