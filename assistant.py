import speech_recognition as sr
import datetime
import wikipedia
import requests
import playsound
from gtts import gTTS
import os
import wolframalpha
from selenium import webdriver
from ecapture import ecapture as ec
import subprocess
import time
import pyjokes
import imdb
import pywhatkit as kit
import requests
from bs4 import BeautifulSoup as soup
import re
import webbrowser
import downloader



#taking commands function
def talk():
    input = sr.Recognizer()
    #mic input
    with sr.Microphone() as source:
        input.adjust_for_ambient_noise(source)
        audio = input.listen(source)
        data = ""
        #converting input to text
        try:
            data = input.recognize_google(audio)
            print("Your question is, " + data)
        except sr.UnknownValueError:
            print("Sorry I did not hear your question, Please repeat again")
        return data


#function for getting response from assistant
def respond(output):
    num = 0
    print(output)
    num += 1
    response = gTTS(text = output, lang = 'en')
    file = str(num) + '.mp3'
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)

#Download movie function
def Download(input):
    downloader.Search(input)
    respond("Say the number of movie you want to download or back if you want to repeat command")
    #text = talk().lower()
    #if "back" in text:
    #    return
    #downloader.Links(text)
    #respond("Choose the quality of video by saying which one you want")

    #downloader.Download(text)


def find_movie(text):
    movies = imdb.IMDb()
    respond("Searching for " + text)
    movies_search = movies.search_movie(text)

    if len(movies_search) == 0:
        respond("No results found")
    else:
        respond('I found these')

        for movie in movies_search:
            #title = movie['title']
            #year = movie['year']
            #respond(f'{title} released in {year}')


            info = movie.getID()
            movie = movies.get_movie(info)

            title = movie['title']
            #year = movie['year']
            rating = movie['rating']
            plot = movie['plot'][0]
            genres = movie['genres']

            respond(f'{title} has IMDB rating of {rating}.\
                Movie is consider to be in category of following genres: {genres}.\
                The plot of the movie is {plot}')
            respond("Should I continue or stop? Say stop to stop reading movie list, say continue to continue")
            text = talk().lower()

            if 'continue' in text:
                continue
            else:
                return


if __name__=='__main__':
    respond("Hi, I am your personal desktop assistant")

    while(1):

        respond("How can I help you?")
        text=talk().lower()

        if text==0:
            continue

        if "stop" in str(text) or "exit" in str(text) or "bye" in str(text):
            respond("Ok bye and take care")
            break

        if 'download' in text:
            text = ' '.join(text.split()[1:])
            Download(text)

        if 'play' in text:
            text = ' '.join(text.split()[1:])
            respond('playing {}'.format(text))
            kit.playonyt(text, True)

        if 'movie' in text:
            text = ' '.join(text.split()[1:])
            find_movie(text)

        if 'wikipedia' in text:
            respond('Searching Wikipedia')
            text =text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=3)
            respond("According to Wikipedia")
            print(results)
            respond(results)

        elif "camera" in text or "take a photo" in text:
            ec.capture(0,"robo camera","img.jpg")

        elif 'joke' in text:
            respond(pyjokes.get_joke())

        elif 'search' in text:
            text = ' '.join(text.split()[1:])
            kit.search(text)

        elif 'time' in text:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"the time is {strTime}")

        elif 'search'  in text:
            text = text.replace("search", "")
            webbrowser.open_new_tab(text)
            time.sleep(3)

        elif 'who are you' in text or 'what can you do' in text:
            respond('I am your personal desktop assistant.')

        elif 'open gmail' in text:
            webbrowser.open_new_tab("https://www.gmail.com")
            respond("Gmail is open")
            time.sleep(3)

        elif "who made you" in text or "who created you" in text or "who discovered you" in text:
            respond("I was built by Marko")
            print("I was built by Marko")

        elif "shut down" in text:
            respond("Ok , your system will shut down in 10 secs")
            subprocess.call(["shutdown", "/l"])