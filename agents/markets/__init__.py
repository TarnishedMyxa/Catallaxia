
class Market:
    def __init__(self, good):
        self.price = 0
        self.good=good

class order_matching_market(Market):
    def __init__(self, good):
        super().__init__(good)
        self.order_book = order_book()

    def add_order(self, order):
        self.order_book.add_order(order)


class order_book:
    def __init__(self, precision=0.01):
        self.buy_orders = []
        self.sell_orders = []
        self.min_price = 999999999999
        self.max_price = 0
        self.precision = precision
        self.price=0

    def add_order(self, order):
        if order.is_buy:
            self.buy_orders.append(order)
        else:
            self.sell_orders.append(order)

        if order.price < self.min_price:
            self.min_price = order.price
        if order.price > self.max_price:
            self.max_price = order.price

    def find_price(self):
        if len(self.buy_orders) == 0 or len(self.sell_orders) == 0:
            return 0

        for i in range((self.max_price-self.min_price)/self.precision):
            self.price = self.min_price + i*self.precision
            buy_quantity = 0
            sell_quantity = 0
            for order in self.buy_orders:
                if order.price >= self.price:
                    buy_quantity += order.quantity
            for order in self.sell_orders:
                if order.price <= self.price:
                    sell_quantity += order.quantity
            if buy_quantity >= sell_quantity:
                return self.price


class order:
    def __init__(self, price, quantity, is_buy):
        self.price = price
        self.quantity = quantity
        self.is_buy = is_buy
        self.is_filled = False



if __name__ == '__main__':
    pass

