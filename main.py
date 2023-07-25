import datetime
import wikipedia
import pyttsx3
import pywhatkit
import speech_recognition as sr
import cv2
import webbrowser
import random
from PIL import ImageTk
import PIL.Image
from tkinter import *
import os

# l1 = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

# hour = int(datetime.datetime.now.hour)
# if hour >= 0 and hour < 12:
#     talk("Good morning my team")
# elif hour >= 12 and hour < 16:
#     talk('Good evening my team')
# elif hour >= 16 and hour < 18:
#     talk('Good evening my team')


def talk(text):
    engine.say(text)
    # speaker.say(speech)
    engine.runAndWait()


l1 = sr.Recognizer()


def take_cmd():
    try:
        with sr.Microphone() as source:

            print(" SPEAK NOW.......")

            voice = l1.listen(source)
            command = l1.recognize_google(voice)
            command = command.lower()

            if 'avatar' in command:
                command = command.replace('avatar', '').replace('hey', '').replace('hi', '')
                # talk(command)
                print(command)

    except Exception:
        command = ''

    return command


def run_avatar():
    command = take_cmd()
    command = command.lower()

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        exit()

    elif 'who are you' in command:
        talk('My name is avatar. I am you virtual assistant')

    elif 'open google' in command:
        talk('Opening google for you..')
        webbrowser.open('www.google.co.in')
        exit()

    elif 'open youtube' in command:
        talk('Opening youtube for you..')
        webbrowser.open('www.youtube.com')
        exit()

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'search' in command:
        search = command.replace('search', '').replace('hey', '').replace('avatar', '').replace('hi', '')
        talk('searching' + search)
        pywhatkit.search(search)
        exit()

    elif 'wikipedia' in command:
        search = command.replace('wikipedia', '').replace('search', '').replace('on', '')
        info = wikipedia.summary(search, 1)
        print('According to wikipedia' + info)
        talk(info)
        exit()

    elif 'date' and 'go' in command:
        talk('I would love to go.....')

    elif 'are you single' in command:
        talk('I am in the relationship with the internet....')

    elif 'exit' in command:
        talk('Thanks team have a good day')

    # elif 'open' and 'camera' in command:
    #     talk('Opening camera')
    #     cap=cv2.VideoCapture(0)
    #     while True:
    #         ret,img = cap.read()
    #         cv2.imshow('webcam',img)
    #         k= cv2.waitKey(10)
    #         if k==27:
    #             break;
    #     cap.release()
    #     cv2.destroyAllWindows()
    #     exit()

    else:
        talk('Please say the command again.....')


class Widget:
    def __init__(self):
        root = Tk()
        root.title('AVATAR')
        root.geometry('520x320')
        # fp = open("robot-1169742.jpg", "rb")
        # img = PIL.Image.open(fp)
        # img = ImageTk.PhotoImage(Image.open('robot-1169742.jpg'))
        # panel = Label(root, image=img)
        panel = Label(root, image='')
        panel.pack(side='right', fill='both', expand='no')
        # compText = StringVar()
        users = StringVar()
        users.set('AVTAR')
        userframe = LabelFrame(root, text='AVTAR', font=('Railways', 24,'bold'))
        userframe.pack(fill='both', expand='yes')
        top = Message(userframe, textvariable=users, bg='black',fg='white')
        top.config(font=("Century Gothic", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')
        btn = Button(root, text='Speak', font=('railways', 10, 'bold'),bg='red', fg='white', command=run_avatar)
        btn.pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10,'bold'), bg = 'yellow', fg = 'black', command = root.destroy)
        btn2.pack(fill='x', expand='no')
        talk('hello team  i am avtar how can i help you')
        root.mainloop()


if __name__ == '__main__':
    widget = Widget()


while True:
    run_avatar()

