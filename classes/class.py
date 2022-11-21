# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 02:48:58 2022

@author: Phoenix
"""

### classes - contain certain attributes
# class classNme:
    
#     def __init__(self):
#         ## Creating attributes for the class
#         self.Attribute = 0
        
#     def anotherFunction(self):
#         Action(s)
    
class Team:
    
    def __init__(self):
        self.teamName = "Name"
        self.teamOrigin = "Origin"
           
    def defineTeamName(self, Name):
        self.teamName = Name
        
    def defineTeamOrigin(self, Origin):
        self.teamOrigin = Origin
        
teamOne =Team()

print(teamOne.teamName)

teamOne.defineTeamName("Tigers")
print(teamOne.teamName)

print(teamOne.teamOrigin) 

teamOne.defineTeamOrigin("Kenya")
print(teamOne.teamOrigin)   