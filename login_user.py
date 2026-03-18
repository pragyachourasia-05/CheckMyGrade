class LoginUser:
    def __init__(self, user_id, password, role):
        self.user_id = user_id
        self.password = password
        self.role = role

    def to_dict(self):
        return {
            "User_id": self.user_id,
            "Password": self.password,
            "Role": self.role
        }

    def login(self):
        return f"{self.user_id} logged in"

    def logout(self):
        return f"{self.user_id} logged out"

    def change_password(self, new_password):
        self.password = new_password