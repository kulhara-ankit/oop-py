class Product:

    def __init__(self, name, price, deal_price, ratings):

        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price

    def display_product_details(self):
        print("Product : {}".format(self.name))
        print("Price : {}".format(self.price))
        print("Deal Price : {}".format(self.deal_price))
        print("You Saved : {}".format(self.you_save))
        print("Ratings : {}".format(self.ratings))


    def get_deal_price(self):
        return self.deal_price

class Electronics(Product):

    # def set_warranty(self, warranty_in_months):
    #     self.warranty_in_months = warranty_in_months

    # def get_warranty(self):
    #     return self.warranty_in_months


    def __init__(self, name, price, deal_price, ratings, warranty_in_months):
        super().__init__(name, price, deal_price, ratings)
        self.warranty_in_months = warranty_in_months

    
    def display_product_details(self):
        super().display_product_details()
        print("Warranty in Months : {}".format(self.warranty_in_months))
        

class Grocery(Product):

    # def set_expiry_date(self, expiry_date):
    #     self.expiry_date = expiry_date

    # def get_expiry_date(self):
    #     return self.expiry_date

    def __init__(self, name, price, deal_price, ratings, expiry_date):
        super().__init__(name, price, deal_price, ratings)
        self.expiry_date = expiry_date
    
    def display_product_details(self):
        super().display_product_details()
        print("Expiry Date is : {}".format(self.expiry_date))
    



class Laptop(Electronics):
    def __init__(self, name, price, deal_price, ratings, warranty_in_months, ram, storage):
        super().__init__(name, price, deal_price, ratings, warranty_in_months)
        self.ram = ram
        self.storage = storage

    def display_product_details(self):
        super().display_product_details()
        print("RAM with {}".format(self.ram))
        print("Storage with {}".format(self.storage))




class Order:

    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address

    def add_items(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity : {}".format(quantity))
            print("")

    def get_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_bill += price
        print("Total Bill : {}".format(total_bill))
        return total_bill




tv = Electronics("Tv", 48000, 45000, 4.8, 36)
#tv.set_warranty(36)

print()
milk = Grocery("pulse", 80, 78, 3.5, 6)
#milk.set_expiry_date(6)
dell = Laptop("Dell Inspiron Is345",58999, 55000, 4.8, 24, "16GB", "1TB SSD")
print()
order_obj = Order("Prime", "Nagpur")
order_obj.add_items(tv, 2)
order_obj.add_items(milk, 7)
order_obj.add_items(dell, 1)
order_obj.display_order_details()
order_obj.get_total_bill()
