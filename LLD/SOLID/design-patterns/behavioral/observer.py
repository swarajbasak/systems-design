from ABC import ABC, abstractmethod


# order manager is the observable
# everyone who is interested in order processing can subscribe to it
# payment processors, notification services, loggers are observers
# order manager keeps a list of observers and notifies them when an order is processed

class Observer(ABC):
    @abstractmethod
    def update(self, order):
        pass

class InventoryService(Observer):
    def update(self, order):
        print(f"Updating inventory for order: {order}")

class ShippingService(Observer):
    def update(self, order):
        print(f"Arranging shipping for order: {order}")

class OrderManager:
    def __init__(self):
        self.items = []
        self.total_price = 0
        self.observers = set()

    def attach(self, observer: Observer):
        self.observers.add(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)
    
    def process_order(self):
        print(f"Processing order with total price: ${self.total_price}")
        self.notify()