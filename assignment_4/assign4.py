"""

This file simulates a shopping cart, with different
objects for product, inventory, catalog, and cart.

"""

class Product:
    def __init__(self, name, price, category):
        # Initialize product attributes
        self._name = name
        self._price = price
        self._category = category

    # Define how products are classified
    def __eq__(self, other):
         if isinstance(other, Product):
             if  ((self._name == other._name and self._price == other._price) and (self._category==other._category)):
                return True
             else:
                return False
         else:
            return False

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_category(self):
        return self._category

    # Implement string representation
    def __repr__(self):
        rep = 'Product(' + self._name + ',' + str(self._price) + ',' + self._category + ')'
        return rep

class Inventory:
    def __init__(self):
        #initialize an empty dictionary to store inventory items
        self._inventory = {}

    def add_to_productInventory(self,productName,productPrice,productQuantity):
        #add an item to inventory
        if productName not in self._inventory:
            self._inventory[productName] = {'name':productName, 'price':int(productPrice), 'quantity':int(productQuantity)}

    def add_productQuantity(self,nameProduct,addQuantity):
        #add product quantity to inventory
        self._inventory[nameProduct]['quantity'] += addQuantity

    def remove_productQuantity(self,nameProduct,removeQuantity):
        #remove product quantity from inventory
        self._inventory[nameProduct]['quantity'] -= removeQuantity

    def get_productPrice(self,nameProduct):
        return self._inventory[nameProduct]['price']

    def get_productQuantity(self,nameProduct):
        return self._inventory[nameProduct]['quantity']

    def display_Inventory(self):
        for item in self._inventory.values():
            print(f'{item["name"]}, {item["price"]}, {item["quantity"]}')


class ShoppingCart:
    def __init__(self,buyerName,inventory):
        #initialize values
        self._buyerName = buyerName
        self._inventory = inventory
        self._cart = {}
        self._total = 0

    def add_to_cart(self,nameProduct,requestedQuantity):
        #add an item to cart
        if nameProduct in self._cart:
            if requestedQuantity < self._inventory.get_productQuantity(nameProduct):
                self._cart[nameProduct]['quantity'] += requestedQuantity
                self._inventory.remove_productQuantity(nameProduct, requestedQuantity)
                self._total += (self._inventory.get_productPrice(nameProduct) * requestedQuantity)
                return "Filled the order"
        elif requestedQuantity < self._inventory.get_productQuantity(nameProduct):
            self._cart[nameProduct] = {'product':nameProduct, 'quantity':requestedQuantity}
            self._inventory.remove_productQuantity(nameProduct,requestedQuantity)
            self._total += (self._inventory.get_productPrice(nameProduct)*requestedQuantity)
            return "Filled the order"
        else:
            return "Can not fill the order"

    def remove_from_cart(self,nameProduct,requestedQuantity):
        #remove an item from cart
        if nameProduct in self._cart:
            cart_quantity = self._cart[nameProduct]['quantity']
            if requestedQuantity <= cart_quantity:
                self._cart[nameProduct]['quantity'] -= requestedQuantity
                self._inventory.add_productQuantity(nameProduct,requestedQuantity)
                self._total -= (self._inventory.get_productPrice(nameProduct)*requestedQuantity)
                return "Successful"
            else:
                return "The requested quantity to be removed from cart exceeds what is in the cart"
        else:
            return "Product not in the cart"

    def view_cart(self):
        #view the total items in cart
        for item in self._cart.values():
            print(f'{item["product"]} {item["quantity"]}')
        print("Total:", self._total)
        print("Buyer Name:", self._buyerName)


class ProductCatalog:
    def __init__(self):
        #initialize an empty dictionary
        self._catalog = {}

    def addProduct(self,product):
        self._catalog[product.get_name()] = {'name': product.get_name(), 'price': product.get_price(),'category':product.get_category()}

    def price_category(self):
        #sort items by price category
        low_items_set = set()
        medium_items_set = set()
        high_items_set = set()
        low_items_count = 0
        medium_items_count = 0
        high_items_count = 0
        for item_key,item_value in self._catalog.items():
            price = item_value['price']

            if 0 <= price <= 99:
                low_items_count += 1
                low_items_set.add(item_value['name'])
            elif 100 <= price <= 499:
                medium_items_count += 1
                medium_items_set.add(item_value['name'])
            else:
                high_items_count += 1
                high_items_set.add(item_value['name'])
        print("Number of low price items:",low_items_count)
        print("Number of medium price items:",medium_items_count)
        print("Number of high price items:",high_items_count)

    def display_catalog(self):
        #display all items in catalog
        for item in self._catalog.values():
            print(f"Product: {item['name']} Price: {item['price']} Category: {item['category']}")

def populate_inventory(filename):
    #populate the inventory from a file
    infile = open(filename, 'r')
    line = infile.readline()
    inventory = Inventory()
    while line != "":
        line = line.strip()
        line = line.split(",")
        inventory.add_to_productInventory(line[0],line[1],line[2])
        line = infile.readline()
    infile.close()
    return inventory


def populate_catalog(filename):
    #populate the catalog given a file
    infile = open(filename, 'r')
    line = infile.readline()
    catalog_dict = ProductCatalog()
    while line != "":
        line = line.strip()
        line = line.split(",")
        product = Product(line[0],int(line[1]),line[3])
        catalog_dict.addProduct(product)
        line = infile.readline()
    infile.close()
    return catalog_dict






