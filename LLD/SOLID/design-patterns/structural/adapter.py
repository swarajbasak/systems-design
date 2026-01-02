from abc import ABC, abstractmethod

class Logger:
    @abstractmethod
    def log_order(self, items, total_price):
        pass

class FileLogger(Logger):
    def log_order(self, items, total_price):
        with open("orders.txt", "a") as f:
            f.write(f"Order: {items}, Total: {total_price}\n")

class SomeThirdPartyLogger:
    def send_event_data(self, items, total_price):
        with open("third_party_logs.txt", "a") as f:
            f.write(f"Event - Items: {items}, Total: {total_price}\n")

class ThirdPartyLoggerAdapter(Logger):
    def __init__(self, third_party_logger: SomeThirdPartyLogger):
        self.third_party_logger = third_party_logger

    def log_order(self, items, total_price):
        self.third_party_logger.send_event_data(items, total_price)

class OrderManager:
    def __init__(self, logger: Logger):
        self.items = []
        self.total_price = 0
        self.logger = logger

    def add_item(self, name, price):
        self.items.append(name)
        self.total_price += price

    def process_order(self):
        self.logger.log_order(self.items, self.total_price)
