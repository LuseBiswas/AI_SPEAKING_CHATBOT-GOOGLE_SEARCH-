import pyttsx3
import random
import requests
import pywhatkit
from bs4 import BeautifulSoup
text_speech = pyttsx3.init()

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
 if (qs == "hi"):
  text_speech.say(random.choice(list1))
 elif (qs == "how are you"):
     text_speech.say(random.choice(list2))
 elif ( qs == "hey" ):
  text_speech.say(random.choice(list1))
 elif (qs == "what is your name"):
     text_speech.say(random.choice(list3))
 elif (qs == "who is your creator"):
     text_speech.say("My creator is Ritesh Biswas")
 elif (qs == "can you please help me"):
     text_speech.say(random.choice(list4))
 elif (qs == "can you help me"):
     text_speech.say(random.choice(list4))
 elif (qs == "bye"):
    text_speech.say(random.choice(list5))
 elif (qs == "thanks"):
     text_speech.say("Welcome, hope you like my company.")
 elif (qs == "search"):
    import wikipedia as googleScrap
    says=input("Enter you query:-")
    text_speech.say("Here what i found on web")
    try:
     pywhatkit.search(says)
     result=googleScrap.summary(says,3)
     text_speech.say(result)
    except Exception:
     text_speech.say(random.choice(list6))


 else:
  text_speech.say(random.choice(list6))
 text_speech.runAndWait()


