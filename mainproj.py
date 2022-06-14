# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:29:21 2020

@author: Agarw
"""

import time
def fun(qn1):
    score=10
    right=0
    wrong=0
    for i in range(len(qn1)):
        print("_", end=" ")
        listkeep=['none']*len(qn1)
    while(score!=0):
        g=input("Guess any letter of the word. Only one letter allowed at a time:- ")
        g=g.lower()
        for k in range(len(qn1)):
                j=qn1[k]
                if(g==j):
                    listkeep[k]=j
                    right=right+1
                else:
                    if(listkeep[k]=='none' or listkeep[k]=='_'):
                        listkeep[k]='_'
                        wrong=int(wrong)
                    wrong=wrong+1
                if(wrong==len(qn1)):
                    print("\n Sorry, the guessed letter is not there in the word. Please try again. \n")
                    score=score-1
        wrong=0
        for x in listkeep:
            print(x,end=" ")
        if(right==len(qn1)):
            print("\n Congratulations! you have cracked the word rightly.")
            print("Your score for this round is: ",score)
            break
        if(score==0):
            print("Oh no you are out of turns.")
            print("the correct word was: ",qn)
            break
    return score
import random
list1=['himmachal pradesh','jammu kashmir','haryana','punjab','uttar pradesh','delhi','uttrakhand','rajasthan','gujrat','maharashtra','assam','nagaland','manipur','mizoram','tripura','west bengal','jharkhand','bihar','odisha']
list2=['grapes','lychee','cherry','apple','mango','orange','kiwi','pomegranate','papaya','pineapple','watermelon','banana']
list3=['apple','samsung','lenovo','sony','panasonic','lg','microsoft','google','britannia','coka-cola','adidas','nike','garneir','tresemme','dove','pears']
list4=['gmeet','gclassrooom','zoom','gmail','telegram','whatsapp','snapchat','instagram','youtube','flipcart','amazon','myntra','candycrush','fruit ninja']
list5=['football','basketball','cricket','tennis','hockey','badminton','volleyball','kabaddi','kho kho','chess','carrom','ludo']
print("IT TAKES 3 TO MAKE IT 30.","\n","Welcome to our word guessing game. Choose any number from 1 to 5 based on the field you are good at.")

round=0
fscore=0
g=0
while(round!=3):    
    print(" 1. Indian States names", "\n", "2. Fruits Name","\n","3.Renowned Brands Name ","\n","4. Mobile Applications ","\n","5. Sports name")
    n=int(input("Enter your choice:- "))
    if(g==n):
        print("\n Oops you have played this round already. Choose some other number than ",n,".")
        n=int(input("Enter your choice:- "))
        if(g==n):
            print("Sorry, you cannnot play further. You chose the same section again.")
            break
    if(n==1):
        sec="Indian States name guessing"
        print("Welcome to ",sec, "section. Here is a blank provided. Guess the letters of the word to complete the word and earn points.")
        qn=random.choice(list1)
        for z in range(0,7):
            if(qn==list1[z]):
                print("*HINT*  It is a northern state of India.")
        for z in range(7,10):
            if(qn==list1[z]):
                print("*HINT*  It is a western state of India.")
        for z in range(10,15):
            if(qn==list1[z]):
                print("*HINT*  It is a north-eastern state of India.")
        for z in range(15,19):
            if(qn==list1[z]):
                print("*HINT*  It is an eastern state of India.")
        qn1=list(qn)
        fscore=fscore+int(fun(qn1))
    if(n==2):
        sec="Fruits name guesssing"
        print("Welcome to ",sec, "section. Here is a blank provided. Guess the letters of the word to complete the word and earn points.")
        qn=random.choice(list2)
        for y in range(0,3):
            if(qn==list2[y]):
                print("*HINT*  It is a small sized fruit and comes in group")
        for y in range(3,8):
            if(qn==list2[y]):
                print("*HINT*  It is a medium sized fruit.")
        for y in range(8,11):
            if(qn==list2[y]):
                print("*HINT*  It is a big sized fruit.")
        if(qn==list2[11]):
            print("*HINT* This fruit is not round in shape.")
        qn1=list(qn)
        fscore=fscore+int(fun(qn1))
    if(n==3):
        sec="Brand's name guessing"
        print("Welcome to ",sec, "section. Here is a blank provided. Guess the letters of the word to complete the word and earn points.")
        qn=random.choice(list3)
        for f in range(0,7):
            if(qn==list3[f]):
                print("*HINT*  It is a company/brand which produces electronic gadgets.")
        for f in range(7,9):
            if(qn==list3[f]):
                print("*HINT* it is a famous software company.")
        for f in range(9,10):
            if(qn==list3[f]):
                print("*HINT* it is a famous food or beverages company/brands.")
        for f in range(10,12):
            if(qn==list3[f]):
                print("*HINT* it is a famous shoes brand.")
        for f in range(12,16):
            if(qn==list3[f]):
                print("*HINT* it is a brand/company which produces products for body use.")
        qn1=list(qn)
        fscore=fscore+int(fun(qn1))
    if(n==4):
        sec="Mobile application's name guessing"
        print("Welcome to ",sec, "section. Here is a blank provided. Guess the letters of the word to complete the word and earn points.")
        qn=random.choice(list4)
        for g in range(0,4):
            if(qn==list4[g]):
                print("*HINT* it is app used in online studies/classes.")
        for g in range(4,9):
            if(qn==list4[g]):
                print("*HINT* it is a very comman app used in day to day life.")
        for g in range(9,12):
            if(qn==list4[g]):
                print("*HINT* it is a e-shopping app.")
        for g in range(12,14):
            if(qn==list4[g]):
                print("*HINT* it is a gaming app.")
        qn1=list(qn)
        fscore=fscore+int(fun(qn1))
    if(n==5):
        sec="Sports name guessing"
        print("Welcome to ",sec, "section. Here is a blank provided. Guess the letters of the word to complete the word and earn points.")
        qn=random.choice(list5)
        for w in range(0,9):
            if(qn==list5[w]):
                print("*HINT* it is an outdoor game.")
        for w in range(9,12):
            if(qn==list5[w]):
                print("*HINT* it is an indoor game.")
        qn1=list(qn)
        fscore=fscore+int(fun(qn1))
    round=round+1
    g=n
    print("Round",round,"is over")
    if(round!=3):
        print("\n","Welcome to round ",int(round)+1,". Choose a number again except the one chosen before.")
print("\n","You have reached to the end of the game. Thank you for playing.")
print("Your total score is: ", fscore)
if(fscore>=25):
    print("You are a pro player. You have aced it.")
if(fscore>=20 and fscore<25):
    print("Great job! You played very well")
if(fscore>=15 and fscore<20):
    print("Good job! We appreciate your efforts")
if(fscore<15):
    print("Come back and play again. We are sure, you will do better next time.")
    
time.sleep(10)
    