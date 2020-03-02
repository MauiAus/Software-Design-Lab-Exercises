#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:13:37 2020

@author: Maui
"""

class Account:
    user = ["Mark", "Marielle", "Ana"]
    password = ["123", "321", "312"]

    def __init__(self, userw, passw):
        self.userw = userw
        self.passw = passw

    def matchUser(self):
        if self.userw in self.user:
            return True
        else:
            return False
    def matchPass(self):
        if self.passw in self.password:
            return True
        else:
            return False
    def AccMatch(self):
        if (self.matchUser() and self.matchPass() == True):
            if self.user.index(self.userw) == self.password.index(self.passw):
                return True
            else:
                return False
        else:
            return False
    def MatchAcc(self):
        if (self.AccMatch() == True):
            return True
        else:
            return False
                

def login():
    error = 0
    while error != 3 or error != 10:
        inUser = input("Enter your User: ")
        inPass = input("Enter your Pass: ")
        check = Account(inUser,inPass)
        if(check.MatchAcc() == True):
            error = 10
            break
        else:
            error += 1
            if error == 3:
                break
            print("Invalid user or password!! \nIf login is failed", (3-error), "more times the Police will be alerted")
    if(error == 3):
        print("Invalid login. \nThe Police have been alerted!")
    elif(error == 10):
        print("Login successful")

login()
        
    

            
