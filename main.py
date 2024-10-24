import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import openai
from gtts import gTTS
import pygame
import os



recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="NEWS_API KEY"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
    tts=gTTS(text)
    tts.save('temp.mp3')
    # Initialize Pygame mixer
    pygame.mixer.init()
    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')
    # Play the MP3 file
    pygame.mixer.music.play()
    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        
    pygame.mixer.music.unload()
    os.remove("temp.mp3")


# Set your OpenAI API key
openai.api_key = "open AI API key"

def aiProcess(command):
    # Set your OpenAI API key
    openai.api_key = "openai API key"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Ensure you are using a valid model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": command},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return "I encountered an error processing your request."


    return completion.choices[0].message.content
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/everything?q=Apple&from=2024-10-23&sortBy=popularity&apiKey={newsapi}")
        if r.status_code==200:
            # parse the json response
            data=r.json()
            # extract the articles
            articles=data.get('articles',[])
            # print the headlines
            for article in articles:
                speak(article['title'])
    else:
        # let openAI handle the requests
        output=aiProcess(c)
        speak(output)
        
        
        
if __name__=="__main__":
    speak("Initializing jarvis......")
    while True:
    # listen for wake word "jarvis"
    # obtain audio from the microphone
      r=sr.Recognizer()
         
    # recognize speech using sphinx
      print("recognizing...")
      try:
          with sr.Microphone() as source:
             print("listening...")
             audio=r.listen(source,timeout=2,phrase_time_limit=1)
          word=r.recognize_google(audio)
          if(word.lower()=="jarvis"):
              speak("Ya")
              # Listen for command
              with sr.Microphone() as source:
                print("jarvis active...")
                audio=r.listen(source)
                command=r.recognize_google(audio)
                
                processCommand(command)
      except Exception as e:
        print("error; {0}".format(e))
        
