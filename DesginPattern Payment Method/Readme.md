
# Python Design Patterns - Payment Processing System

A real-world Python project demonstrating multiple important software design patterns using a Payment Processing Application.

This project combines:

- Singleton Pattern
- Decorator Pattern
- Adapter Pattern
- Observer Pattern

to simulate a scalable and maintainable backend payment architecture.

---

# 🚀 Project Overview

This project demonstrates how modern backend systems use design patterns together to solve real engineering problems like:

- Shared resource management
- Authentication & logging
- Third-party payment gateway integration
- Event-driven notifications
- Loose coupling & scalability

---

# 📌 Design Patterns Used

| Design Pattern | Purpose |
|---|---|
| Singleton | Shared database connection |
| Decorator | Authentication & logging |
| Adapter | Payment gateway compatibility |
| Observer | Email/SMS notifications |

---

# 🏗️ Application Flow

```text
User Makes Payment
       ↓
Authentication Check
       ↓
Logging
       ↓
Different Payment Gateway Support
       ↓
Shared Database Connection
       ↓
Notify Email + SMS
```

---

# 📂 Project Structure

```text
payment-system/
│
├── main.py
├── README.md
```

---

# ⚙️ Features

## ✅ Singleton Pattern
- Creates only one database connection object
- Prevents unnecessary resource creation

## ✅ Decorator Pattern
- Adds logging and authentication dynamically
- Keeps business logic clean

## ✅ Adapter Pattern
- Converts different payment gateway interfaces into a common interface
- Supports:
  - PayPal
  - Credit Card
  - Google Pay

## ✅ Observer Pattern
- Sends notifications after successful payment
- Supports:
  - Email notifications
  - SMS notifications

---

# 🧠 Real-World Problems Solved

| Problem | Solution |
|---|---|
| Multiple DB connections | Singleton |
| Repeated auth/logging code | Decorator |
| Different gateway APIs | Adapter |
| Hardcoded notifications | Observer |

---

# 🖥️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Design Patterns

---

# 📜 Code Explanation

## 1️⃣ Singleton Pattern

Used for:

```python
DatabaseConnection
```

Ensures only one database connection object is created throughout the application lifecycle.

### Benefits
- Memory efficient
- Centralized connection management
- Better resource handling

---

## 2️⃣ Decorator Pattern

Used for:

```python
@authenticate
@logger
```

Adds:
- Authentication
- Logging

without modifying original payment processing logic.

### Benefits
- Cleaner code
- Reusable functionality
- Separation of concerns

---

## 3️⃣ Adapter Pattern

Used for:
- PayPal
- Credit Card
- Google Pay

Each payment provider has different method names.

Adapters normalize them into:

```python
pay(amount)
```

### Benefits
- Loose coupling
- Easier third-party integration
- Common payment interface

---

## 4️⃣ Observer Pattern

Used for:
- Email notifications
- SMS notifications

After payment success, all observers are notified automatically.

### Benefits
- Event-driven architecture
- Easy scalability
- Independent notification services

---

# ▶️ How to Run

## Clone Repository

```bash
git clone https://github.com/your-username/payment-design-patterns.git
```

## Navigate to Project

```bash
cd payment-design-patterns
```

## Run Application

```bash
python main.py
```

---

# 📌 Sample Output

```text
User is authenticated....

Start of logger in a application...

[LOG] Payment processing started

Amount debited 250 using Paypal method
Thank you for using PayPal...

Creating Database Connection...
Connected to Database

Email Notification: Payment of 250 processed successfully.
SMS Notification: Payment of 250 processed successfully.

[LOG] Payment processing completed
```

---

# 🎯 Key Learning Outcomes

This project helps understand:

- Real-world usage of design patterns
- Clean architecture principles
- Loose coupling
- Maintainable backend design
- Scalable software engineering concepts

---

# 📚 Design Pattern Concepts Covered

- Creational Design Pattern
- Structural Design Pattern
- Behavioral Design Pattern

---

# 🔥 Future Improvements

Possible enhancements:

- Add Factory Pattern
- Add Strategy Pattern
- Add Kafka/RabbitMQ event system
- Add Async notifications
- Add REST API layer using Flask/FastAPI
- Add Database persistence

---
                    User Payment
                          │
                ┌─────────┴─────────┐
                │                   │
          Authentication       Logging
              Decorator        Decorator
                │                   │
                └─────────┬─────────┘
                          │
                    Payment Adapter
          ┌──────────┬──────────┬──────────┐
          │          │          │
       PayPal      CreditCard   GooglePay
                          │
                    Singleton DB
                          │
                    Observer Notify
                 ┌────────┴────────┐
                 │                 │
              Email              SMS

              
# 👨‍💻 Author

Swapnil Thorat

Senior Python Developer

---

# ⭐ If You Like This Project

Give it a ⭐ on GitHub and feel free to contribute.
