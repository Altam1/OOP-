import csv

class Item:
    pay_rate = 0.8  # a 20% of discount
    all = []

    def __init__(self,name: str,price:float,quantity=0):

        # Run validations to the received arguments
        assert price >=0 ,f"price {price} is not grater than or equal to zero!"
        assert quantity >=0 ,f"quantity  {quantity} is not grater than or equal to zero!"
        # print(name,price,quantity,total)
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        # Action to ecexute
        Item.all.append(self)
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        # print(Item.__dict__)

    # def __init__(self,name,price=0,quantity=0):
    #     self.name=name
    #     self.price=price
    #     self.quantity=quantity
        # print(f"an instance created：{name,price,quantity} the price for all is : {price*quantity} ")



    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
           Item(
               name = item.get('name'),
               price = float(item.get('price')),
               quantity = int(item.get('quantity')),
           )
    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

        def __repr__(self):
            return f"Item('{self.name}',{self.price},{self.quantity}) "

print(Item.is_integer(7.5))