class Elevator:
    def __init__(self, bottom_floor, top_floor) -> None:
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    # Function moves to the inputted floor
    def move_to_floor(self,floor):

        # Check that input floor is not out of range
        if floor > self.top_floor or floor < self.bottom_floor:
            print("Virheellinen kerros, ohjelma suljetaan.")
            return
        
        # Moves floor to inputted floor
        while self.current_floor is not floor:
            if self.current_floor > floor:
                print(f"Nykyinen kerros: {self.current_floor}")
                Elevator.floor_down(self,1)
            elif self.current_floor < floor:
                print(f"Nykyinen kerros: {self.current_floor}")
                Elevator.floor_up(self,1)
        else:
            print(f"Saavuit kerrokseen: {self.current_floor}")

        print(f"\nHissi palaa pohjakerrokseen.")

    # Elevator goes up
    def floor_up(self, floor):
        self.current_floor += floor
        
    # Elevator goes down
    def floor_down(self, floor):
        self.current_floor -= floor

# Building class
class Building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.elevator_count = [Elevator(bottom_floor, top_floor) for _ in range(elevator_count)]
    
    def move_elevator(self, elevator_num, target):
        if elevator_num < len(self.elevator_count):
            print(f"\nLiikutaan hissillä {elevator_num + 1}")
            self.elevator_count[elevator_num].move_to_floor(target)


house = Building(1,12,4)
Building.move_elevator(house,0,7)
Building.move_elevator(house,1,3)
Building.move_elevator(house,2,12)
Building.move_elevator(house,3,2)

