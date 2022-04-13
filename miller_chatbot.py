# Rule_based Nltk chatbot- using NLTK Library.
from nltk.chat.util import Chat, reflections

QA = [
    [
         r"Hi|How are you|Is anyone there?|Moin|Hello|Good day",
            ["Hello, thanks for visiting","Good to see you again","Hi there, how can I help?", ]
    ],
    [
        r"Bye|See you later|Goodbye",
            ["See you later", "thanks for visiting","Have a nice day","Bye! Come back again soon."]
    ],
    [
        r"Thanks|Thank you|That's helpful",
            ["Happy to help!","Any time!","My pleasure"]
    ],
    [
        r"no wlan|wlan is not working|no signal",
           ["thank you for stating your problem","thank you, your problem is noted"]
    ],
    [
        r"can i speak with a employee|i need personal help",
            ["a employee will call you, please wait a moment"]
    ],
    [
        r"no internet|internet is not working|no connection",
            ["thank you for stating your problem","thank you, your problem is noted"]
    ],
    [
        r"calls doesnt work|i cant call|calling is not possible",
            ["thank you for stating your problem","thank you, your problem is noted"]
    ],
    [
        r"internet crashes|no internet for shot piriods|internet connaction is no stabil",
            ["thank you for stating your problem","thank you, your problem is noted"]
    ],
    [
        r"router is offline|router doesent work",
            ["thank you for stating your problem","thank you, your problem is noted"]
    ],
]


def miller():
    print("Hi, I'm Tom. I know you like delicious meals , i believe thats why you are here? :) \nPlease type lowercase English language to start a conversation. Type quit to leave , Am here to serve you")


chat = Chat(QA, reflections)
if __name__ == "__main__":
   miller()

chat.converse()