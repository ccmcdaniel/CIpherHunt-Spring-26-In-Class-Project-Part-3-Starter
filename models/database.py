import sqlite3

class DatabaseModel:
    def __init__(self, path):
        self.__path  = path

        conn = sqlite3.connect(self.__path)
        cursor = conn.cursor()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS User (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    points INTEGER DEFAULT 0 
                )
            ''')

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS Clue (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    clue_text TEXT,
                    key TEXT,
                    date_created DATE DEFAULT (datetime('now','localtime')),
                    is_solved BOOLEAN DEFAULT 0,
                    FOREIGN KEY (user_id) REFERENCES User(id)
                )
            ''')
        
        conn.commit()
        conn.close()

    #----------------User Operations--------------------
    def AddUser(self, username, email):
        try:
            conn = sqlite3.connect(self.__path)
            cursor = conn.cursor()
            
            cursor.execute("INSERT INTO User(username, email) VALUES(?, ?)", (username, email))

            conn.commit()
            conn.close()

            return True
        
        except sqlite3.Error:
            return False


    def GetUserByUsername(self, username):
        try:
            conn = sqlite3.connect(self.__path)
            cursor = conn.cursor()

            result = cursor.execute("SELECT * FROM User WHERE username=?", (username,)).fetchall()

            if len(result) != 0:
                result = result[0]
            else:
                result = None

            conn.commit()
            conn.close()

            return result
        
        except sqlite3.Error as e:
            print(e)
            return None

    def GetUserByID(self, id):
        try:
            conn = sqlite3.connect(self.__path)
            cursor = conn.cursor()

            result = cursor.execute("SELECT * FROM User WHERE id=?", (id,)).fetchall()

            if len(result) != 0:
                result = result[0]
            else:
                result = None

            conn.commit()
            conn.close()

            return result
        
        except sqlite3.Error as e:
            print(e)
            return None
        
    def UpdateUser(self, id, username=None, email=None, points=None):
        sql = "UPDATE USER SET "
        values = ()

        if username == None and email == None and points == None:
            return

        count = 0
        if username != None:
            sql += "username=?"
            values += tuple([username])
            
            count += 1
        
        if email != None:
            if count > 0:
                sql += ','

            sql += "email=?"
            values += tuple([email])
            
            count += 1
        
        if(points != None):
            if count > 0:
                sql += ','
            
            sql += "points=?"
            values += tuple([points])
            
            count += 1

        sql += " WHERE id=?"
        values += tuple([id])
        
        try:
            conn = sqlite3.connect(self.__path)
            cursor = conn.cursor()

            result = cursor.execute(sql, values)

            conn.commit()
            conn.close()

            return True

        except sqlite3.Error as e:
            print(e)
            return False    

    def EraseUserData(self, id):
        pass

    #----------------Clue Operations---------------------
    def AddClue(self, user_id, clue_text, key):
        try:
            conn = sqlite3.connect(self.__path)
            cursor = conn.cursor()
            
            cursor.execute("INSERT INTO Clue(user_id, clue_text, key) VALUES(?, ?, ?)", (user_id, clue_text, key))

            conn.commit()
            conn.close()

            return True
        
        except sqlite3.Error:
            return False
    
    def GetRandomClue(self):
        try:
            conn = sqlite3.connect(self.__path)
            cursor = conn.cursor()
            
            result = cursor.execute("SELECT * FROM Clue Where is_solved=0 ORDER BY RANDOM() LIMIT 1").fetchall()

            if(len(result) > 0):
                result = result[0]
            else:
                result = None

            conn.commit()
            conn.close()

            return result
        
        except sqlite3.Error:
            return None
    
    def GetClueByID(self, id):
        try:
            conn = sqlite3.connect(self.__path)
            cursor = conn.cursor()
            
            result = cursor.execute("SELECT * FROM Clue WHERE id=?", (id,)).fetchall()

            if(len(result) > 0):
                result = result[0]
            else:
                result = None

            conn.commit()
            conn.close()

            return result
        
        except sqlite3.Error:
            return None

    def AttemptSolveClue(self, id, key):
        clue = self.GetClueByID(id)

        if(clue):
            if key.lower() == clue[3].lower():
                try:
                    conn = sqlite3.connect(self.__path)
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Clue SET is_solved=1 WHERE id=?", (id,))
                    conn.commit()
                    conn.close()
                    return True
                except sqlite3.Error as e:
                    print(e)
                    return False
            else:
                return False
        else:
            return False
        
    def GenerateClues(self, data):
        self.ClearClueTable()
        
        for clue in data:
            self.AddClue(1, clue[0], clue[1])


    # ---Utility Operations--

    def ClearUserTable(self):
        conn = sqlite3.connect(self.__path)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM User")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name=\'User\'")

        conn.commit()
        conn.close()

    def ClearClueTable(self):
        conn = sqlite3.connect(self.__path)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM Clue")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name=\'Clue\'")

        conn.commit()
        conn.close()

    def ResetDatabase(self):
        self.ClearClueTable()
        self.ClearUserTable()
    
    
if __name__ == "__main__":
    db = DatabaseModel("test_db.db")
    #db.AddUser("john_doe2903", "johndoe2938@gmail.com")

    # ---User operations test---
    '''
    print(db.GetUserByUsername("john_doe2903"))
    print(db.GetUserByUsername("john_doe2903439"))
    print(db.GetUserByID(1))
    print(db.GetUserByID(2))
    print(db.GetUserByID('1'))
  
    db.UpdateUser(1, username="john_doe4545")
    db.UpdateUser(1, email="john_doe4545@gmail.com")
    db.UpdateUser(1, username="jane_doe4534", email="jane_doe4545@gmail.com")
    db.UpdateUser(1, points=34)


    print(db.GetRandomClue())
    print(db.GetRandomClue())
    print(db.GetRandomClue())
    print(db.GetRandomClue())
    print(db.GetRandomClue())
    print(db.GetRandomClue())

    print(db.AttemptSolveClue(5, 'Candle'))
    print(db.AttemptSolveClue(3, 'Chad'))
    '''