from collections import Counter


class CheckoutSolution:
    PRICES = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    OFFERS = {"A": (3, 130), "B": (2, 45)}

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

        free_b  = counts.get('E', 0) // 2
        charged_b = max(0, counts.get('B', 0) - free_b)

        for item, count in counts.items():
            if item not in self.PRICES:
                return -1

            offer_total = 0
            if item in self.OFFERS:
                qty, offer_price = self.OFFERS[item]
                offer_count = count // qty
                offer_total += offer_count * offer_price
                count -= offer_count * qty

            offer_total += self.PRICES[item] * count
            basket_total += offer_total

        return basket_total


