# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:45:48 2019

@author: 19158
"""

class StoneGame:
    def stone(self,pile_of_stones):
        N = len(pile_of_stones)
        
        def dp(i,j):
            if i > j:
                return 0
            
            play = (j-i-N) %2
            
            if play == 1:
                return max(pile_of_stones[i] + dp(i+1,j), pile_of_stones[j]+dp(i,j-1))
            
            else:
                return min(-pile_of_stones[i]+dp(i+1,j),-pile_of_stones[j]+dp(i,j-1))
            
            return dp(0,N-1) > 0
