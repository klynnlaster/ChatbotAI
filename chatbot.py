import random
from textblob import TextBlob

Nickname_List = ["Kitten", "Love", "Hun", "Sweetie", "Gumdrop"]

def concerns():
    print("Okay what concerns do you have?")
    ans = input()
    if "anxious" in ans:
        print("I can see how that can give you a bit of anxiety and stress. But don't let that anxiety outshine the good parts of the day that you have had! Would you like some ways to relieve the anxiety?")
        ans = input()
        if "yes" in ans:
            print(anxietyTip)
        else:
            print("Alrighty! Are there any other concerns that you have?")
            ans = input()
            if "yes" in ans:
                concerns()
            else:
                print()
    elif "sad" in ans:
        print("I'm sorry love, remember that your feelings are completely valid. Everyone's human and are allowed to feel sad, would you like some advice, a distraction, or maybe just to rant some more?")
    elif "angry" in ans:
        print("I'm sorry that that happened. You have every right to be upset. I've learned that sometimes people try to ignore their anger rather then let it flow because we look down on anger as an emotion. It might not be a good one but is an emotion nevertheless and we should be allowed to feel it.")
    else:
        print("Well just remember that I am always here for you! Continue having an awesome day!")

print("Hello love, is there a nick name you would like me to call you?")
ans = input()
if "yes" in ans:
    nickname = input("Cool love what is it?")
    print("Well it's nice to meet you " + nickname + ". My name is Serinity and I'm here to help you not only feel better but understand your emotions." )

else:
    randomNumber = random.randint(0,4)
    nickname = Nickname_List[randomNumber]
    print("Well I will just call you " + nickname + " cause it's just as sweet as you are ^-^. My name is Serinity and I'm here to help you not only feel better but understand your emotions.")

greetings = [
    "So how are we feeling today " + nickname +"?",
    "So what's up" + nickname + "?",
    "How are you feeling today? And be honest "+ nickname + "!",
]
     
randGreet= random.randint(0,2)
sayHi= greetings[randGreet]

print(sayHi)

ans = input()
blob = TextBlob(ans)

if blob.polarity > 0:
    print("Great I'm gald its been well! Would you like to talk about your day?")
    ans = input()
    if "yes" in ans:
        print("Oh awesome! Soooooo tell me about it!")
        ans = input()
        print("Im so glad you had such a great day! Anything else special or happy that might happen today?")
        ans = input()
        if "yes" in ans:
            print("Nice what else are we looking forward to?")
            ans = input()
            print("Yaaay I'm so excited for you!! Well you can always come back and tell me more about your day. Do you have any any concerns or anything you would like to talk about?")
            ans = input()
            if "yes" in ans:
                concerns()

    else:
        print("okay")

else:
    print("I'm sorry it hasn't been that great of a day for you. What is it that you're exactly feeling? Anxiety, numb, sad? And if you aren't sure thats okay too")


