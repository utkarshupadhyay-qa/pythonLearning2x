class Car:
    color = None
    model = None

    def car_details(self):
        print("Your car details is: ", self.color, self.model)


car_color = input("Enter the color of your car \n")
car_model = input("Enter the model of your car \n")

car_obj_ref = Car()
car_obj_ref.color = car_color
car_obj_ref.model = car_model

car_obj_ref.car_details()