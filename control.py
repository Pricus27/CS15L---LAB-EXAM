from functions import Item, PerishableItem, ElectronicItem, Inventory


def create_sample_inventory():
    inventory = Inventory()
    inventory.add_item(Item("Notebook", 50, 25.00))
    inventory.add_item(PerishableItem("Milk", 20, 60.00, 2))
    inventory.add_item(PerishableItem("Bread", 15, 45.00, 5))
    inventory.add_item(ElectronicItem("Headphones", 10, 1500.00, 12))
    inventory.add_item(ElectronicItem("USB Cable", 30, 120.00, 6))
    return inventory


def show_menu():
    print("\n========== INVENTORY SYSTEM ==========")
    print("1. Display all items")
    print("2. Search for an item")
    print("3. Add a regular item")
    print("4. Add a perishable item")
    print("5. Add an electronic item")
    print("6. Restock an item")
    print("7. Sell an item")
    print("8. Update quantity")
    print("9. Total inventory value")
    print("0. Exit")
    print("======================================")


def get_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid number.")
        return None


def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid number.")
        return None


def run():
    inventory = create_sample_inventory()

    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            name = input("Enter item name to search: ").strip()
            item = inventory.search(name)
            if item:
                print("\nItem found:")
                item.display()
            else:
                print(f"Item '{name}' not found.")

        elif choice == "3":
            name = input("Item name: ").strip()
            qty = get_int("Quantity: ")
            price = get_float("Price: ")
            if qty is not None and price is not None:
                inventory.add_item(Item(name, qty, price))

        elif choice == "4":
            name = input("Item name: ").strip()
            qty = get_int("Quantity: ")
            price = get_float("Price: ")
            days = get_int("Days until expiry: ")
            if qty is not None and price is not None and days is not None:
                inventory.add_item(PerishableItem(name, qty, price, days))

        elif choice == "5":
            name = input("Item name: ").strip()
            qty = get_int("Quantity: ")
            price = get_float("Price: ")
            warranty = get_int("Warranty (months): ")
            if qty is not None and price is not None and warranty is not None:
                inventory.add_item(ElectronicItem(name, qty, price, warranty))

        elif choice == "6":
            name = input("Item name: ").strip()
            item = inventory.search(name)
            if item:
                qty = get_int("Quantity to restock: ")
                if qty is not None:
                    item.restock(qty)
            else:
                print(f"Item '{name}' not found.")

        elif choice == "7":
            name = input("Item name: ").strip()
            item = inventory.search(name)
            if item:
                qty = get_int("Quantity to sell: ")
                if qty is not None:
                    item.sell(qty)
            else:
                print(f"Item '{name}' not found.")

        elif choice == "8":
            name = input("Item name: ").strip()
            qty = get_int("New quantity: ")
            if qty is not None:
                inventory.update_quantity(name, qty)

        elif choice == "9":
            total = inventory.total_inventory_value()
            print(f"\nTotal Inventory Value: {total:.2f}")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
