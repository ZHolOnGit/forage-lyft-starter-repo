from battery import Batteries
from engine import Engines
from Car import Car

class CarFactory:
    def create_calliope(self,last_service_date,current_mileage,last_service_mileage):
        engine = Engines.CapuletEngine(last_service_mileage,current_mileage)
        battery = Batteries.SpindlerBattery(last_service_date)

        return Car(engine, battery)

    def create_glissade(self, last_service_date, current_mileage, last_service_mileage):
        engine = Engines.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = Batteries.SpindlerBattery(last_service_date)

        return Car(engine, battery)

    def create_palindrome(self, last_service_date, warning_light_on):
        engine = Engines.SternmanEngine(warning_light_on)
        battery = Batteries.SpindlerBattery(last_service_date)

        return Car(engine, battery)
    def create_roschach(self, last_service_date, current_mileage, last_service_mileage):
        engine = Engines.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = Batteries.NubbinBattery(last_service_date)

        return Car(engine, battery)
    def create_thovex(self, last_service_date, current_mileage, last_service_mileage):
        engine = Engines.CapuletEngine(last_service_mileage, current_mileage)
        battery = Batteries.NubbinBattery(last_service_date)

        return Car(engine, battery)


