from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, model, nb_wheels, color, license_plate, nb_doors):
        super().__init__(model, nb_wheels, color, license_plate)
        self.nb_doors = nb_doors

    def set_nb_doors(self, nb_doors):
        self.nb_doors = nb_doors

    def __str__(self):
        return f"{self.color} {self.model} car with {self.nb_doors} doors and license plate {self.license_plate}"
