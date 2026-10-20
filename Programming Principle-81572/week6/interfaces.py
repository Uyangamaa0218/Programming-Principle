from __future__ import annotations

from typing import TYPE_CHECKING, Iterable, Protocol

if TYPE_CHECKING:
    from checkout_models import Product

class PriceCalculator(Protocol):
    def calculate_total_price(self, products: Iterable[Product]) -> int:
        ...
    #ellipsis
    #They mean:
    #The method has been declared, but its implementation is not provided here.