from flask_sqlalchemy import SQLAlchemy
MAX_SIZE_STR = 50

db_user = SQLAlchemy()

class User(db_user.Model):

    __tablename__ = 'user_tb'
    
    id = db_user.Column(db_user.Integer, primary_key=True)
    name = db_user.Column(db_user.String(MAX_SIZE_STR))
    email = db_user.Column(db_user.String(MAX_SIZE_STR))
    login = db_user.Column(db_user.String(MAX_SIZE_STR))
    password = db_user.Column(db_user.String(MAX_SIZE_STR))
    address = db_user.Column(db_user.String(MAX_SIZE_STR))
    telephone = db_user.Column(db_user.Integer)

    def __init__(self, name: str, email: str, login: str, password: str, address: str, telephone: str) -> None:
        self.name = name
        self.email = email
        self.login = login
        self.password = password
        self.address = address
        self.telephone = telephone
    
    def getName(self):
        return self.name
    
    def getEmail(self):
        return self.email
    
    def getLogin(self):
        return self.login
    
    def getAddress(self):
        return self.address
    
    def getTelephone(self):
        return self.telephone
