class Publication:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Publication name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Publication name: {self.name}")
        print(f"Chief editor: {self.chief_editor}")


class Car:
    def __init__(self, registration, max_speed, current_speed, travelled_distance):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    # def __str__(self):
    #     return (
    #         self.registration,
    #         self.max_speed,
    #         self.current_speed,
    #         self.travelled_distance,
    #     )

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


class Electric(Car):
    def __init__(
        self,
        registration,
        max_speed,
        current_speed,
        travelled_distance,
        battery_capacity,
    ):
        super().__init__(registration, max_speed, current_speed, travelled_distance)
        self.battery_capacity = battery_capacity


class Gasoline(Car):
    def __init__(
        self, registration, max_speed, current_speed, travelled_distance, tank_capacity
    ):
        super().__init__(registration, max_speed, current_speed, travelled_distance)
        self.tank_capacity = tank_capacity


def main():
    publication1_name = "Donald Duck"
    publication2_name = "Compartment No. 6"
    page_count = 192
    author = "Rosa Liksom"
    chief_editor = "Aki Hyyppä"
    publication1 = Publication(publication1_name)
    publication2 = Publication(publication2_name)
    book = Book(publication2, author, page_count)
    magazine = Magazine(publication1, chief_editor)
    magazine.print_information()
    print("\n")
    book.print_information()


def main2():
    registration1 = "ABC-15"
    max_speed1 = 180
    battery_capacity = 52.5
    registration2 = "ACD-123"
    max_speed2 = 165
    tank_capacity = 32.3
    electric_car = Electric(registration1, max_speed1, 0, 0, battery_capacity)
    gasoline_car = Gasoline(registration2, max_speed2, 0, 0, tank_capacity)
    electric_car.accelerate(180)
    gasoline_car.accelerate(165)
    electric_car.drive(3)
    gasoline_car.drive(3)
    print(
        f"\n{registration1}, Travelled distance: {electric_car.travelled_distance} km\n"
    )
    print(
        f"\n{registration2}, Travelled distance: {gasoline_car.travelled_distance} km\n"
    )


main()
main2()
