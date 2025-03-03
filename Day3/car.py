class Car:
   
    def __init__(self,name,fuelRate, velocity):
        self.name=name 
        self.fuelRate=self._validation_fuelRate(fuelRate)
        self.velocity=self._validation_velocity(velocity)

        #validation for feulRate
    def _validation_fuelRate(self,fuelRate):
        if  0 <= fuelRate <=100:
            return fuelRate
        else:
            print("Fuel Rate must be between 0 : 100")
            return 100

    #validation for velocity
    def _validation_velocity(self,velocity):
        if 0 <= velocity <=200:
            return velocity
        else:
            print("Velocity must be between 0 : 200")

    def run(self,velocity, distance):
        self.velocity = self._validation_velocity(velocity)
       
        fuel_need_per_km = 1
        fuel_need = fuel_need_per_km * distance

        if self.fuelRate >= fuel_need:
            self.fuelRate -=fuel_need
            print(f"The car {self.name} is running at {self.velocity} km/h for {distance} km.")
            print(f"Remaining fuel: {self.fuelRate}L")
            # self.stop()
        else:
            remaining_dis = distance -(self.fuelRate / fuel_need_per_km)
            self.fuelRate = 0
            self.stop(remaining_dis)

        
            # print(max_distance_to_end_feul)
       
    def stop(self,remaining_dis=0):
        self.velocity = 0
        if remaining_dis > 0:
            print(f"The car {self.name} has stopped due to no fuel or reaching destination.")
            print(f"Car stopped! Fuel empty. Remaining distance: {remaining_dis} km.")
        # else:
        #     print("Car stopped! You have reached your destination.")


    
    def __str__(self):
        return f"Car(name: {self.name}, Fuel: {self.fuelRate}%, Velocity: {self.velocity} km/h)"




car =Car('BMW',100,200)
# print(car)
car.run(150, 120)# Car Class:
# - attributes (name, fuelRate, velocity)
# -methods (run, stop)