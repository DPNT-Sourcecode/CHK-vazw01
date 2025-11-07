from collections import Counter


class CheckoutSolution:
    PRICES = {"A": 50, "B": 30, "C": 20, "D": 15}
    OFFERS = {"A": (3, 130), "B": (2, 45)}

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str) or not skus.isalpha():
            return -1

        counts = Counter(skus)
        basket_total = 0

        for item, count in counts:
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
