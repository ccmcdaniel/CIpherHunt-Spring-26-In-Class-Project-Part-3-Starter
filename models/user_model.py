from models.rank_model import Rank

class UserModel:
    def __init__(self, db, id=None):
        self.__id = 1
        self.__username = "johndoe1111"
        self.__email = "john.doe.1111@gmail.com"
        self.__rank = Rank(0)

    @property
    def id(self):
        return self.__id
    
    @property
    def username(self):
        return self.__username
    
    @property
    def email(self):
        return self.__email
    
    @property
    def rank(self):
        return self.__rank

    # Instructor Completes This
    def UpdateUsername(self, new_username):
        self.__username = new_username
        return True
    
    # Instructor Completes This
    def UpdateEmail(self, new_email):
        self.__email = new_email
        return True
    
    # Student Completes This
    def IncreasePoints(self, amount):
        if(amount <= 0):
            return
        else:
            self.__rank.current_points += amount
        
