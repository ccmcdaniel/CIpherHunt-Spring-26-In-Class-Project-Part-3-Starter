from dataclasses import dataclass
from datetime import datetime
import random

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

    # Instructor Completes this
    def GenerateClues(self):
        sample_clues = [
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

        self.__clue_data = []
        self.__id_counter = 1
        for clue in sample_clues:
            clue_obj =  Clue(self.__id_counter, 1, clue[0], clue[1], datetime.now(), False)
            self.__clue_data.append(clue_obj)
            self.__id_counter += 1

        self.__current_clue_index = -1

    # Instructor Completes This
    def GetCurrentClue(self):
        if(self.__current_clue_index != -1):
            return self.__clue_data[self.__current_clue_index]
        else:
            return None

    # Instructor Completes This
    def FetchNewClue(self):
        unsolved_clues = self.GetUnsolvedClues()

        if len(unsolved_clues) == 0:
            self.__current_clue_index = -1
            return None
        
        elif len(unsolved_clues) == 1:
            self.__current_clue_index = 0
            return self.__clue_data[unsolved_clues[0]]
        
        else:
            index = random.choice(unsolved_clues)

            while(index == self.__current_clue_index):
                index = random.choice(unsolved_clues)

            self.__current_clue_index = index
            return self.__clue_data[index]
        

    # Instructor Completes This
    def GetClueUsername(self):
        return "guest"

    # Student Completes This
    def AddClue(self, clue_text, key, user_id):
        clue_obj = Clue(self.__id_counter, user_id, clue_text, key, datetime.now(), False)
        self.__clue_data.append(clue_obj)
        self.__id_counter += 1
        return True

    # Student Completes This 
    def AttemptCurrentClueSolve(self, key):
        if(key == self.__clue_data[self.__current_clue_index].key):
            self.__clue_data[self.__current_clue_index].is_solved = True
            self.FetchNewClue()
            return True
        else:
            return False
        
    # this function is temporary until we can connect to the DB.
    def GetUnsolvedClues(self):
        result = []
        
        for i in range(len(self.__clue_data)):
            if self.__clue_data[i].is_solved == False:
                result.append(i)

        return result



if __name__ == "__main__":
    model = ClueModel()
    print(model.GetCurrentClue().clue_text)

    for i in range(15):
        print(model.GetPrevClue().clue_text)