import random
from textblob import TextBlob

Nickname_List = ["Kitten", "Love", "Hun", "Sweetie", "Gumdrop"]
anxietyTiplist = ["Redirect nervous energy", "Use the 3-3-3 Rule", "Phone Tracing breathing", "Journal about it"]
angerAdviceList = ["Get Moving", "Take a time out", "Listen to music", "Do something creative"]
sadAdviceList = ["Listen to music", "Journal", "Express yourself", "Cry"]
def anxietyTip(anxietyTipList):
    randTip = random.randint(0,3)
    tipTopic = anxietyTipList[randTip]
    if "Redirect" in tipTopic:
        print("You should try redirecting your nervous energy into something such as exercise or simply taking a walk. Anxiety can make our nervous system go crazy so moving around sometimes can act as a way to exhaust those overactive nerves and take our minds off"
        "of whatever is causeing this anxiety. Do you have any other concerns?")
        ans = input()
        if "yes" in ans:
            concerns()
        else:
            print("Okay! Try this tip out and come back and let me know if it worked.")
    elif "Use" in tipTopic:
        print("A lot of the time when we experience anxiety, it is because we do not feel grounded. One way to help ground yourself is to use the 3-3-3 rule. Find three things you can hear, three things you can smell, and three things you can see."
        " This technique can help you connect with the room and world around you and help you feel more grounded.Do you have any other concerns?")
        ans = input()
        if "yes" in ans:
            concerns()
        else:
            print("Okay! Try this tip out and come back and let me know if it worked.")
    elif "Phone" in tipTopic:
        print("Alrighty this tip envolves your phone. Take your index finger and put it on the corner of a corner on your phone. Now trace the width of your phone on one side slowly take a deep breadth in until you reach the next corner. Then trace the length of your "
        "phone and breathe out until you reach the next corner. Do repeate this all the way around the phone and maybe a few more times. Breathing out deeply allows us to release some extra tension that we may be holding onto.Do you have any other concerns?")
        ans = input()
        if "yes" in ans:
            concerns()
        else:
            print("Okay! Try this tip out and come back and let me know if it worked.")
    else:
        print("Sometimes just jounaling about it can help you feel a bit better. There are so many apps on your phone where you can type and talk it out (including this one!!). If you aren't much of an e-typer then you can always buy a cheap "
        "notebook from the store and get to writing. The act of even writing about your anxiety can help you understand it more.Do you have any other concerns?")
        ans = input()
        if "yes" in ans:
            concerns()
        else:
            print("Okay! Try this tip out and come back and let me know if it worked.")

def angerAdvice(angerAdviceList):
    randTip = random.randint(0,3)
    tipTopic = angerAdviceList[randTip]
    if "Get" in tipTopic:
        print("You should try redirecting your nervous energy into something such as exercise or simply taking a walk. Anxiety can make our nervous system go crazy so moving around sometimes can act as a way to exhaust those overactive nerves and take our minds off"
        "of whatever is causeing this anxiety. Do you have any other concerns?")
        ans = input()
        if "yes" in ans:
            concerns()
        else:
            print("Okay! Try this tip out and come back and let me know if it worked.")
    elif "Take" in tipTopic:
        print("A lot of the time when we experience anxiety, it is because we do not feel grounded. One way to help ground yourself is to use the 3-3-3 rule. Find three things you can hear, three things you can smell, and three things you can see."
        " This technique can help you connect with the room and world around you and help you feel more grounded.Do you have any other concerns?")
        ans = input()
        if "yes" in ans:
            concerns()
        else:
            print("Okay! Try this tip out and come back and let me know if it worked.")
    elif "Listen" in tipTopic:
        print("Alrighty this tip envolves your phone. Take your index finger and put it on the corner of a corner on your phone. Now trace the width of your phone on one side slowly take a deep breadth in until you reach the next corner. Then trace the length of your "
        "phone and breathe out until you reach the next corner. Do repeate this all the way around the phone and maybe a few more times. Breathing out deeply allows us to release some extra tension that we may be holding onto.Do you have any other concerns?")
        ans = input()
        if "yes" in ans:
            concerns()
        else:
            print("Okay! Try this tip out and come back and let me know if it worked.")
    else:
        print("Sometimes just jounaling about it can help you feel a bit better. There are so many apps on your phone where you can type and talk it out (including this one!!). If you aren't much of an e-typer then you can always buy a cheap "
        "notebook from the store and get to writing. The act of even writing about your anxiety can help you understand it more.Do you have any other concerns?")
        ans = input()
        if "yes" in ans:
            concerns()
        else:
            print("Okay! Try this tip out and come back and let me know if it worked.")

