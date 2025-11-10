from collections import Counter




class CheckoutSolution:
    PRICES = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}
    OFFERS = {"A": [(5,200),(3, 130)], "B": [(2, 45)]}

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


