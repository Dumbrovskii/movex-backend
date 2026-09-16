from abc import ABC, abstractmethod

from src.domain.value_objects import Route, Money


class PricingService(ABC):

    @abstractmethod
    def calculate_price(self, route: Route) -> Money:
        pass