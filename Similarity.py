#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 21:28:07 2018

@author: tinahuang
"""
import math

# definie class similarity
class similarity:
    
    # Class instantiation 
    def __init__ (self, ratingP, ratingQ):
        self.ratings1 = ratingP
        self.ratings2 = ratingQ

    # Minkowski Distance between two vectors
    def minkowski(self, r):
        distance = 0
        for k in self.ratings1:
            if k in self.ratings2:
                distance = distance + pow(abs(self.ratings1[k] - self.ratings2[k]), r)
        return pow(distance, 1/r)
                
    # Pearson Correlation between two vectors
    def pearson(self):
        sump = 0
        sumq = 0
        sumpq = 0
        sump2 = 0
        sumq2 = 0
        n = 0
        for item in self.ratings1.keys():
            if item in self.ratings2.keys():
                p = self.ratings1[item]
                q = self.ratings2[item]
                sump = sump + p
                sumq = sumq + q
                sumpq = sumpq + p * q
                sump2 = sump2 + pow(p, 2)
                sumq2 = sumq2 + pow(q, 2)
                n = n + 1
        
                
        denominator = 0
        
        if n == 0:
            print ('0 key match; returning -2 correlation!')
            return -2
        denominator = denominator +(math.sqrt(sump2 - pow(sump, 2) / n) * 
                                    math.sqrt(sumq2 - pow(sumq, 2) / n))
        if denominator == 0:
           print ("0 denominator; returning -2 correlation!")
           return -2
        else:
           return (sumpq - (sump * sumq) / n) / denominator
        
      
# user ratings
UserPRatings = {'Motorola':8, 'LG':5, 'Sony':1, 'Apple':1, 'Samsung':5, 'Nokia':7}
UserQRatings = {'Apple':7, 'Samsung':1, 'Nokia':4, 'LG':4, 'Sony':6, 'Blackberry':3}

SimPQ = similarity (UserPRatings, UserQRatings)
ManDist = SimPQ.minkowski(1)
EucDist = SimPQ.minkowski(2)
MinDist = SimPQ.minkowski(3)
PearsonC = SimPQ.pearson()
print (ManDist)
print (round(EucDist, 4))
print (round(MinDist, 4))
print (round(PearsonC,4))




