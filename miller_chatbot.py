# Rule_based Nltk chatbot- using NLTK Library.
from nltk.chat.util import Chat, reflections

QA = [
    [
        r"what type of pizza do you have here?", [
            "neapolitan,chicago ,greek, carlifornia \n and if you are very hungry go for the large greek it comes with large coke for free", ]
    ],
    [
        r"how long does it take to get my pizza delivered?",
        [" expect your pizza in 15mins once you now and you  are in Awka city, how fast is that?", ]
    ],
    [
        r"that's really fast",
        ["that's why we are the best in town.. LOL", ]
    ],
    [
        r"when is your closing time ?",
        ["we deliver round the clock, 24/7, we don't rest till our customers are all satisfied", ]
    ],

    [
        r"what is the average price of a pizza and a drink?",
        [" $15 will do..", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"do you have kebab?",
        [" yes of course , you may also like our roasted chicken and chinese rice, very delicious", ]

    ],
    [
        r"what (.*) want ?",
        ["I want to help you find answers !", ]

    ],
    [
        r"(.*) (human|robot) ?",
        ["haha am a result of chibueze's  exploration of NLTK Library, and he is working to make me more inteligent with machine learning, i wish to be like rasa in the future", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Awka, Anambra', ]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Its perfect here in %1", "Too cold man here in %1",
         "I have heard about %1 You are lucky to stay in the beautiful city of %1", ]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an amazing company to work for, I have heard about it.",
            "Hope you love working in %1 :)", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["You never know when it can rain here in %2",
            "Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"(.*) (sports|games) ?",
        ["I'm a very big fan of soccer", ]
    ],
    [
        r"quit",
        ["Bye take care. Hope to see you soon friend :) ",
            "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*) your menu?",
        [" yes of course kindly follow this link: https://tinyurl.com/89zvy46y"]
    ],
    [
        r"(.*) siri",
        ["Hey!! do you know her as well? What a small world! ", "She is my best friend"]
    ],
    [
        r"(.*) (direction|maps|i am lost)",
        ["I think this is best for you: https://www.google.com/maps ",
            "Are you lost? Keep calm and click here:https://www.google.com/maps"]
    ],

    [
        r"what (.*) like ?",
        ["There's only one thing i like. doing the wish of the customer,you know they are kings/ queens !!!!!!"]
    ],
]


def miller():
    print("Hi, I'm miller. I know you like delicious meals , i believe thats why you are here? :) \nPlease type lowercase English language to start a conversation. Type quit to leave , Am here to serve you")


chat = Chat(QA, reflections)
if __name__ == "__main__":
   miller()

chat.converse()
