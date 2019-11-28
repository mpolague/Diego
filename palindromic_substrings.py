# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:53:17 2019

@author: 19158
"""

def CountPalindromic(str,letters):
    dp = [[0 for x in range(letters)] for y in range(letters)]
    palindrome = [[False for x in range(letters)] for y in range(letters)]
    
    for i in range(letters):
        palindrome[i][i] = True
        
    for let in range(letters-1):
        if (str[let] == str[let+1]):
            palindrome[let][let+1] = True
            dp[let][let+1] = 1
    
    for gap in range(2,letters):
        for let in range(letters-gap):
            j = gap+let
            
            if(str[let] == str[j] and palindrome[let+1][j-1]):
                palindrome[let][j] = True
                
                if (palindrome[let][j] == True):
                    dp[let][j] = (dp[let][j-1]+ dp[let+1][j] + 1-dp[let+1][j-1])
                else:
                    dp[let][j] = (dp[let][j-1] + dp[let+1][j] - dp[let+1][j-1])
            