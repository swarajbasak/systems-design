from abc import ABC, abstractmethod

class OrderState(ABC):
    @abstractmethod
    def pay(self, order, amount):
        pass    

    @abstractmethod
    def cancel(self, order):
        pass

class NewState(OrderState):
    def pay(self, order, amount):
        if amount >= order.total_price:
            print("Payment successful. Order is now Processing.")
            order.set_state(PaidState())
        else:
            print("Insufficient payment. Order remains New.")

    def cancel(self, order):
        print("Order cancelled from New state.")
        order.set_state(CancelledState())
    
class ShippedState(OrderState):
    def pay(self, order, amount):
        print("Order already shipped. Payment not required.")
        order.set_state(CompletedState())

    def cancel(self, order):
        print("Cannot cancel. Order already shipped.")


class Order:
    def __init__(self):
        self.state = NewState()
    
    def set_state(self, state: OrderState):
        self.state = state
    
    def pay(self, amount):
        self.state.pay(self, amount)
    
    def cancel(self):
        self.state.cancel(self)