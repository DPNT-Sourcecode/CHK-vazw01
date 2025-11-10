from collections import Counter
from typing import Dict, List, Tuple

PRICES: Dict[str, int] = {
    "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10,
    "G": 20, "H": 10, "I": 35, "J": 60, "K": 80, "L": 90,
    "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50,
    "S": 30, "T": 20, "U": 40, "V": 50, "W": 20, "X": 90,
    "Y": 10, "Z": 50,
}

MULTI_BUY_OFFERS: Dict[str, list] = {
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)],
    "H": [(10, 80), (5, 45)],
    "K": [(2, 150)],
    "P": [(5, 200)],
    "Q": [(3, 80)],
    "V": [(3, 130), (2, 90)],
}

SELF_OFFERS: Dict[str, int] = {
    "F": 3,
    "U": 4,
}

CROSS_OFFERS: List[Tuple[str, int, str, int]] = [
    ("E", 2, "B", 1),
    ("N", 3, "M", 1),
    ("R", 3, "Q", 1),
]


def _helper_apply_bundles(count: int, offers: List[Tuple[int, int]]) -> Tuple[int, int]:
    total = 0
    for qty, price in offers:
        n, count = divmod(count, qty)
        total += price * n

    return total, count

def _helper_cross_apply_offers(counts: Counter) -> Dict[str, int]:
    free: Dict[str, int] = {}
    for trigger_sku, trigger_qty, free_sku, free_qty in CROSS_OFFERS:
        triggers  =counts.get(trigger_sku, 0) // trigger_qty
        if triggers:
            free[free_sku] = free.get(free_sku, 0) + triggers * free_qty
    return free

def _helper_chargeable_after_free(sku: str, counts: Counter, cross_free: Dict[str, int]) -> int:
    c = counts.get(sku, 0)
    group = SELF_OFFERS.get(sku)
    if group:
        c -= c // group
    if sku in cross_free:
        c = max(0, c - cross_free[sku])
    return c


class CheckoutSolution:

    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1
        if any(ch not in PRICES for ch in skus):
            return -1

        counts = Counter(skus)

        cross_free = _helper_cross_apply_offers(counts)
        basket_total = 0

        for sku, unit_price in PRICES.items():
            chargeable_count = _helper_chargeable_after_free(sku, counts, cross_free)
            if chargeable_count <= 0:
                continue

            bundles = MULTI_BUY_OFFERS.get(sku, [])

            if bundles:
                b_total, leftover  = _helper_apply_bundles(chargeable_count, bundles)
                basket_total += b_total + leftover * unit_price

            else:
                basket_total += chargeable_count * unit_price
        return basket_total





