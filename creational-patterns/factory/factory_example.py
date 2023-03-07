"""This pattern provides an interfaz to create objects in superclass meanwhile it allows subclass to alter the kind
of objects that will be created.

 In this example, we will have a vehicle factory, but we need to return cars and trucks"""

from abc import ABC
from typing import Optional


# Example object class and subclasses

class Vehicle(ABC):
    def __init__(self) -> None:
        self.wheels: Optional[str] = None
        self.color: Optional[str] = None

    def change_wheels(self, wheels: str) -> str:
        raise NotImplementedError


class Car(Vehicle):
    def change_wheels(self, wheels: str) -> None:
        self.wheels = "car_wheels"


class Truck(Vehicle):
    def change_wheels(self, wheels: str) -> None:
        self.wheels = "truck_wheels"


# Example factory class and subclasses

class VehicleFactory(ABC):
    """This is the vehicle factory interface. Concrete subclasses will implement it.
    It shouldn't be an interface necessary. It could return its own default product also"""

    def create(self) -> Vehicle:
        raise NotImplementedError


    @staticmethod
    def get_wheels_characteristics(self) -> str:
        """Creation is not the main goal of a factory usually. This could have some business logic.
        The main goal of a factory is disconnect this logic from the concrete implementations
        of the product"""

        return "business logic method example"


class CarFactory(VehicleFactory):
    "Our concrete factory will return a son of Vehicle (Car), which is still a Vehicle"

    def create(self) -> Car:
        return Car()


class TruckFactory(VehicleFactory):
    def create(self) -> Truck:
        return Truck()


# Now we can create our concrete objects. As both are vehicles, this will not break his father functionality

my_car = CarFactory().create()
my_truck = TruckFactory().create()


class Application:
    """If we had an application, it could play with our concrete implementations of Vehicle"""
    def __init__(self):
        self.vehicle: Optional[Vehicle] = None

    def choose_vehicle(self, vehicle_config: str):
        if vehicle_config == "car":
            self.vehicle = CarFactory().create()

        if vehicle_config == "truck":
            self.vehicle = TruckFactory().create()
