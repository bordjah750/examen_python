from vehicle import Vehicle

class Metro(Vehicle):
    def __init__(self, model, nb_wheels, color, license_plate, nb_cars):
        super().__init__(model, nb_wheels, color, license_plate)
        self.nb_cars = nb_cars

    def set_nb_cars(self, nb_cars):
        self.nb_cars = nb_cars

    def __str__(self):
        return f"{self.color} {self.model} metro with {self.nb_cars} cars and license plate {self.license_plate}"
