class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.__quantity = quantity
        self.__price = price

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    def restock(self, qty):
        if qty < 0:
            print("Error: Cannot restock a negative quantity.")
            return False
        self.__quantity += qty
        print(f"Restocked {qty} of '{self.name}'. New quantity: {self.__quantity}")
        return True

    def sell(self, qty):
        if qty < 0:
            print("Error: Cannot sell a negative quantity.")
            return False
        if qty > self.__quantity:
            print(f"Error: Not enough stock of '{self.name}'. Available: {self.__quantity}")
            return False
        self.__quantity -= qty
        print(f"Sold {qty} of '{self.name}'. Remaining: {self.__quantity}")
        return True

    def total_value(self):
        return self.__quantity * self.__price

    def display(self):
        print(f"Name: {self.name}")
        print(f"Quantity: {self.__quantity}")
        print(f"Price: {self.__price:.2f}")
        print(f"Total Value: {self.total_value():.2f}")


class PerishableItem(Item):
    def __init__(self, name, quantity, price, days_until_expiry):
        super().__init__(name, quantity, price)
        self.days_until_expiry = days_until_expiry

    def is_expiring_soon(self):
        return self.days_until_expiry <= 3

    def total_value(self):
        value = super().total_value()
        if self.is_expiring_soon():
            return value * 0.5  # 50% discount
        return value

    def display(self):
        super().display()
        print(f"Days Until Expiry: {self.days_until_expiry}")
        if self.is_expiring_soon():
            print("Status: Expiring soon (50% discount applied)")


class ElectronicItem(Item):
    def __init__(self, name, quantity, price, warranty_months):
        super().__init__(name, quantity, price)
        self.warranty_months = warranty_months

    def display(self):
        super().display()
        print(f"Warranty: {self.warranty_months} months")


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        for existing in self.items:
            if existing.name.lower() == item.name.lower():
                print(f"Error: Item '{item.name}' already exists in inventory.")
                return False
        self.items.append(item)
        print(f"Added '{item.name}' to inventory.")
        return True

    def update_quantity(self, name, qty):
        item = self.search(name)
        if item is None:
            print(f"Error: Item '{name}' not found.")
            return False
        if qty < 0:
            print("Error: Quantity cannot be negative.")
            return False
        # Sell or restock to reach the target quantity
        current = item.get_quantity()
        if qty > current:
            item.restock(qty - current)
        elif qty < current:
            item.sell(current - qty)
        else:
            print(f"'{item.name}' quantity is already {qty}.")
        return True

    def search(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None

    def display_all(self):
        if not self.items:
            print("Inventory is empty.")
            return
        print("\n===== INVENTORY =====")
        for i, item in enumerate(self.items, 1):
            print(f"\n--- Item {i} ---")
            item.display()
        print("\n=====================")

    def total_inventory_value(self):
        return sum(item.total_value() for item in self.items)
