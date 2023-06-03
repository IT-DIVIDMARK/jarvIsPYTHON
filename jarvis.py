
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Initialize a dictionary to store user feedback
user_feedback = {}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    # Email sending code
    pass

def analyze_sentiment(text):
    # Analyze sentiment using the SentimentIntensityAnalyzer
    sentiment_scores = sia.polarity_scores(text)
    # Return the compound sentiment score
    return sentiment_scores['compound']

def handle_query(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in query:
        webbrowser.open("https://www.google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("https://www.stackoverflow.com")
    elif 'play music' in query:
        music_dir = '/path/to/music/folder'
        songs = os.listdir(music_dir)
        print(songs)
        os.system(f"xdg-open '{os.path.join(music_dir, songs[0])}'")
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    elif 'open code' in query:
        codePath = "/path/to/code/executable"
        os.system(codePath)
    elif 'email' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "youremail@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry, I am not able to send this email")

if _name_ == "_main_":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Handle the query and get the user's feedback
        handle_query(query)
        speak("Did I provide the correct information?")
        feedback = takeCommand().lower()

        # Analyze sentiment of
