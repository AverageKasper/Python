class Car:
    def __init__(monke, register, top_speed,):
        monke.register = register
        monke.top_speed = top_speed
        monke.current_speed = 0
        monke.distance = 0

charger = Car("ABC-123","142 km/h")

print(f"Auton ominaisuudet:\nrekisteritunnus: {charger.register} \nhuippunopeus: {charger.top_speed} "
      f"\ntämänhetkinen nopeus: {charger.current_speed} \nkuljettu matka: {charger.distance}")