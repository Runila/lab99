class UserAccount:
    def __init__(self, username, email, password):
        self.username=username
        self.email=email
        self.password=password

    def set_password(self, new_password):
        self.password=new_password

    def check_password(self, password):
        return self.password == password


user = UserAccount("user1", "user@e.com", "password")
print("Пароль корректен:", user.check_password("password"))
user.set_password("newpassword")
print("Пароль корректен:", user.check_password("newpassword"))
print("Пароль корректен:", user.check_password("password"))
