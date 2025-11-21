class User:
    def __init__(self, first_name, last_name, email="", nickname="", newsletter_subscription=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.nickname = nickname
        self.newsletter_subscription = newsletter_subscription
        self.login_attempts = 0

    def describe_user(self):
        print(f"Повне ім'я: {self.first_name} {self.last_name}")
        if self.email:
            print(f"Поштова адреса: {self.email}")
        if self.nickname:
            print(f"Нікнейм: {self.nickname}")
        print(f"Розсилка новин: {'Так' if self.newsletter_subscription else 'Ні'}")

    def greeting_user(self):
        print(f"Привіт, {self.first_name} {self.last_name}! Раді вас бачити на сайті.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

