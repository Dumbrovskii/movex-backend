from abc import ABC, abstractmethod

from movex_domain.value_objects.route import Route
from movex_domain.value_objects.money import Money


class PricingService(ABC):

    @abstractmethod
    def calculate_price(self, route: Route) -> Money:
        pass