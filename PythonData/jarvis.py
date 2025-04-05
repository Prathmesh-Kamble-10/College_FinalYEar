import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait() 


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!");

    elif hour>=12 and hour<18: 
         speak("Good Afternoon!");

    else:
        speak("Good Evening!");

    speak("Hi I am Your Assistant sir. How can I help you");

def takeCommand():
# this is for recongnition of your microphone and they answer your question its take input from microphone in Simple word
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listining...")
        r.pause_threshold = 1
        audio = r.listen(source)    

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")  
        
    except Exception as e:
        #print(e)
        print("Say that again please")
        return "None"
    return query

if __name__ == "__main__": 
        wishMe()    
         #while True:   
        if 1:

            query = takeCommand().lower()
                #logic and executing task for
                
            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)  

            elif 'open youtube' in query:
                webbrowser.open("www.youtube.com")  

            elif 'open netflix' in query:
                webbrowser.open("www.netflix.com")  

            elif 'play music' in query:
                music_dir = 'E:\\Music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0])) 

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir, the Time is{strTime}") 

            elif 'open code' in query:  
                codePath = "C:\\Users\\kprat\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)