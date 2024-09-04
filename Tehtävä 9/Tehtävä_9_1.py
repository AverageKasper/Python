class Car:
    def __init__(self, register, top_speed,):
        self.register = register
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance = 0

charger = Car("ABC-123","142 km/h")

print(f"Auton ominaisuudet:\nrekisteritunnus: {charger.register} \nhuippunopeus: {charger.top_current_speed} "
      f"\ntämänhetkinen nopeus: {charger.current_speed} \nkuljettu matka: {charger.distance}")