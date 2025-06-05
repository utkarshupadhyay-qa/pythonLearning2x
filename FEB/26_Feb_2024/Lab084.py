class Car:
    name = None
    make = None
    model = None


    def __init__(self, obj_name, obj_make, obj_model): # Parameterise constructor

        # Special function , called automatically whenever Object is created

        self.name = obj_name
        self.make = obj_make
        self.model = obj_model

    def start_engine(self):
        print("Starting a car with name: ", self.name)
        print("Starting a car with make: ", self.make)
        print("Starting a car with model: ", self.model)


lambo = Car("lamborghini", "V3", "2024")
lambo.start_engine()

print("----------------------------------")


ferrari = Car("Parasangue", "V8" , "2023")
ferrari.start_engine()
