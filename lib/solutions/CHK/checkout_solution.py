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
    adjusted_counts = counts.copy()
    for offer_sku, required_qty, free_sku, free_qty in CROSS_OFFERS:
        num_offers = counts.get(offer_sku, 0) // required_qty
        if num_offers > 0 and free_sku in adjusted_counts:
            adjusted_counts[free_sku] = max(0, adjusted_counts[free_sku] - num_offers * free_qty)
    return adjusted_counts

def _helper_chargeable_after_free(sku: str, counts: Counter, cross_free: Dict[str, int]) -> int:
    c = counts.get(sku, 0)
    group = SELF_OFFERS.get(sku)
    if group:
        c -= c // group
    if sku in cross_free:
        c = max(0, c - cross_free[sku])
    return c


class CheckoutSolution:
    PRICES = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}
    OFFERS = {"A": [(5, 200), (3, 130)], "B": [(2, 45)]}

    def _apply_bundles(self, count: int, offers):
        total = 0
        for qty, price in offers:
            n, count = divmod(count, qty)
            total += price * n

        return total, count

    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1
        if any(ch not in self.PRICES for ch in skus):
            return -1

        counts = Counter(skus)
        basket_total = 0

        free_b = counts.get('E', 0) // 2
        charged_b = max(0, counts.get('B', 0) - free_b)

        a_count = counts.get('A', 0)
        a_total, a_remaining = self._apply_bundles(a_count, self.OFFERS['A'])
        basket_total += a_total + a_remaining * self.PRICES['A']

        b_total = 0
        b_remaining = charged_b
        b_total, b_remaining = self._apply_bundles(b_remaining, self.OFFERS['B'])
        basket_total += b_total + b_remaining * self.PRICES['B']

        basket_total += counts.get('C', 0) * self.PRICES['C']
        basket_total += counts.get('D', 0) * self.PRICES['D']
        basket_total += counts.get('E', 0) * self.PRICES['E']

        f_count = counts.get('F', 0)
        free_f = f_count // 3
        charged_f = f_count - free_f
        basket_total += charged_f * self.PRICES['F']

        return basket_total




