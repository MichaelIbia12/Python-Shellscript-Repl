import pyautogui
#import time

f = open('name.txt', 'r')
screen = pyautogui.size()
startButton = (10, screen.height - 10)
response_num = 0
Botname = "boxDroid"

pyautogui.PAUSE = 1.25
response = [
    "hi",
    "how are you",
    "my name is " + Botname,
    "what is your name ?"
]
positive_reponses = [
    "yes"
    "okay"
    "fine"
    "you too"
]
class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""

def array_string(letterend, letterstart, text):
    main_str = ""
    while letterstart != letterend:
        main_str += text[letterstart]
        letterstart += 1

    return main_str


def msg_filter(msg, filter1, filter2,):
    filter_one = msg.replace(filter1, " ")
    filter_two = filter_one.replace(filter2, "")
    return filter_two


def keyWord_finder(keyword, text, space):
    return text.index(keyword) + space



def talkBack():
    msg = pyautogui.prompt(response[response_num-1],"Response")
    if response[response_num-1].find("name"):
        filter_text = msg_filter(msg, "is", " ")
        letterstarter = keyWord_finder("me", filter_text, 2)
        Person().name = array_string(len(filter_text), letterstarter, filter_text)
        print(Person().name)
        response.append("Nice to meet you " + Person().name)

    for r in positive_reponses:
        if r in msg:
            response.append("😊")



#pyautogui.moveTo(startButton)
#pyautogui.rightClick()
#pyautogui.typewrite("NotePad")
#pyautogui.press("Enter")
#time.sleep(5)
pyautogui.countdown(5)
while True:
    pyautogui.typewrite(response[response_num], interval=0.15)
    pyautogui.press("Enter")
    response_num += 1
    print(response_num)
    if response_num > len(response) - 1:
        talkBack()
