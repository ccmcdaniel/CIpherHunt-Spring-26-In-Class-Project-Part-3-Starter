from models.rank_model import Rank

class UserModel:
    def __init__(self, db, id=None):
        self.__db = db

        if(id != None):
            pass # return here to load user data from database...
                 # if no ID is provided, then generate a mock user
        else:
            user_data = self.__db.GetUserByID(1)

            if user_data == None:
                self.__id = 1
                self.__username = "johndoe1111"
                self.__email = "john.doe.1111@gmail.com"
                self.__rank = Rank(0)
                self.__db.AddUser(self.__username, self.__email)
            else:
                self.__id = user_data[0]
                self.__username = user_data[1]
                self.__email = user_data[2]
                self.__rank = Rank(int(user_data[3]))

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

    def UpdateUsername(self, new_username):
        result = self.__db.UpdateUser(self.__id, username = new_username)

        if result:
            self.__username = new_username
            return True
        else:
            return False
        
    def UpdateEmail(self, new_email):
        result = self.__db.UpdateUser(self.__id, email = new_email)

        if result:
            self.__email = new_email
            return True
        else:
            return False
        
    def IncreasePoints(self, amount):
        if(amount <= 0):
            return
        else:
            self.__rank.current_points += amount
            self.__db.UpdateUser(self.__id, points=self.rank.current_points)
        
