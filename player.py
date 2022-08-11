from random import randint, random
from board import GameBoard

class ai:
    def __init__(self,size,team):
        id = randint(0,10000)
        self.currMove = 0
        self.preferences = {}
        self.size = size
        
        self.team = team
        
        for a in range(self.size*self.size):
            self.preferences[a] = random()
        
        self.preferences = dict(sorted(self.preferences.items(), key=lambda item: item[1]))

    def __str__(self):
    
        buf = ''
        
        
        
        for key,value in self.preferences.items():
            buf += f'{key}: {value}\n'
        return buf

    
    def play(self,game):
        moved = False
        for key,value in self.preferences.items():
            if moved:
                break
            if game.move(self.team,key) == True:
                moved = True
        
            
            
        
        
        
        
    
    
