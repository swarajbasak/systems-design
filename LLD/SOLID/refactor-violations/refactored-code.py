from ABC import ABC, abstractmethod

class PaymentProcessor:
    @abstractmethod
    def process_payment(self, amount):
        pass

class NotificationService:
    @abstractmethod
    def send_notification(self, message):
        pass

class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class EmailNotificationService(NotificationService):
    def send_notification(self, message):
        print(f"Sending email notification: {message}")

class SMSNotificationService(NotificationService):
    def send_notification(self, message):
        print(f"Sending SMS notification: {message}")

class Logger:
    @abstractmethod
    def log(self, message):
        pass

class FileOrderLogger:
    def log_order(self, items, total_price):
        with open("orders.txt", "a") as f:
            f.write(f"Order: {items}, Total: {total_price}\n")


class OrderManager:
    def __init__(self, payment_processor: PaymentProcessor, notification_service: NotificationService, logger: Logger):
        self.items = []
        self.total_price = 0
        self.payment_processor = payment_processor
        self.notification_service = notification_service
        self.logger = logger

    def add_item(self, name, price):
        self.items.append(name)
        self.total_price += price

    def process_order(self):
        self.payment_processor.process_payment(self.total_price)
        self.notification_service.send_notification("Your order has been processed.")
        self.logger.log_order(self.items, self.total_price)


