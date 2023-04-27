class Vehicle:
    def __init__(self, model, nb_wheels, color, license_plate):
        self.model = model
        self.nb_wheels = nb_wheels
        self.color = color
        self.license_plate = license_plate
        self.is_available = True

    def set_color(self, color):
        self.color = color

    def set_license_plate(self, license_plate):
        self.license_plate = license_plate

    def set_available(self, is_available):
        self.is_available = is_available

    def __str__(self):
        return f"{self.model} ({self.color}) with license plate {self.license_plate}"
