from dataclasses import dataclass
from datetime import datetime

@dataclass
class Clue:
    id: int
    user_id: int
    clue_text: str
    key: str
    date_created: datetime
    is_solved: bool

class ClueModel:
    def __init__(self, db):
        self.__db = db
        self.GenerateClues()
        self.FetchNewClue()

    def GenerateClues(self):
        # Sample dataset for "CipherHunt" 
        # Format: [Clue, Secret Key, Hint]
        clues = [
            [
                "I have keys but no locks. I have a space but no room. You can enter, but never leave.", 
                "Keyboard"
            ],
            [
                "The more of me there is, the less you see.", 
                "Darkness"
            ],
            [
                "I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me.", 
                "Fire"
            ],
            [
                "What has to be broken before you can use it?", 
                "Egg"
            ],
            [
                "I'm tall when I'm young, and I'm short when I'm old. What am I?", 
                "Candle"
            ],
            [
                "What is always in front of you but can't be seen?", 
                "Future"
            ],
            [
                "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish.", 
                "Map"
            ]
        ]

        self.__db.GenerateClues(clues)


    def GetCurrentClue(self):
        if(self.__current_clue == None):
            self.FetchNewClue()

        return self.__current_clue
    
    def FetchNewClue(self):
        result = self.__db.GetRandomClue()

        if(result):
            date = datetime.strptime(result[4], "%Y-%m-%d %H:%M:%S")
            self.__current_clue = Clue(result[0], result[1], result[2], result[3], date, result[5])
        else:
            self.__current_clue = None

        return self.__current_clue
    
    def GetClueUsername(self):
        result = self.__db.GetUserByID(self.__current_clue.user_id)

        if result:
            return result[1]
        else:
            return None
    
    def AddClue(self, clue_text, key, user_id):
        result = self.__db.AddClue(user_id, clue_text, key)

        if result:
            return True
        else:
            return False
        
    def AttemptCurrentClueSolve(self, key):
        result = self.__db.AttemptSolveClue(self.__current_clue.id, key)
        
        if(result):
            return True
        else:
            return False

     

if __name__ == "__main__":
    model = ClueModel()
    print(model.GetCurrentClue().clue_text)

    for i in range(15):
        print(model.GetPrevClue().clue_text)