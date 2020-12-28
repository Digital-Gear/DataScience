import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit as pyBrain
import datetime
import wikipedia as wiki
import pyjokes as joke
import webbrowser as browse
import random
import PyDictionary as dictionary
import os


####
recogniser = sr.Recognizer()
# if many microphones, get all available devices and use "sr.Microphone(device_index=3)"
# sr.Microphone.list_microphone_names()
microphone = sr.Microphone()
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1.0)
engine.setProperty('rate', 170)


#### engine Name
wake = 'pixel'
introduction = ["I`m all ears", "I`m listening", "Do you need help", "Can I assist you", "How can I help you",
                "if you have more free time, you can ask any questions", "can I be of your service today",
                "what do you want me to do more"]
endStatement = ["sorry, I`m not mature enough to understand that. Could you repeat again", "Didnt quite understood you",
                "could you be a bit more clearer", "Come again, please", "Do you even hear yourself"]


def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('hey, How can I help you today?')


def take_command():
    try:
        with microphone as source:
            talk(introduction[random.randint(0, len(introduction) - 1)])
            recogniser.adjust_for_ambient_noise(source, duration=0.5)
            print('Waiting for Command...')
            audioIn = recogniser.listen(source)
            command = recogniser.recognize_google(audioIn)
            command = command.lower()
            command = command.replace(wake, '')
            print(command)
            return command

    except sr.RequestError:
        talk('Network error.')

    except:
        pass


def run_pixel():
    command = take_command()

    try:

        if 'play' in command:
            video = command.replace('play', '', 1)
            print(command)
            talk('playing ' + video + 'on you tube')
            pyBrain.playonyt(video)

        elif 'introduce' in command or 'are you' in command or 'your name' in command or 'who made you' in command:
            talk('I`m pixel, prashanths desktop voice assistant')

        elif 'time' in command:
            time24 = datetime.datetime.now().strftime('%H:%M')
            time12 = datetime.datetime.now().strftime('%I:%M:%p')
            talk('Current time is ' + time12)
            print('Current time is ' + time12)

        elif 'today' in command or 'date' in command:
            talk(datetime.date.today().strftime("%B %d, %Y"))
            print(datetime.date.today().strftime("%B %d, %Y"))

        elif 'hey' in command or 'you doing' in command or 'hello' in command:
            talk('hello there')

        elif 'wikipedia' in command:
            about = command.replace('wikipedia', '', 1)
            information = wiki.summary(about, 2)
            talk('Here is what i found on wikipedia.')
            talk(information)
            print(information)

        elif 'joke' in command:
            talk(joke.get_joke())

        elif 'search' in command:
            talk('Here is what i found on google.')
            command = command.replace('search', '')
            browse.open("https://www.google.com/search?q={}".format(command))

        elif wake in command:
            talk('at your assistance')

        elif 'meaning' in command or 'mean' in command:
            command = command.replace('what is the meaning of', '')
            command = command.replace('what does', '')
            command = command.replace('mean', '')
            command = command.replace('meaning', '')
            talk(dictionary.PyDictionary.meaning(command))

        elif 'synonym' in command:
            command = command.replace('what is the synonym for', '')
            command = command.replace('what are the synonym for', '')
            command = command.replace('synonym', '')
            talk(dictionary.PyDictionary.synonym(command))

        elif 'antonym' in command:
            command = command.replace('what is the antonym for', '')
            command = command.replace('what are the antonym for', '')
            command = command.replace('antonym', '')
            talk(dictionary.PyDictionary.antonym(command))

        elif 'translate' in command:
            command = command.replace('translate', '')
            command = command.json.dumps(command)
            talk(dictionary.PyDictionary.translate(command, '', 'de'))

        elif 'find location' in command or 'show me the location of' in command:
            command = command.replace('find location', '')
            url = 'https://google.nl/maps/place/' + command + '/&amp;'
            browse.get().open(url)

        elif 'you know' in command:
            talk('If my designer knows, consider i know as well')

        elif 'notepad' in command:
            talk('activating system control protocol')
            os.startfile(
                'C:\\Users\\Z0043TRS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad')

        elif 'bye' in command:
            talk('Its pleasure assisting you, adios amigo')
            exit()

        else:
            talk(endStatement[random.randint(0, len(endStatement) - 1)])
    except:
        pass

while True:
    run_pixel()