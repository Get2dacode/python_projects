from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import json
import datetime
import wikipedia



def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')


def ok():
    talkToMe('ok here we go')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand()

    return command


def time():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talkToMe("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        talkToMe("Good Afternoon Sir !")

    else:
        talkToMe("Good Evening Sir !")


def nameMe():
    talkToMe("I am your Assistant")
    assname = "Ryker"
    talkToMe(assname)



def assistant(command):
    "if statements for executing commands"

    if 'song' in command:
        reg_ex = re.search('what is (.*)', command)
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        ok()
        webbrowser.open(url)
        print('Done!')

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain + '.com'
            ok()
            webbrowser.open(url)
            print('Done!')
        else:
            pass

    elif "what's up" in command:
        talkToMe('what it do baby')
        talkToMe('what can i help you with ')

    elif 'search' in command:
        talkToMe('Searching Wikipedia...')
        results = wikipedia.summary(command, sentences=1)
        talkToMe("According to Wikipedia")
        print(results)
        talkToMe(results)

    elif 'joke' in command:
        talkToMe('ok')
        res = requests.get(
            'https://icanhazdadjoke.com/',
            headers={"Accept": "application/json"}
        )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')


    elif "where is" in command:
        reg_ex = re.search('where is (.*)', command)
        location = reg_ex.group(1)
        ok()
        webbrowser.open(
            'https://www.google.com/maps/place/' + location + "")

    elif 'the time' in command:
        time = datetime.datetime.now().strftime("%I,%M,%p")
        talkToMe("the time is")
        talkToMe(time)

    elif 'close up'  in command:
        talkToMe("Ok make sure to shut down your computer")
        exit()


time()
nameMe()
talkToMe('I am ready for your command')

# loop to continue executing multiple commands
while True:

    assistant(myCommand())
