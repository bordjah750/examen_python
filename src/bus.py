from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, model, nb_wheels, color, license_plate, nb_seats):
        super().__init__(model, nb_wheels, color, license_plate)
        self.nb_seats = nb_seats

    def set_nb_seats(self, nb_seats):
        self.nb_seats = nb_seats

    def __str__(self):
        return f"{self.color} {self.model} bus with {self.nb_seats} seats and license plate {self.license_plate}"
