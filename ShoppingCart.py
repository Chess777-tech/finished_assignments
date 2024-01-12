class Product: 
    def __init__(self, name, price):
        self.name = name 
        self.price = price 


class Shoppingcart:
    def __init__(self):
        self.items = [] 
    
    def add_item(self,product, quantity=1):
        # Method to add items to the shopping cart 
        for item in self.items:
            if item['product'] == product:
                item['quantity'] += quantity
                return
        self.items.append({'product': product, 'quantity': quantity})
    

    def remove_item(self,product,quantity=1):
        # Method to remove items from shopping cart 
        for item in self.items:
            if item['product'] == product:
                item['quantity'] -= quantity
                if item['quantity'] <= 0:
                    self.items.remove(item)
                return
    

    def calculate_total(self):
        # Method to calculate the total cost of items in the shopping cart
        total_cost = sum(item['product'].price * item['quantity'] for item in self.items)
        return total_cost


    def display_cart(self):
         # Method to display the contents of the shopping cart
        print("Shopping Cart:")
        for item in self.items:
            print(f"{item['product'].name} - Quantity: {item['quantity']}")


product1 = Product("laptop", 800)
product2 = Product("Headphones", 50)
product3 = Product("Mouse", 20)


cart = Shoppingcart()

cart.add_item(product1, 2)
cart.add_item(product2, 1)
cart.add_item(product3, 3)


cart.display_cart()


cart.remove_item(product1, 1)
cart.display_cart()


total_cost = cart.calculate_total()
print(f"Total Cost: ${total_cost}")