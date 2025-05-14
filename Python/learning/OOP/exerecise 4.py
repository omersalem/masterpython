class product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def show_info(self):
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

class store:
    def __init__(self):
        self.products = []
    def add_product(self,product):
        self.products.append(product)
    def show_products(self):
        
        for product in self.products:
            if product.quantity > 0:
                product.show_info()
            else:
                print(f"{product.name} is out of stock.")
    
    def search_product(self,name):
        for product in self.products:
            if product.name == name:
                product.show_info()
                return
        print(f"{name} not found in the store.")

    def remove_product(self,name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"{name} has been removed from the store.")
                return
        print(f"{name} not found in the store.")
    def buy_products(self,name):
        for product in self.products:
            if product.name.lower() == name.lower():
                if product.quantity > 0:
                    print(f"You bought {product.name} for {product.price}.")
                    product.quantity -= 1
                    return
                else:
                    print(f"{product.name} is out of stock.")
                    return
        
               

def show_options():
    while True:
        print("************** Welcome to the Store! **************")
        print("Please choose an option:")
        print("1. Add product")
        print("2. Show products")
        print("3. Search product")
        print("4. Remove product")
        print("5. Buy product")
        print("6. Exit")
        opt=int(input("Enter your choice: "))
        if opt==1:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            new_product = product(name, price, quantity)
            store1.add_product(new_product)
            print(f"{name} has been added to the store.")
            continue
        elif opt==2:
            store1.show_products()
            continue
        elif opt==3:
            name = input("Enter product name: ")
            store1.search_product(name)
            continue
        elif opt==4:
            name = input("Enter product name: ")
            store1.remove_product(name)
            continue
        elif opt==5:
            name = input("Enter product name: ")
            store1.buy_products(name)
            continue
        elif opt==6:
            print("Thank you for visiting the store!")
            break
        else:
            print("Invalid option. Please try again.")
            continue


car = product('car', 20000, 5)
bike = product('bike', 500, 10)
phone = product('phone', 1000, 0)
    
store1 = store()

show_options()