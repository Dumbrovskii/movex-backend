from src.application.interfaces.services import PricingService
from src.config import settings
from movex_domain.value_objects.route import Route
from movex_domain.value_objects.money import Money

from decimal import Decimal


class DefaultPricingService(PricingService):

    def calculate_price(self, route: Route) -> Money:
        distance_km = Decimal(str(route.distance_meters)) / Decimal("1000")

        amount = settings.RIDE_BASE_FARE + distance_km * settings.RIDE_PRICE_PER_KM

        return Money(
            amount=amount.quantize(Decimal("0.01")),
            currency="UAH"
        )