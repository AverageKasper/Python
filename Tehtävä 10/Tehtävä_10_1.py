class Elevator:
    def __init__(self, bottom_floor, top_floor) -> None:
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    # Function moves to the inputted floor
    def move_to_floor(self,floor):
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

    # Elevator goes up
    def floor_up(self, floor):
        self.current_floor += floor
        
    # Elevator goes down
    def floor_down(self, floor):
        self.current_floor -= floor

hotel = Elevator(1, 10)
hotel.move_to_floor(7)
hotel.move_to_floor(1)