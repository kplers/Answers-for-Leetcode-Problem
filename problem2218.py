class Solution:

    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        piles_length=len(piles)
        first_pile_length=len(piles[0])
        table=[[0, piles[0][0]]]
        # Table's ith row, jth column (each starting from 0) represents the maximum value of coins if you use j coins from the first i+1 piles
        # Therefore, the answer we want to get is table's last element: i=piles_length-1 and j=k
      
        if k>1: # Let's first set the first row of the table.
            for i in range(2,k+1):
                if i>first_pile_length:
                    table[0].append(-1)
                else:
                    table[0].append(table[0][-1]+piles[0][i-1])
            

        # from the second pile, we use dynamic programming: we use the previous row's data to obtain the next row's data.
        for i in range(1,piles_length):
            pile=piles[i]
            pile_length=len(pile)
            table.append(table[-1].copy()) #First append the last row.
            pile_sum=0
            for j in range(1, 1+pile_length): #Revise the appended row.
                pile_sum+=pile[j-1]
                for m in range(j,k+1):
                    if table[-2][m-j]==-1: #It means the rest of that row isn't available.
                        break
                    if table[-2][m-j]+pile_sum>table[-1][m]: #It means that combination is larger than table[-1][m]
                        table[-1][m]=table[-2][m-j]+pile_sum #So we revise it.

        return table[-1][-1]  # return the last element of the table.                 



        
