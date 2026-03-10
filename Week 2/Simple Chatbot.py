#Name: Ryan Xu
#Date 3/9/2026
#Title: Simple Chatbot

import random

def chatbot():
    moods = ["bad", "good", "meh", "great", "amazing"]
    foods = ["pizza", "sushi", "tacos", "burgers"]
    chance = random.randint(1, 2)

    print(
        "Hi there! I'm a newly made chatbot, here to ask you about your day! But start off what's your name?"
    )
    name = input("Enter your name: ")
    print("Okay " + name + " How are you feeling today?")
    answer = input("")
    print("Well I suppose that's good to hear that your feeling " + answer +
          " today! I'm feeling " + random.choice(moods) + " today.")
    print(
        "On another topic seeing as that one went... well. What is your favorite food?"
    )
    answer = input("")
    print("I see, I see. I'm personally a fan of " + random.choice(foods) +
          " but I suppose yours is just alright")
    print(
        "Well to finally see if well get along alright, I'll ask you one final question. Put it all on black or red?"
    )
    answer = input("")

    if chance == 1:
        chance = "BLACK"

    if chance == 2:
        chance = "RED"

    if chance == answer.upper():
        print("A WIN, WELL GET ALONG JUST FINE!")
    else:
        print("A LOSS ARE YOU KIDDING ME?! GET OUT OF MY SIGHT!")


chatbot()
