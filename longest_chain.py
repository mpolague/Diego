# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:07:19 2019

@author: 19158
"""

def findlong(self,chain):
    chain.sort()
    
    dp = [1] * len(chain)
    
    for i in range(len(chain)):
        for j in range(i):
            if chain[j][1] < chain[i][0]:
                dp[i] = max(dp[j],dp[i]+1)
    return max(dp)