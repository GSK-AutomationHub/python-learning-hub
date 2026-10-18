
class Item:
    product_rate = 0.8
    all = []
    def __init__(self,product_name:str,variant_name:str,variant_price:float,quantity=0):
        # initialize instance variables
        self.product_name = product_name
        self.__variant_name = variant_name
        self.__variant_price = variant_price
        self.quantity = quantity

        # run argument validations
        assert self.__variant_price >0, f"product variant price {self.__variant_price} is not greater tan zero"

        # list all instances
        Item.all.append(self)

    # to make instance variable read-only
    @property
    def variant_name(self):
        return self.__variant_name

    @property
    def variant_price(self):
        return self.__variant_price

    # to override instance variable
    @variant_price.setter
    def variant_price(self, value):
        if value < self.__variant_price:
            print("not a valid price")
        else:
            self.__variant_price = value

    def calculate_product_total_price(self):
        return self.__variant_price * self.quantity

    def calculate_discount(self):
        return self.calculate_product_total_price() * self.product_rate

    def apply_discount(self):
        return self.calculate_product_total_price() - self.calculate_discount()

    def __repr__(self):
        return f"Item('{self.product_name}','{self.__variant_name}',{self.__variant_price},{self.quantity})"


    def __prepare_email_subject(self,recipient_email):
        return f"""
        To: {recipient_email}
        Subject: Your Store Updates: New product available
        """

    def __prepare_email_body(self):
        return f"""
        Hello, 
         We have product {self.product_name}  now available in store
 
        Regards.
        Store          
        """

    def __prepare_email_signature(self):
        return f"""
        Your Store
        NewYork
        """
    def __connect_to_smtp_server(self):
        server_config = "server_ip"
        self.connect(server_config)

    def send_email(self,recipient_email):
        self.__prepare_email_subject(recipient_email)
        self.__prepare_email_body()
        self.__prepare_email_signature()
        self.__connect_to_smtp_server()



phone = Item('iPhone_new',"x12",75000,1)
print(Item.all)
print(phone.variant_name)
phone.product_rate = 0.2
print(phone.calculate_product_total_price())
print(phone.apply_discount())
phone.send_email('abc@testemail.com')

# phone.variant_price = 120000
# print(Item.all)