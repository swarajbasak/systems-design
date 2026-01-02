from ABC import ABC, abstractmethod

class NotificationService:
    @abstractmethod
    def send_notification(self, message):
        pass

class AppendedSignatureDecorator(NotificationService):
    def send_notification(self, message):
        message += "-- sent from python"
        return super().send_notification(message)

class EmailNotificationService(NotificationService):
    def send_notification(self, message):
        print(f"Sending email notification: {message}")

class SMSNotificationService(NotificationService):
    def send_notification(self, message):
        print(f"Sending SMS notification: {message}")


class OrderManager:
    def __init__(self, notification_service: NotificationService):
        self.items = []
        self.total_price = 0
        self.notification_service = notification_service

    def add_item(self, name, price):
        self.items.append(name)
        self.total_price += price

    def process_order(self):
        self.notification_service.send_notification("Your order has been processed.")


