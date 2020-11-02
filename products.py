class Product:

    def __init__(self):
        self.productList = [
            {"name": "T-shirt", "price": 10.99},
            {"name": "Pants", "price": 14.99},
            {"name": "Jacket", "price": 19.99},
            {"name": "Shoes", "price": 24.99}
        ]
        self.offerList = [
            {1: "Buy two t-shirts and get a jacket half its price"},
            {2: "Shoes are on 10% off"}
        ]

    def get_product(self):
        return self.productList

    def get_offers(self):
        return self.offerList
