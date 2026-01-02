class OrderManager:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_item(self, name, price):
        self.items.append(name)
        self.total_price += price

    def process_order(self, payment_type):
        # Violation 1: Logic for payment types is hardcoded
        if payment_type == "CreditCard":
            print(f"Processing credit card payment of ${self.total_price}")
        elif payment_type == "PayPal":
            print(f"Processing PayPal payment of ${self.total_price}")
        
        # Violation 2: This class handles its own logging/persistence
        with open("orders.txt", "a") as f:
            f.write(f"Order: {self.items}, Total: {self.total_price}\n")

    def send_notification(self, type):
        # Violation 3: Forcing a specific notification method
        if type == "email":
            print("Sending email notification...")
        elif type == "sms":
            print("Sending SMS notification...")