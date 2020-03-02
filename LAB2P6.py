#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:34:30 2020

@author: Maui
"""
import random


class Player:
    rollsCount = 0
    money = 50
    point = 0
    def rollDice(self):
        roll = random.randint(2,12)
        self.rollsCount+=1
        return roll
    def isWinner(self, bet):
        self.money = self.money + (bet * 2)
        print("You win!")
        self.printBalance()
        self.point = 0
    def isLoser(self, bet):
        self.money = self.money - bet
        print("You lose!")
        self.printBalance()
        self.point = 0
    def isDraw(self, bet):
        print("You get your money back!")
        self.printBalance()
        self.point = 0
    def pointPlay(self, bet):
        current_die = self.rollDice()
        print("Dice  Roll: ", current_die)
        if current_die == self.point:
            self.isWinner(bet)
        elif current_die == 7 or 11:
            self.isLoser(bet)
        elif current_die == 12:
            self.isDraw(bet)
        else:
            self.pointPlay(bet)
    def passPlay(self, bet):
        cur_point = self.point
        if cur_point == 0:
            self.printBorder()
            print("Pass Play!")
            current_die = self.rollDice()
            print("Dice  Roll: ", current_die)
            if current_die == 7 or current_die == 11:
                self.isWinner(bet)
            elif current_die == 4 or current_die == 5 or current_die == 8 or current_die == 10:
                self.point = current_die
                self.passPlay(bet)
            elif current_die == 2 or 3 or 12:
                self.isLoser(bet)
            else:
                self.passPlay(bet) 
        elif cur_point != 0:
            self.printBorder()
            print("Point Play!")
            self.pointPlay(bet)
        else:
            self.passPlay(bet)
    def dontPassPlay(self, bet):
        cur_point = self.point
        if cur_point == 0:
            self.printBorder()
            print("Don't Pass Play!")
            current_die = self.rollDice()
            print("Dice Roll: ", current_die)
            if current_die  == 2 or current_die == 3:
                self.isWinner()
            elif current_die == 12:
                self.isDraw()
            else:
                self.point = current_die
                self.dontPassPlay(bet)
        elif cur_point != 0:
            self.printBorder()
            print("Point Play!")
            self.pointPlay(bet)
        else:
            self.dontPassPlay(bet)
    def placeBet(self):
        bet = float(input("Enter bet amount: "))
        if bet > 0 and (self.money - bet) >= 0:
            self.playType(bet)
        else:
            print("You do not have enough money.")
            self.placeBet()
    def playType(self, bet):
        self.printBorder()
        print("1 - Pass Line\n2 - Don't Pass Line")
        play_choice = int(input("Play Type: "))
        if play_choice == 1:
            self.passPlay(bet)
        elif play_choice == 2:
            self.dontPassPlay(bet)
        else:
            self.playType()
    def playOneGame(self):
        self.printBorder()
        print("You have chosen to play One Game")
        self.placeBet()
        print("Thank you for playing!")
    def playManyGames(self):
        if self.money > 0:
            self.placeBet()
            play_on = int(input("Continue?\n1 - Yes\n2 - No\n: "))
            if play_on == 1:
                self.playManyGames()
            elif play_on == 2:
                print("Thank you for playing!")
            else:
                self.playManyGames()
        else:
            print("You are out of balance!\nThank you for playing!")
        
    def printBorder(self):
        print("====================================================================")
    def printBalance(self):
        print("\t\t\t=======================")
        print("\t\t\t=   YOU HAVE $", float(self.money), "  =")
        print("\t\t\t=======================")
    def atStartup(self):
        self.printBorder()
        print("\n\t\tWELCOME TO CRAPS GAME TERMINAL EDITION\n")
        self.printBorder()
        self.printBalance()
        print("1 - Play One Game\n2 - Play Many Games\n3 - Exit")
        menu_choice = int(input("Play?: "))
        if menu_choice == 1:
            self.playOneGame()
        elif menu_choice == 2:
            self.printBorder()
            print("You have chosen to play Many Game")
            self.playManyGames()
        elif menu_choice == 3:
            pass
        else:
            self.atStartup()

Player1 = Player()
Player1.atStartup()
        
                

