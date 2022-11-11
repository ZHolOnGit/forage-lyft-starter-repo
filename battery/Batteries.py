from datetime import datetime

from abc import abstractmethod


class Battery:

    @abstractmethod
    def needs_service(self):
        pass


class SpindlerBattery(Battery):

    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = datetime.today()

    def needs_service(self):
        delta = self.current_date- self.last_service_date

        return delta.days > 730


class NubbinBattery(Battery):

    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = datetime.today()

    def needs_service(self):
        today = datetime.today()
        delta = self.current_date - self.last_service_date

        return delta.days > 1460
