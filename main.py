PRODUCT = {
    "book": 100,
    "pen": 20,
    "laptop": 1000,
    "phone": 500
}


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)


    def total_price(self):
        return sum(product.price for product in self.products)

    def show_products(self):
        for product in self.products:
            print(product.name, ":", product.price)


class Customer:
    def __init__(self, name):
        self.name = name
        self.carts = []

    def add_cart(self, cart):
        self.carts.append(cart)

    def remove_cart_by_id(self, index):
        if 0 <= index < len(self.carts):
            self.carts.pop(index)

    def show_carts(self):
        for i, cart in enumerate(self.carts):
            print(f"Cart {i}:")
            cart.show_products()
            print("Total:", cart.total_price())
            print("-----")


customer = Customer(input("your name:"))
n = int(input("how many carts?"))
for i in range(n):
    cart = Cart()

    m = int(input(f"how many product in cart{i}?"))
    for j in range(m):
        name = input("enter product name")
        if name.lower() in PRODUCT:
            price = PRODUCT[name]
            product = Product(name, price)
            cart.add_product(product)
        else:
            print("not found")
    customer.add_cart(cart)

customer.show_carts()