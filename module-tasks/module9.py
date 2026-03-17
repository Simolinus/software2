import random


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


def main():
    cars = []
    for i in range(10):
        car_registration = f"ABC-{1+i}"
        car_max_speed = random.randrange(100, 200)
        car = Car(car_registration, car_max_speed, 0, 0)
        print(
            f"\nRegistration: {car.registration}\nMax speed: {car.max_speed}\nCurrent speed: {car.current_speed} km/h\nTravelled distance: {car.travelled_distance} km\n"
        )
        cars.append(car)
    print("-----RACE START-----")
    while True:
        for car in cars:
            acceleration = random.randrange(-10, 15)
            hours_travelled = 1
            car.accelerate(acceleration)
            car.drive(hours_travelled)
            if car.travelled_distance >= 10000:
                winner = car.registration
                break
        if car.travelled_distance >= 10000:
            break
    for car in cars:
        print(
            f"\nRegistration: {car.registration}\nMax speed: {car.max_speed}\nCurrent speed: {car.current_speed} km/h\nTravelled distance: {car.travelled_distance} km\n"
        )
    print("-----RACE END-----")
    print(f"Winner is {winner}!")


main()
