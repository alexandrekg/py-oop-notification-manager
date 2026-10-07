# Object-Oriented Programming Challenge: Multifunctional Notification Gateway

Welcome to the **Multifunctional Notification Gateway** challenge! This practical Object-Oriented Programming (OOP) exercise is designed to help you practice and master key software engineering concepts in Python, specifically **Polymorphism**, **Composition**, and **Abstraction**.

---

## 🎯 Objective

Design and implement a notification system for an e-commerce platform. The system handles sending messages to customers across multiple channels (Email, SMS, and Push Notifications). Each channel maintains its own specific sending logic, constraints, and formatting rules, while a central manager coordinates delivery using polymorphic interface methods.

---

## 🧠 Concepts Covered

- **Abstraction & Polymorphism:** Creating a unified base/abstract interface for channels so the manager can invoke sending logic without knowing specific channel implementations.
- **Composition:** Building a `NotificationManager` that holds and manages a collection of `NotificationChannel` instances.
- **Encapsulation:** Protecting internal state and logic using private and protected access modifiers.

---

## 📋 Requirements

### 1. Base Class / Abstract Interface: `NotificationChannel`

- **Protected/Private Attributes:**
  - `_sender` (`str`): Identifier of the sender (e.g., sender email, phone number, or app token).
- **Methods:**
  - `__init__(self, sender: str)`
  - `send(self, recipient: str, message: str) -> bool`: Abstract/base method to be overridden by subclasses. Validates message constraints and returns `True` if sent successfully or `False` if validation fails.

### 2. Concrete Subclasses (Polymorphism)

Implement three subclasses inheriting from `NotificationChannel`:

#### `EmailChannel`
- **Attribute:** `subject_prefix` (`str`, optional, e.g., `"[Notification]"`).
- **Validation Rule:** The message must contain at least 5 characters.
- **Output on Success:**
  `"EMAIL sent by [sender] to [recipient] | Subject: [subject_prefix] | Body: [message]"`

#### `SMSChannel`
- **Validation Rule:** The message cannot exceed **160 characters**, and the `recipient` must be non-empty.
- **Output on Success:**
  `"SMS sent by [sender] to [recipient] | Body: [message]"`

#### `PushChannel`
- **Validation Rule:** Fails if the `recipient` is empty or `None`.
- **Output on Success:**
  `"PUSH sent to device [recipient] | App Token: [sender] | Body: [message]"`

---

### 3. Manager Class: `NotificationManager` (Composition)

The manager class handles channel execution and maintains sending logs.

- **Private Attributes:**
  - `__channels` (`list`): List storing registered `NotificationChannel` instances (Composition).
  - `__log` (`list`): List logging all delivery attempts (successes and failures).
- **Methods:**
  - `add_channel(self, channel: NotificationChannel) -> None`: Registers a new channel.
  - `notify_all(self, recipient: str, message: str) -> dict`: Iterates through all registered channels to dispatch the message using polymorphism. Returns a summary dictionary: `{"success": X, "failed": Y}`.
  - `get_history(self) -> list`: Returns a copy of the delivery logs.

---

## 🧪 Test Case / Usage Example

You can use the following script to test your implementation:

```python
from abc import ABC, abstractmethod

# Implement your classes here (NotificationChannel, EmailChannel, SMSChannel, PushChannel, NotificationManager)

if __name__ == "__main__":
    # 1. Instantiate notification channels
    email = EmailChannel(sender="support@store.com", subject_prefix="[Order Alert]")
    sms = SMSChannel(sender="+15550199")
    push = PushChannel(sender="APP_TOKEN_SECURE_123")

    # 2. Create the manager and add channels (Composition)
    manager = NotificationManager()
    manager.add_channel(email)
    manager.add_channel(sms)
    manager.add_channel(push)

    # 3. Test valid message dispatch across all channels
    print("--- TEST 1: Valid Delivery ---")
    result1 = manager.notify_all(recipient="user_123", message="Your order has been approved successfully!")
    print("Result:", result1)
    # Expected: {"success": 3, "failed": 0}

    # 4. Test SMS character limit failure (> 160 characters)
    print("\n--- TEST 2: Overly Long Message for SMS ---")
    long_text = "A" * 161
    result2 = manager.notify_all(recipient="user_123", message=long_text)
    print("Result:", result2)
    # Expected: {"success": 2, "failed": 1}

    # 5. Check delivery logs
    print("\n--- DELIVERY HISTORY ---")
    for log_entry in manager.get_history():
        print(log_entry)
```