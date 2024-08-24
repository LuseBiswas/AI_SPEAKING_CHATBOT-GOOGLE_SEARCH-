import random
import requests
import pywhatkit
from bs4 import BeautifulSoup
from gtts import gTTS
from playsound import playsound
import os

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "temp.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)  # Remove the file after playing

print(
    "\n----------------------------------------->Welcome to LUSE CHAT-BOT Service<-----------------------------------------")
print("\n")
print("Anytime you want to quit then please write 'bye'. Hope you Enjoy!!")
print("\n")
print("\n")
list1 = ["hey bro","Great","Hello!","Hi there!","Hey! How’s it going?","What’s up?","How goes it?"]
list2 = ["I am fine and good, What about you","THANKS FOR ASKING. I’M DOING WELL","THINGS ARE GOOD"," I’VE HAD A WHIRLWIND OF A WEEK, BUT I’M HANGING IN THERE.","IT HAS BEEN A ROUGH WEEK.","I’M LOOKING FORWARD TO THE END OF THE PANDEMIC"]
list3 = ["My name is Lusee","I'm Lusee","Lusee"]
list4 = ["Yes , why not. Its my pleasure to help you","Of course.","I'd be happy to.","It would be my pleasure","Sure. What do you need help with?"]
list5 = ["Take care, Thanks for talking to me","See you soon ","I’ve got to get going","Have a nice day","I look forward to our next meeting","It was nice seeing you"]
list6 = ["I’m sorry, I didn’t catch what you said. Could you repeat it","I’m sorry, what was that?","Could you say that again, please?","I’m sorry, I’m not sure I understand what you mean to say."]
#--------------------------------------------------------------------------------------------------

while True:
    qs = input("You: ")
    if qs == "hi":
        speak(random.choice(list1))
    elif qs == "how are you":
        speak(random.choice(list2))
    elif qs == "hey":
        speak(random.choice(list1))
    elif qs == "what is your name":
        speak(random.choice(list3))
    elif qs == "who is your creator":
        speak("My creator is Ritesh Biswas")
    elif qs == "can you please help me":
        speak(random.choice(list4))
    elif qs == "can you help me":
        speak(random.choice(list4))
    elif qs == "bye":
        speak(random.choice(list5))
        break
    elif qs == "thanks":
        speak("Welcome, hope you like my company.")
    elif qs == "search":
        import wikipedia as googleScrap
        says = input("Enter your query:- ")
        speak("Here what I found on the web")
        try:
            pywhatkit.search(says)
            result = googleScrap.summary(says, 3)
            speak(result)
        except Exception:
            speak(random.choice(list6))
    else:
        speak(random.choice(list6))
