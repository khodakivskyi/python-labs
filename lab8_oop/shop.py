class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        print(f"Назва магазину: {self.shop_name}, Тип магазину: {self.store_type}")

    def open_shop(self):
        print(f"Онлайн-магазин {self.shop_name} відкритий!")

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, increment):
        self.number_of_units += increment


class Discount(Shop):
    def __init__(self, shop_name, store_type, number_of_units=0):
        super().__init__(shop_name, store_type, number_of_units)
        self.discount_products = []

    def get_discounts_ptoducts(self):
        return self.discount_products

    def add_discount_product(self, product):
        if product not in self.discount_products:
            self.discount_products.append(product)

