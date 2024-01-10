import pyttsx3 
import speech_recognition as sr 
import datetime as dt
import wikipedia
import webbrowser
import os
import smtplib
import random as r2
import sys
import wolframalpha
import googlesearch
import sqlite3 as sq
from threading import *
from tkinter import *
import datetime


win=Tk()
win.title('Friday')
win.geometry('380x585')
win.config(background="black")
conn = sq.connect('dat.db')
cursor=conn.cursor()
usertext=StringVar()
comtext=StringVar()

def new_GUI():
    root = Tk()
    root.geometry('490x473')
    root.title('Commands List')
    cmds="""                 

    1) Search Google keyword
        example: search google python or search google Friday assistant
                
    2)Wikipedia
        example:

    3) Open Youtube-> To open youtube on browser

    4)Go Offline/Nothing/Bye-> To close Application

    5)Shutdown-> To shutdown the Operating System

    6)Open Code-> To open Microsoft Visual Code

    7)Open C Drive-> To Open C Drive   

    8)Open D drive-> To Open D Drive 

    """
    hpframe=LabelFrame(
        root,
        text="Commands:- ",
        font=('Black ops one',18,'bold'),
        highlightthickness=3)
    hpframe.pack(fill='both',expand='yes')

    hpmsg=Message(
        hpframe,
        text=cmds,
        bg='black',
        fg='White'
        )
    hpmsg.config(font=('Comic Sans MS',18,'bold'),justify="LEFT")
    hpmsg.pack(fill='both',expand='no')
    exitbtn = Button(
        root, 
        text='EXIT', 
        font=('#7adb1e', 18, 'bold'), 
        bg='Green', 
        fg='white',
        borderwidth=5,
        command=root.destroy).pack(fill='x', expand='no')
    root.mainloop()
compframe=LabelFrame(
    win,
    text="Friday ",
    font=('Lucida',18,'bold'),
    highlightthickness=2)
compframe.pack(fill='both',expand='yes')
left2=Message(
    compframe,
    textvariable=comtext,
    bg='Black',
    fg='White',
    justify='left'
    )
left2.config(font=('Lucida',18,'bold'),aspect=250)
left2.pack(fill='both',expand='yes')
userframe=LabelFrame(
    win,
    text="Mr. Amitesh",
    font=('Lucida',18,'bold'),
    highlightthickness=2,)    
userframe.pack(fill='both',expand='yes')
left1=Message(
    userframe,
    textvariable=usertext,
    bg='black',
    fg='White',
    justify='left'
    )
left1.config(font=('Lucida',18,'bold'),aspect=250)
left1.pack(fill='both',expand='yes')
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('R2K75H-7ELALHR35X')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

comtext.set("""Hello! I am your Personal Assistant Friday
Click on Start button to give your Commands"""
)
usertext.set(' ')
def printo(shan):
    global comtext
    comtext.set(shan) 

def speak(audio):
    printo(audio+"\n")
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!" +name)

    elif hour>=12 and hour<18:
        speak("Good Afternoon!" +name)   

    else:
        speak("Good Evening!" +name)
        
    speak("""Hello {} 
How can I help you?""".format(name))

def Name():    
    global r,source,audio,query,name
    name=" "
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What is your name")
        printo("Please tell me Your name?\n")
        printo("Listening...\n")   
        audio = r.listen(source)

    try:
        printo("Recognizing...\n")    
        name = r.recognize_google(audio, language='en-in')       

    except Exception as e:
        printo(e)    
        printo("Again please...\n") 
        speak("Again please...")
        Name() 
        return None
    return name
    wishMe()

def Commands():
    global r,source,audio,query,usertext
    r = sr.Recognizer()
    r.energy_threshold=5000
    with sr.Microphone() as source:
        printo("Listening...\n")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Mr. Amitesh: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def srch_google():
    printo("Seaching on Google.....\n")
    #audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        keywords=(text.split(" "))
        printo(keywords)
        del keywords[0]
        del keywords[0]
        printo(keywords)
        
        def listosrting(s):
            str1=" "
            new=str1.join(s)
            return new
        printo(listosrting(keywords))
        keyword=listosrting(keywords)
        printo("You said : {}\n".format(keyword))
        url='https://www.google.co.in/search?q='
        search_url=f'https://www.google.co.in/search?q='+keyword
        speak('searching on google' +" "+ keyword)
        webbrowser.open(search_url)
    except:
        printo("Can't recognize\n")

