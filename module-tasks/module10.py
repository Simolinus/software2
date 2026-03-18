import random


class Elevator:
    def __init__(self, bottom_floors, top_floors):
        self.bottom_floors = bottom_floors
        self.top_floors = top_floors
        self.current_floor = 0

    def go_to_floor(self):
        target_floor = int(input("Enter target floor: "))
        if target_floor <= self.top_floors:
            if target_floor > self.current_floor:
                self.floor_up(self.current_floor, target_floor)
        else:
            print("Floor does not exist")
        if target_floor >= self.bottom_floors:
            if target_floor < self.current_floor:
                self.floor_down(self.current_floor, target_floor)
        else:
            print("Floor does not exist")
        return self.current_floor

    def floor_up(self, floor, target_floor):
        while floor < target_floor:
            floor += 1
            print(floor)
        self.current_floor = floor
        return self.current_floor

    def floor_down(self, floor, target_floor):
        while floor > target_floor:
            floor -= 1
            print(floor)
        self.current_floor = floor
        return self.current_floor

    def elevator_fire_alarm(self):
        if self.current_floor == self.bottom_floors:
            print("Already at bottom floor")
        while self.current_floor < self.bottom_floors:
            self.current_floor += 1
            print(self.current_floor)
            if self.current_floor == self.bottom_floors:
                print("Arrived at bottom floor")
        while self.current_floor > self.bottom_floors:
            self.current_floor -= 1
            print(self.current_floor)
            if self.current_floor == self.bottom_floors:
                print("Arrived at bottom floor")
        print("\n")


class Building:
    def __init__(self, bottom_floors, top_floors, elevators):
        self.bottom_floors = bottom_floors
        self.top_floors = top_floors
        self.elevators = elevators
        self.elevators_list = []

    def elevator_list(self):
        for i in range(self.elevators):
            elevator = Elevator(self.bottom_floors, self.top_floors)
            self.elevators_list.append(elevator)

    def run_elevator(self, which_elevator):
        elevator = self.elevators_list[which_elevator]
        elevator.go_to_floor()

    def fire_alarm(self):
        print("-----Fire alarm-----")
        for i in range(len(self.elevators_list)):
            elevator = self.elevators_list[i]
            print(f"Elevetor NO.{i}")
            elevator.elevator_fire_alarm()


class Car:
    def __init__(self, registration, max_speed, current_speed, travelled_distance):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed):
        accel_km_h = speed
        if self.current_speed <= self.max_speed:
            self.current_speed = self.current_speed + accel_km_h
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed
            if self.current_speed <= 0:
                self.current_speed = 0
        else:
            self.current_speed = self.max_speed

    def drive(self, hours):
        distance_travelled = self.current_speed * hours
        self.travelled_distance = self.travelled_distance + distance_travelled


class Race:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
        self.participants = []
        self.time = 0

    def hour_passes(self):
        self.time += 1
        for i in range(len(self.participants)):
            car = self.participants[i]
            acceleration = random.randrange(-10, 15)
            car.accelerate(acceleration)
            car.drive(self.time)

    def print_status(self):
        print(f"-----HOURS [{self.time}] PASSED-----")
        print(
            f"{'Registration':<15}{'Max speed':<12}{'Current speed':<15}{'Distance':<10}"
        )
        print(
            f"{'------------':<15}{'---------':<12}{'-------------':<15}{'--------':<10}"
        )
        for i in range(len(self.participants)):
            car = self.participants[i]
            print(
                f"{car.registration:<15}{str(car.max_speed) +' km/h':<12}{str(car.current_speed)+' km/h':<15}{str(car.travelled_distance)+' km':<10}"
            )
        print(
            f"{'------------':<15}{'---------':<12}{'-------------':<15}{'--------':<10}"
        )

    def race_finished(self):
        winner = None
        for i in range(len(self.participants)):
            car = self.participants[i]
            if car.travelled_distance >= self.distance:
                if winner is None or car.travelled_distance > winner.travelled_distance:
                    winner = car
        if winner:
            return True, winner.registration
        return False, None


def main():
    bottom_floors = int(input("Enter bottom floors: "))
    top_floors = int(input("Enter top floors: "))
    elevators = int(input("Enter how many elevators: "))
    building = Building(bottom_floors, top_floors, elevators)
    building.elevator_list()
    print("To stop using elevator enter 'stop'")
    while True:
        elevator_number = input("Enter elevator number: ")
        if elevator_number == "stop":
            break
        building.run_elevator(int(elevator_number))
    building.fire_alarm()


def main2():
    race = Race("Grand Demolition Derby", 8000)
    for i in range(10):
        car_registration = f"ABC-{1+i}"
        car_max_speed = random.randrange(100, 200)
        car = Car(car_registration, car_max_speed, 0, 0)
        race.participants.append(car)
    while True:
        if race.time % 10 == 0:
            race.print_status()
        race.hour_passes()
        is_finished, winner = race.race_finished()
        if is_finished == True:
            race.print_status()
            print(f"Winner is {winner}!")
            break


main2()
