class Solution:
    def solve(self,i,j,word,board,index):
        m = len(board)
        n = len(board[0])
        
        if index==len(word): 
            return True

        if i<0 or j<0 or i>=m or j>=n                  or board[i][j]=="$":
            return False

        if board[i][j] != word[index]:
            return False

        temp = board[i][j]
        board[i][j]="$"

        for x,y in [(1,0),(0,1),(-1,0),(0,-1)] :
            row = i+x
            col = j+y 
            if self.solve(row,col, word,board,index+1):
                return True

        board[i][j]= temp
        return False          
                        
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and self.solve(i,j,word,board,0):
                    return True
        return False