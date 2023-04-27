import tkinter as tk

class VehicleManagementGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Vehicle Management System")
        self.pack()

        # Add Vehicle Frame
        self.add_vehicle_frame = tk.LabelFrame(self, text="Add Vehicle")
        self.add_vehicle_frame.pack(side="left", padx=10, pady=10)

        tk.Label(self.add_vehicle_frame, text="Vehicle Type:").grid(row=0, column=0)
        self.vehicle_type_var = tk.StringVar()
        self.vehicle_type_var.set("Car")
        tk.OptionMenu(self.add_vehicle_frame, self.vehicle_type_var, "Car", "Motorcycle", "Bus", "Subway").grid(row=0, column=1)

        tk.Label(self.add_vehicle_frame, text="Brand:").grid(row=1, column=0)
        self.brand_var = tk.StringVar()
        tk.Entry(self.add_vehicle_frame, textvariable=self.brand_var).grid(row=1, column=1)

        tk.Label(self.add_vehicle_frame, text="Model:").grid(row=2, column=0)
        self.model_var = tk.StringVar()
        tk.Entry(self.add_vehicle_frame, textvariable=self.model_var).grid(row=2, column=1)

        tk.Label(self.add_vehicle_frame, text="Year:").grid(row=3, column=0)
        self.year_var = tk.IntVar()
        tk.Entry(self.add_vehicle_frame, textvariable=self.year_var).grid(row=3, column=1)

        tk.Label(self.add_vehicle_frame, text="Color:").grid(row=4, column=0)
        self.color_var = tk.StringVar()
        tk.Entry(self.add_vehicle_frame, textvariable=self.color_var).grid(row=4, column=1)

        tk.Label(self.add_vehicle_frame, text="Plate Number:").grid(row=5, column=0)
        self.plate_number_var = tk.StringVar()
        tk.Entry(self.add_vehicle_frame, textvariable=self.plate_number_var).grid(row=5, column=1)

        tk.Button(self.add_vehicle_frame, text="Add Vehicle", command=self.add_vehicle).grid(row=6, column=1)

        # Statistics Frame
        self.stats_frame = tk.LabelFrame(self, text="Statistics")
        self.stats_frame.pack(side="right", padx=10, pady=10)

        tk.Label(self.stats_frame, text="Number of Vehicles:").grid(row=0, column=0)
        self.num_vehicles_label = tk.Label(self.stats_frame, text="0")
        self.num_vehicles_label.grid(row=0, column=1)

        tk.Label(self.stats_frame, text="Number of Cars:").grid(row=1, column=0)
        self.num_cars_label = tk.Label(self.stats_frame, text="0")
        self.num_cars_label.grid(row=1, column=1)

        tk.Label(self.stats_frame, text="Number of Motorcycles:").grid(row=2, column=0)
        self.num_motorcycles_label = tk.Label(self.stats_frame, text="0")
        self.num_motorcycles_label.grid(row=2, column=1)

        tk.Label(self.stats_frame, text="Number of Buses:").grid(row=3, column=0)
        self.num_buses_label = tk.Label(self.stats_frame, text="0")
        self
