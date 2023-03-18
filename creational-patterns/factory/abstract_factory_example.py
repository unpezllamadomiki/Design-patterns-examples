"""This pattern is perfect to create families of products. In our example, we could have luxury vehicles
and cheap vehicles. A client interested in luxury vehicles don't want to buy a cheap vehicle and vice-versa"""
from abc import ABC
from typing import Optional


# In the first step, we create abstract products. Those products are different but related and make up a family.
# Example: A family of vehicles.
class Car(ABC):
    def __init__(self) -> None:
        self.wheels: Optional[str] = None
        self.color: Optional[str] = None

    def change_wheels(self, wheels: str) -> str:
        raise NotImplementedError


class Truck(ABC):
    def __init__(self) -> None:
        self.wheels: Optional[str] = None
        self.color: Optional[str] = None

    def change_wheels(self, wheels: str) -> str:
        raise NotImplementedError


# In the second step, we implement variants of our abstract products which are different implementations
# of our abstract products grouped by variants. Example: Luxury and Cheap vehicles.
class LuxuryCar(Car):
    def change_wheels(self, wheels: str) -> None:
        self.wheels = "luxury_car_wheels"


class CheapCar(Car):
    def change_wheels(self, wheels: str) -> None:
        self.wheels = "cheap_car_wheels"


class LuxuryTruck(Truck):
    def change_wheels(self, wheels: str) -> None:
        self.wheels = "luxury_truck_wheels"


class CheapTruck(Truck):
    def change_wheels(self, wheels: str) -> None:
        self.wheels = "cheap_truck_wheels"


# Then we can create our abstract factory, which will return our abstract products (Car and Truck).
class AbstractVehicleFactory(ABC):
    def create_car(self) -> Car:
        raise NotImplementedError

    def create_truck(self) -> Truck:
        raise NotImplementedError


# Now we can define our concrete fabrics based in our families, which will implement our abstract factory methods.

# In this case we will return our abstract products because we want that our client works with all the factories, and
# we don't want it to be coupled with concrete implementations.
class CheapVehicleFactory(AbstractVehicleFactory):
    def create_car(self) -> Car:
        return CheapCar()

    def create_truck(self) -> Truck:
        return CheapTruck()


class LuxuryVehicleFactory(AbstractVehicleFactory):
    def create_car(self) -> Car:
        return LuxuryCar()

    def create_truck(self) -> Truck:
        return LuxuryTruck()


# Our application works with fabric and products, therefore we can use our subclasses without break down our client code
class Application:

    def __init__(self, factory_config) -> None:
        self.factory: Optional[AbstractVehicleFactory] = self.choose_factory(factory_config)
        self.car: Optional[Car] = None
        self.truck: Optional[Truck] = None

    @staticmethod
    def choose_factory(factory_config: str) -> AbstractVehicleFactory:
        if factory_config == "cheap":
            return CheapVehicleFactory()

        if factory_config == "luxury":
            return LuxuryVehicleFactory()

    def create_car(self):
        self.car = self.factory.create_car()

    def create_truck(self):
        self.truck = self.factory.create_truck()


