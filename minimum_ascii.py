# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 22:31:34 2019

@author: 19158
"""

class MinimumAscii(object):
    
    def min_DeleteSum(self, string1, string2):
        dp = [[0] * (len(string2) + 1) for l in range(len(string1) + 1)]

        for first in range(len(string1) - 1, -1, -1):
            dp[first][len(string2)] = dp[first+1][len(string2)] + ord(string1[first])
            
        for second in range(len(string2) - 1, -1, -1):
            dp[len(string1)][second] = dp[len(string1)][second+1] + ord(string2[second])

        for first in range(len(string1) - 1, -1, -1):
            for second in range(len(string2) - 1, -1, -1):
                
                if string1[first] == string2[second]:
                    dp[first][second] = dp[first+1][second+1]
                else:
                    dp[first][second] = min(dp[first+1][second] + ord(string1[first]),
                                   dp[first][second+1] + ord(string2[second]))

        return dp[0][0]