# Singleton
# Decorator
# Adapter
# Observer

# User Makes Payment
#        ↓
# Authentication Check
#        ↓
# Logging
#        ↓
# Different Payment Gateway Support
#        ↓
# Shared Database Connection
#        ↓
# Notify Email + SMS


# Pattern	Used For
# Singleton	Shared DB connection
# Decorator	Auth + Logging
# Adapter	Stripe & PayPal compatibility
# Observer	Email/SMS notifications

# ==========================================
# 1. SINGLETON PATTERN
# Shared Database Connection


class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Creating Database Connection...")
            cls._instance = super().__new__(cls)
        
        return cls._instance
    
    def connect(self):
        print("Connected to Database")
        

# ==========================================
# 2. DECORATOR PATTERN
# Logging & Authentication
# ==========================================

def logger(func):
    def wrapper(*args, **kwargs):
        print("Start of logger in a application...")
        print("\n[LOG] Payment processing started")
        res = func(*args, **kwargs)
        print("[LOG] Payment processing completed")
        return res
    return wrapper
    
    
def authenticate(func):
    def wrapper(*args, **kwargs):
        print("User is authenticated....")
        return func(*args, **kwargs)
    return wrapper
    
# ==========================================
# 3. Adapeter PATTERN
# Different Payment Gateways
# ==========================================   

# Adapter for paypal, credit card, gpay, etc
# 1. THIRD-PARTY SERVICES (The Adaptees)


class PayPal:
    def pay_to_account(self, amount):
        print(f"Amount debited {amount} using Paypal method")
        print("Thank you for using PayPal...")

class Credit_Card:
    def pay_by_cc(self, amount):
        print(f"Amount debited {amount} using Credit Card method")
        print("Thank you for using Credit Card...")
        
class GooglePay:
    def by_googlepay_id(self, amount):
        print(f"Amount debited {amount} using GooglePay method")
        print("Thank you for using GooglePay...")
        
# ==========================================
# ADAPTERS (The Translators)
# ==========================================

class PayPalAdapter:
    def __init__(self, paypal):
        self.paypal = paypal


    def pay(self, amount):
        self.paypal.pay_to_account(amount)
        
        
class CreditCardAdapter:
    def __init__(self, cc):
        self.cc = cc
        
    def pay(self, amount):
        self.cc.pay_by_cc(amount)
        

class GooglepayAdapter:
    def __init__(self, gpay):
        self.gpay = gpay
    
    def pay(self, amount):
        self.gpay.by_googlepay_id(amount)
        
        
# ==========================================
# 4. OBSERVER PATTERN (Notifications)
# ==========================================
class PaymentNotificationSystem:
    def __init__(self):
        self._observers  = []
        
    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, amount):
        for observer in self._observers:
            observer.update(amount)


class EmailNotification:
    def update(self, amount):
        print(f"Email Notification: Payment of {amount} processed successfully.")



class SMSNotification:
    def update(self, amount):
        print(f"SMS Notification: Payment of {amount} processed successfully.")
        
        
# ==========================================
# 5. THE MAIN PIPELINE (Tying It All Together)
# ==========================================

@authenticate
@logger
def process_user_acc(adapter_instance, amount, notifier):
    adapter_instance.pay(amount)
    
    db = DatabaseConnection()
    
    notifier.notify(amount)
    
# ==========================================
# 6. EXECUTION SCRIPT

notifier = PaymentNotificationSystem()
notifier.attach(EmailNotification())
notifier.attach(SMSNotification())

paypal_gateway = PayPalAdapter(PayPal())
cc_credit = CreditCardAdapter(Credit_Card())


process_user_acc(paypal_gateway, 250, notifier)
