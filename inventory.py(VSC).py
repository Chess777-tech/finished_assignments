class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)

    def update_product(self, name, price=None, quantity=None):
        for product in self.products:
            if product.name == name:
                if price is not None:
                    product.price = price
                if quantity is not None:
                    product.quantity = quantity

    def list_products(self):
        for product in self.products:
            print(f"{product.name}: {product.quantity} available at {product.price} each")

inventory = Inventory()
inventory.add_product("Apple", 0.5, 10)
inventory.add_product("Banana", 0.3, 20)
inventory.add_product("Orange", 0.4, 15)

# List all products in the inventory
inventory.list_products()
# Output:
# Apple: 10 available at 0.5 each
# Banana: 20 available at 0.3 each
# Orange: 15 available at 0.4 each

# Update the price of apples and the quantity of oranges
inventory.update_product("Apple", price=0.6)
inventory.update_product("Orange", quantity=20)

# List all products in the inventory again
inventory.list_products()
# Output:
# Apple: 10 available at 0.6 each
# Banana: 20 available at 0.3 each
# Orange: 20 available at 0.4 each

# Remove bananas from the inventory
inventory.remove_product("Banana")

# List all products in the inventory one last time
inventory.list_products()
# Output:
# Apple: 10 available at 0.6 each
# Orange: 20 available at 0.4 each