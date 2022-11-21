# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 03:09:24 2022

@author: Phoenix
"""

class Team:
    
    def __init__(self, Name ="Name", Origin="Origin"):
        self.teamName = Name
        self.teamOrigin = Origin
        
teamOne = Team('Arusha', 'Tanzania')
teamTwo = Team('Kigali', 'Rwanda')
teamThree=Team()

print(teamOne.teamName, teamOne.teamOrigin)
print(teamTwo.teamName, teamTwo.teamOrigin)
print(teamThree.teamName, teamThree.teamOrigin)