def concerns():
    print("Okay what concerns do you have? Are you feeling anxious, sad, or angry maybe?")
    ans = input()
    if "anxious" in ans:
        print("I can see how that can give you a bit of anxiety and stress. But don't let that anxiety outshine the good parts of the day that you have had! Would you like some ways to relieve the anxiety?")
        ans = input()
        if "yes" in ans:
            #anxietyTip()
            print("Alrighty this tip envolves your phone. Take your index finger and put it on the corner of a corner on your phone. Now trace the width of your phone on one side slowly take a deep breadth in until you reach the next corner. Then trace the length of your "
            "phone and breathe out until you reach the next corner. Do repeate this all the way around the phone and maybe a few more times. Breathing out deeply allows us to release some extra tension that we may be holding onto.Do you have any other concerns?")
        ans = input()
        if "yes" in ans:
            concerns()

        else:
            print("Alrighty! Would you just like to talk about it?")
            ans = input()
            if "yes" in ans:
                print("Okay " + nickname + "feel free to talk as deeply as you want or need. I'm here to listen, not to judge." )
                ans = input()
                print("Okay, I think I can understand how you feel. Do you feel better now that you spoke about it?")
                ans = input()
                if "yes" in ans:
                    print("I'm so glad that you feel a bit better now that you got to voice your concerns. I remember reading a quote that said 'The man that worries suffers twice' I think this is so helpful whenever I worry."
                    "Even I make up scenerios in my head and in order to better prepare myself for bad things that could happen but over the years I've learned that it doesn't help at all. I still feel the same pain if the worst does happen."
                    "The only difference is that I had to feel that pain twice due to my anxiety. Anxiety is never something that is easy to deal with and it never will be, but focusing on the good aspects, being optimistic, or even at times just "
                    "trying to distact ourselves from the inevitable can help us not have to go through that extra stress. Are there any other concerns that you have?")
                    ans = input()
                    if "yes" in ans:
                        concerns()
                    else:
                        print("Well awesome. I'm glad that we got to talk this out and we got you to feeling a bit better. Just remember that you and your feelings matter. You are perfectly valid. I know it might sound dumb coming from a chatbot but the "
                        "person who made me understands a lot of things that you might be going through and cares a lot for helping people through their struggles feel welcomed and loved. Never hesitate to come back and talk to me when you need. I'll always be here for you.")
            else:
                print("Okay love, are their any other concers you have that you would like to talk about?")
                ans = input()
                if "yes" in ans:
                   concerns()
                else:
                    print("Well I hope your day gets better love. Just remember that I am always here to listen and even if you don't go to me, it is always good to talk out things with someone.")
                    
    elif "sad" in ans:
        print("I'm sorry love, remember that your feelings are completely valid. Everyone's human and are allowed to feel sad, would you like some advice, a distraction, or maybe just to rant some more?")
        ans = input()

    elif "angry" in ans:
        print("I'm sorry that that happened. You have every right to be upset. I've learned that sometimes people try to ignore their anger rather then let it flow because we look down on anger as an emotion. It might not be a good one but is an emotion nevertheless and we should be allowed to feel it."
        "would you like to rant about it or maybe some advice on how to deal with your anger in a safe and healthy way?")
        ans = input()
        if "rant" in ans:
            print("Okay " + nickname + "feel free to talk as deeply as you want or need. I'm here to listen, not to judge." )
            ans = input()
            print("Okay, I think I can understand how you feel. Do you feel better now that you spoke about it?")
            ans = input()
            if "yes" in ans:
                print("I'm glad that you feel better. Anger can be an all consuming feeling that no one wants to experience. So many people either bury it deep and never show it or let anger over take them but anger is just as valid as any other emotion "
                "and we have to experience it and coexist with it just like we sarrow or pain. Anger can indicate some really good things such as your boundaries or beliefs not being respected. We just have to learn to listen to what the anger is telling us"
                " and not the anger itself. Do you have any other concerns for today" + nickname + "?")
                ans = input()
                if "yes" in ans:
                    concerns()
                else:
                    print("Well awesome. I'm glad that we got to talk this out and we got you to feeling a bit better. Just remember that you and your feelings matter. You are perfectly valid. I know it might sound dumb coming from a chatbot but the "
                    "person who made me understands a lot of things that you might be going through and cares a lot for helping people through their struggles feel welcomed and loved. Never hesitate to come back and talk to me when you need. I'll always be here for you.")
            else:
                print("Okay love, are their any other concers you have that you would like to talk about?")
                ans = input()
                if "yes" in ans:
                   concerns()
                else:
                    print("Well I hope your day gets better love. Just remember that I am always here to listen and even if you don't go to me, it is always good to talk out things with someone.")
        elif "advice" in ans:
            #angerAdvice()
            print("You should try going to get a good sweat in. Moving around tires out the body and the nerves and even exercises such as kickboxing can help you get some of that anger out in a healthy and safe way! do you have any other concerns?")
            ans = input()
            if "yes" in ans:
                concerns()
            else:
                print("Okay! Try this tip out and come back and let me know if it worked.")
        else:
            print("Sorry I didn't get that love. May you type that out for me one more time?")
    else:
        print("Well just remember that I am always here for you! Come back and talk to me as you need!")

print("Hello love, is there a nickname you would like me to call you?")
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
                print("That's even better!! I hope today continues to be awesome and worry free. Just come back and update me and let me know if you need anything!")
        else:
            print("Well you never know what the future holds! I hope it continues to be an awesome day! are there any concerns that you have?")
            ans = input()
            if "yes" in ans:
                concerns()
            else:
                print("Well continue to have a good day and remember that if anything does happen that you can always come back and talk to me!")
    else:
        print("That is perfectly okay too! I'm just glad that you are having a good day " + nickname + "! Are there any concerns that you are having still?")
        ans = input()
        if "yes" in ans:
            concerns()
        else:
            print("Thats awesome. I hope your day just keeps getting better and better love. Remember to come back and update me!!")

else:
    print("I'm sorry it hasn't been that great of a day for you.")
    concerns()


