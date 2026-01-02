from ABC import ABC, abstractmethod

class PaymentProcessor:
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class PaymentProcessorFactory:
    @staticmethod
    def create_payment_processor(payment_type: str) -> PaymentProcessor:
        if payment_type == "CreditCard":
            return CreditCardPaymentProcessor()
        elif payment_type == "PayPal":
            return PayPalPaymentProcessor()
        else:
            raise ValueError(f"Unknown payment type: {payment_type}")

#############################################################################

class NotificationService:
    @abstractmethod
    def send_notification(self, message):
        pass

class EmailNotificationService(NotificationService):
    def send_notification(self, message):
        print(f"Sending email notification: {message}")

class SMSNotificationService(NotificationService):
    def send_notification(self, message):
        print(f"Sending SMS notification: {message}")

class NotificationServiceFactory:
    @staticmethod
    def create_notification_service(notification_type: str) -> NotificationService:
        if notification_type == "email":
            return EmailNotificationService()
        elif notification_type == "sms":
            return SMSNotificationService()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")