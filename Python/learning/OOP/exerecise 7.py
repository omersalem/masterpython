class menue_item:
    def __init__(self,name , price):
        self.name = name
        self.price = price
    def show_info(self):
        print(f"Name: {self.name}, Price: {self.price}")


class restaurant:
    def __init__(self):
        self.menu=[]
        self.order=[]
    def add_item(self, menue_item):
        self.menu.append(menue_item)
        

    def show_menu(self):
        if not self.menu:
            print("No items available.")
            return
        for item in self.menu:
            item.show_info()

    def place_order(self, name):
        for item in self.menu:
            if item.name.lower() == name.lower():
                self.order.append(item)
                print(f"You ordered {item.name}.")
                return
        print(f"{name} not found in the menu.")
    def show_orders(self):
        if not self.order:
            print("No orders yet.")
            return
        for item in self.order:
            item.show_info()

        
    def remove_item(self, name):
        for item in self.order:
            if item.name.lower() == name.lower():
                self.order.remove(item)
                print(f"{name} has been removed from the order.")
                return
        print(f"{name} not found in the order.")



# Add some default items
menu1 = menue_item("Pizza", 10)
menu2 = menue_item("Burger", 5)
restaurant = restaurant()
restaurant.add_item(menu1)
restaurant.add_item(menu2)
# Add some default items


def show_options():
    

# Add some default items


    while True:
        print("\n--- Welcome to the Restaurant ---")
        print("1. Show menu")
        print("2. Place an order")
        print("3. Show your order")
        print("4. Remove item from order")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            restaurant.show_menu()
        elif choice == "2":
            name = input("Enter the item name to order: ")
            restaurant.place_order(name)
        elif choice == "3":
            restaurant.show_orders()
        elif choice == "4":
            name = input("Enter the item name to remove from your order: ")
            restaurant.remove_item(name)
        elif choice == "5":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please try again.")
show_options()
