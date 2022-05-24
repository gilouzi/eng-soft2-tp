class User:
    def __init__(self, email: str, password: str, address: str, telephone: str) -> None:
        self.email = email
        self.password = password
        self.address = address
        self.telephone = telephone

    def login(self):
        raise NotImplementedError('login method not implemented')

    def logout(self):
        raise NotImplementedError('logout method not implemented')
