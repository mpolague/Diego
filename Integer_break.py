# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 21:06:04 2019

@author: 19158
"""
def integer(number):
    
    dp = [1 for i in range(number+1)]
    
    for i in range(3,number+1):
        dp[i] = max(max(i-j,dp[i-j])*j for j in range(1,i))
    return dp[number]

print(integer(10))