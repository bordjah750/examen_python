from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, model, nb_wheels, color, license_plate, has_sidecar=False):
        super().__init__(model, nb_wheels, color, license_plate)
        self.has_sidecar = has_sidecar

    def set_has_sidecar(self, has_sidecar):
        self.has_sidecar = has_sidecar

    def __str__(self):
        if self.has_sidecar:
            return f"{self.color} {self.model} motorcycle with sidecar and license plate {self.license_plate}"
        else:
            return f"{self.color} {self.model} motorcycle with license plate {self.license_plate}"