def search_yt():
    print("searching on youtube.....\n")
    try:
        text=r.recognize_google(audio)
        key=(text.split(" "))
        del key[0]
        del key[0]
        
        def lis(s):
            str1=" "
            new=str1.join(s)
            return new    
        key=lis(key)

        print("You said : {}".format(key))
        url='http://www.youtube.com/results?search_query='
        search_url=f'http://www.youtube.com/results?search_query='+key
        speak('searching on youtube' +" "+ key)
        webbrowser.open(search_url)
    except:
        print("Can't recognize")  

def mainfn():
    global query
    if __name__ == "__main__":
        Name()
        wishMe()
    
def reco():   
    query = Commands().lower()
    
    if 'search google' in query:
        srch_google()

    elif 'search youtube' in query:
            search_yt()

    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=5)
        speak("According to Wikipedia")
        printo(results+"\n")
        speak(results)

    elif 'google' in query:
        speak('Searching Google...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=5)
        speak("According to Google")
        printo(results+"\n")
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        speak('opening google')
        webbrowser.open("google.com")

    elif 'go offline' in query:
        speak('ok '+name)
        quit()
        win.destroy()

    elif 'shutdown' in query:
        speak('okay')
        os.system('shutdown -s')


    elif "what\'s up" in query or 'how are you' in query:
        stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
        speak(r2.choice(stMsgs))
        
    elif 'play music' in query or "play song" in query:   
            music_dir='C:\\Users\Amitesh chaudhary\Music\£иglîsн Sопg'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[12]))

    elif 'play video' in query:   
            video_dir='C:\\Users\Amitesh chaudhary\Videos\Movies'
            videos=os.listdir(video_dir)
            print(videos)
            os.startfile(os.path.join(video_dir, videos[3]))
            speak('Okay, here is your video! Enjoy!')

    elif 'open code' in query:
        codePath = "C:\\Users\\abhi7\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
            
    elif 'open c drive' in query:
        cdrive = "C:"
        os.startfile(cdrive)

    elif 'what is the time' in query or "time" in query:   
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the is {strTime}") 

    elif 'ask' in query:
            speak('You can ask me any geographical questions and what question do you want to ask now')
            question=Commands()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

    elif 'nothing' in query or 'abort' in query or 'stop' in query:
        speak('okay')
        speak('Bye'+name+', have a good day.')
        sys.exit()
        win.destroy()
           
    elif 'hello' in query:
        speak('Hello'+name)

    elif 'bye' in query:
        speak('Bye'+name+', have a good day.')
        sys.exit()
        win.destroy()
       
    else:
        query = query
        try:
            speak('Searching in API...')
            res = client.query(query)
            results = next(res.results).text
            speak('WOLFRAM-ALPHA API says - ')
            speak('please wait.')
            speak(results)
                
        except Exception as e:
                #print(e)
            speak("sorry sir. i can't recognize your command maybe google can handle this should i open google for you?")
            ans=Commands()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                webbrowser.open('www.google.com')
            elif 'no' in str(ans) or 'nah' in str(ans):
                speak("ok disconnecting")
                sys.exit()
            else:
                speak("no respnse i am disconnecting")
                sys.exit()

def exit():
    win.destroy()
    sys.exit()

def start():
    Thread(target=mainfn).start()

def speakingbtn():
    Thread(target=reco).start()

btn = Button(
    win, 
    text='Start!', 
    font=('#7adb1e', 18, 'bold'), 
    bg='black', 
    fg='#7adb1e',
    borderwidth=5,
    command=start).pack(fill='x', expand='no')
btn1 = Button(
    win, 
    text='Start Speaking!', 
    font=('#7adb1e', 18, 'bold'), 
    bg='black', fg='#7adb1e',
    borderwidth=5,
    command=speakingbtn).pack(fill='x', expand='no')
btn2 = Button(
    win, text='Command List', 
    font=('#7adb1e', 18, 'bold'), 
    bg='black', fg='#7adb1e',
    borderwidth=5,
    command=new_GUI).pack(fill='x', expand='no')
btn3 = Button(
    win, 
    text='EXIT', 
    font=('#7adb1e', 18, 'bold'), 
    bg='Red', 
    fg='white',
    borderwidth=5,
    command=exit).pack(fill='x', expand='no')

win.mainloop()