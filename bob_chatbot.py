from nltk.chat.util import Chat, reflections

QA = [
    [
         r"Hi|How are you|Is anyone there?|Moin|Hello|Good day",
            ["Hello, how can i help you","Good to see you again, how can i help you","Hi there, how can I help?", ]
    ],
    [
        r"Bye|See you later|Goodbye",
            ["See you later", "thanks for visiting","Have a nice day","Bye! Come back again soon."]
    ],
    [
        r"(.*) Thanks|(.*) Thank you|(.*) That's helpful",
            ["Happy to help!","Any time!","My pleasure"]
    ],
    [
        r"(.*)wlan(.*)",
           ["thank you for stating your problem","thank you, your problem is noted"]
    ],
    [
        r"(.*)speak|(.*)talk|(.*)call|(.*)employee|(.*)help(.*)",
            ["a employee will call you, please wait a moment","please wait a moment, a employee will call you as soon as possible"]
    ],
    [
        r"(.*)no internet(.*)|(.*)internet is not working(.*)|(.*)no connection(.*)",
            ["thank you for stating your problem,\nan employee will contact you as soon as possible","thank you, your problem is noted and will processed from an employee"]
    ],
    [
        r"(.*)calls doesnt work(.*)|(.*)i cant|can`t call(.*)|(.*)calling is not possible(.*)",
["thank you for stating your problem,\nan employee will contact you as soon as possible","thank you, your problem is noted and will processed from an employee"]    ],
    [
        r"(.*)internet crashes(.*)|(.*)no internet for short periods(.*)|(.*)internet connection is not stable(.*)",
["thank you for stating your problem,\nan employee will contact you as soon as possible","thank you, your problem is noted and will processed from an employee"]    ],
    [
        r"(.*)router is offline(.*)|(.*)router doesent work(.*)",
            ["thank you for stating your problem,\nan employee will contact you as soon as possible","thank you, your problem is noted and will processed from an employee"]
    ],
    [
        r"quit",
        ["Bye take care. Hope to see you soon friend :) ",
            "It was nice talking to you. See you soon :)"]
    ],
]


def bob():
    print("Welcome to the Solutions IT Customer Support , how can i help You? :) \nPlease type lowercase English language to start a conversation. Type quit to leave , Am here to serve you")


chat = Chat(QA, reflections)
if __name__ == "__main__":
   bob()

chat.converse()