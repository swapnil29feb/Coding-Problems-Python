class FoodOrder:
    def __init__(self, order_id: int, customer_name:str):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = []
        self.is_placed = False
        self._total_bill = 0.0
        self.total_qu = 0
        
    def add_item(self, food_item:str, quantity: int, price: float):
        self.food_item = food_item
        self.quantity = quantity
        self.price = price
        
        if self.is_placed:
            print("Cannot modify a placed order.")
            return
        self.items.append(self.food_item)
        self._total_bill = self._total_bill + (self.price * self.quantity)
        self.total_qu = self.total_qu + self.quantity
        # self.is_placed = True
            
    def place_order(self):
        self.is_placed = True
        print(f"Order Place for Order_ID {self.order_id}")
    
    
    def display_order(self):
        print(f"{self.order_id}-{self.customer_name} Order={self.items}, Total Q={self.total_qu},Total={self._total_bill}")
            

o1 = FoodOrder(1,'swap')
o1.add_item('pizza', 2, 299)
o1.add_item('burger', 3, 99)
o1.place_order()
o1.display_order()
o1.add_item('Pasta', 1, 49)
o1.display_order()
# print(o1)

o2 = FoodOrder(2, 'Simita')
o2.add_item('Tandoor',1,450.99)
o2.add_item("Chi. Biryani", 3, 155.25)
o2.add_item('IceCream', 10, 20.15)
o2.place_order()
o2.display_order()