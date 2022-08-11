
class GameBoard:
    def __init__(self,size):
        
        self.size = size
        self.board = {}

        for a in range(self.size*self.size):
            self.board[a] = 0

        self.end = False
        self.tie = False
        self.win = False

    def __str__(self):
        buf = '\n'
        
        buf += '+-----'*self.size+'+\n'
        
        for c in range(self.size):
            for a in range(3):
                for b in range(self.size):
                    #print(self.size*c+b,a)
                    if self.board.get(self.size*c+b) == 0:
                        buf += '|     '
                    elif self.board.get(self.size*c+b) == 1:
                        if a % 2 == 0:
                            buf += '|  O  '
                        else:
                            buf += '| O O '
                    elif self.board.get(self.size*c+b) == 2:
                        if a % 2 == 0:
                            buf += '| X X '
                        else:
                            buf += '|  X  '
                buf += '|\n'
            buf += '+-----'*self.size+'+\n'
            
        return buf
        
    def __checkEnd(self):
   
            

    
        for key,value in self.board.items():
            if value == 0:
                return
        
        self.end = True
       
       
    def __checkEmpty(self,pos):
        if pos < 0 or pos >= self.size*self.size:
            print("ERROR POSITION OUT OF BOUNDS")
        else:
            if self.board.get(pos) == 0:
                return True
        return False

    def move(self,player,pos):
        if pos < 0 or pos >= self.size*self.size:
            print("ERROR POSITION OUT OF BOUNDS")
            return False
        else:
            if player == 1:
                if self.__checkEmpty(pos):
                    self.board[pos] = player
                    self.__checkEnd()
                    return True
                return False

            elif player == 2:
                if self.__checkEmpty(pos):
                    self.board[pos] = player
                    self.__checkEnd()
                    return True
                return False
            else:
                print("ERROR UNKNOWN PLAYER")
                return False
                

        

    
