
class Rank:
    def __init__(self, points=0):
        self.current_points = points
        self.ranks = [
            ('Bystander', 0),
            ('Inquisitor ', 100),
            ('Cryptic', 300),
            ('Cipher-Smith', 500),
            ('Oracle', 700)
        ]

    @property
    def next_rank_points(self):
        # resolve current rank
        i = 0
        while(i < len(self.ranks) and self.current_points >= self.ranks[i][1]):
            i += 1

        # if next rank exist, return the required points for that rank.
        if(i != len(self.ranks)):
            return self.ranks[i][1];
        #otherwise, return -1 to indicate that user is max rank.
        else:
            return -1

    @property
    def current_rank(self):
        i = 0
        while(i < len(self.ranks) and self.current_points >= self.ranks[i][1]):
            i += 1
        
        return self.ranks[i - 1]
    
