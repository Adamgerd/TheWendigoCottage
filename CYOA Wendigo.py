#The Wendigo Cottage by Adam Gawlowski

import random
import time

w = float(1) #WendigoAlert

#def of functions

def intro(): #introduction
    time.sleep(1)
    print("------------------------------------------------------------------------------------------------------")
    print("Welcome to the [Redacted] Cottage, an adventure game created by me in my free-time that you can now play for the low low price of 0$")
    print("I hope you enjoy your playing of this adventure game, I plan to expand it in the future.")
    print("And action! 🎬")
    print("--------------------------------------------------------------------------------------------------")
    print("You have finished your long exhausting day as a banker, one that seemed even slower than most as the hours wore off.")
    print("Afterwards you picked up your wife and two children and drove overnight from the streets of Chicago to your family cottage in the remote Appalachian hills.")
    print("Saturday morning, you arrive, exhausted from your long journey but ready to relax in the Appalachian hills at your cottage.")
    print("You and your family take your luggageo ut of the car into the cottage and then exhausted you sleep until your wife wakes up in the evening")
    print("The sun is slowly settling accross the horizon and it is soon time for dinner...")

def act1(): #Act I "Dinner"
    time.sleep(1)
    print("------------------------------------------------------------------------------------------------------")
    global w
    w = float(1)
    answer = 0
    answer = input("You decide to cook dinner yourself, now well-rested from the car ride here. You are debating whether yoou should do an outside barbecue for dinner or whether you should cook a regular dinner indoor?\n")
    if answer == "outside" or answer == "bbq" or answer == "barbecue" or answer == "ÿard" or answer == "outdoor":
        answer = input("Wanting to experience the great outdoors, after all that was the whole reason for coming here, you have decided to cook barbecue outside on the yard near the forest. Now should you cook sausages and grilled meat or give in to your fchildren's demands for marshmallows?\n")
        if answer == "marshmallows" or answer == "sweets" or answer == "kids":
            print("To the delight of your children and likely dismay of your wife, you have given in and you are now carrying bags of marshmallows to the barbecue preparing everything for cooking marshmallows.")
            w = w+10
        if answer == "ribs" or answer == "grilled meat" or answer == "sausage":
            print("To the dismay of your children but with the blessing of your wife, you have decided to roast sausages on the open fire with mustard and ketchup.")
            w = w+20
    if answer == "inside" or answer == "dinner" or answer == "indoor":
        answer = input("Wanting to stay inside where it was warm and snug and with bugs flying around outside, you have decided to stay indoors. Now you face yet another choice: Do you decide to cook steak with potatoes or do you decide to create something sweet to cap off the first day like sweet dumplings?\n")
        if answer == "steak with potatoes" or answer == "steak" or answer == "potatoes":
            print("You have decided to cook steak with potatoes indoor with the aroma slowly drifting everywhere within the house and eventually you all sit down to enjoy steak with potatoes.")
            w = w+5
        if answer == "sweet" or answer == "dumplings" or answer == "sweet dumplings":
            print("You have decided to cook something sweat and after much thinking remembered your grandmother's recipe for sweet dumplings and after cooking them and pouring butter and sugar on them, you sit down to eat.")
            w = w+1
            
#start of program
            
intro()      
act1()
