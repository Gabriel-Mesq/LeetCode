class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max = 0
        
        for i in range(len(accounts)): #Numero de pessoas
            
            sum = 0
            
            for j in range(len(accounts[i])): #Numero de contas bancarias
            
                sum += accounts[i][j]
                
            if sum > max:
                max = sum
            
        return max
