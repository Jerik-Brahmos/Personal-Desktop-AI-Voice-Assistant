import ctypes
import random
import subprocess
import pyjokes
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import requests
import webbrowser as wb
import pywhatkit
import pyautogui
import sys
import time
import winshell as winshell
import wolframalpha as wolframalpha
from bs4 import BeautifulSoup
from pytube import YouTube
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].id)
def voice():
        engine.setProperty('voice', voices[1].id)
        print(voices[1].id)
        speak("female voice activated")
        speak("hi akash")
        speak("how r u ")
#makes jarvis to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#to make jarvis to wish
def wishtime():
    global vaname
    hour=int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("good morning")
    elif 12 <= hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    engine.runAndWait()
    vaname="FRIDAY"
    speak("hi akash")
    speak(f"IM  jarvis {vaname} , HOW CAN I HELP YOU")
    speak("how r u ")
def search(query):
    query = query.replace("search", "")
    qn = query
    wb.open(f"https://www.google.com/search?q={qn}")
#PLAY MUSIC
def music():
    speak("plaing music")
    #time.sleep(1)
    music_dir="C:\\Users\\JERIK BRAHMOS\\Music"
    songs=os.listdir(music_dir)
    rd = random.choice(songs)
    os.startfile(os.path.join(music_dir,rd))
def change_music():
    speak("changing music")
    #time.sleep(1)
    music_dir="C:\\Users\\JERIK BRAHMOS\\Music"
    songs=os.listdir(music_dir)
    rd = random.choice(songs)
    os.startfile(os.path.join(music_dir,rd))
def writenote():
    speak("What should i write")
    note = takecommand()
    file = open('le.txt', 'w')
    file.write(note)
    speak("done")
def show_note():
    speak("Showing Notes")
    file = open("leo.txt", "r")
    print(file.read())
    speak(file.read(6))
def movie():
    speak("playing a movie")
    #time.sleep(1)
    movie_dir="E:\\MOVIES"
    movies=os.listdir(movie_dir)
    rd = random.choice(movies)
    os.startfile(os.path.join(movie_dir,rd))
def location(query):
    query = query.replace("where is", "")
    query = query.replace("located", "")
    query = query.replace("locate", "")
    query = query.replace("location", "")
    location = query
    speak("User asked to Locate")
    speak(location)
    wb.open("https://www.google.com/maps/place/" + location + "")
def wiki():
    speak("what should i search on wikipedia`")
    qn = takecommand().lower()
    res = wikipedia.summary(qn, sentences=2)
    print(res)
    speak(f"According to wikipedia{res}")
def qn(query):
    qn = query.lower()
    res = wikipedia.summary(qn, sentences=1)
    engine.setProperty('rate', 150)
    print("wait for few seconds")
    print(res)
    speak(f"{res}")
def screenshot():
    speak("PLEASE TELL ME THE NAME OF THE SCREENSHOT")
    try:
        name = takecommand()
    except Exception as e:
        speak("I can't understand plaese type that")
        name = input("enter file name: ")
    speak("I'm taking screenshot")
    #time.sleep()
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    speak("screenshot is takken")
def google():
    speak("what should i search on google")
    qn = takecommand().lower()
    wb.open(f"https://www.google.com/search?q={qn}")
def youtube():
    speak("opening youtube")
    wb.open('www.youtube.com')
def play_yt(query):
    query = query.replace("youtube","")
    query = query.replace("search", "")
    query = query.replace("play", "")
    query = query.replace("on", "")
    query = query.replace("in", "")
    query = query.replace("from", "")
    speak("playing" + query)
    pywhatkit.playonyt(query)
def facebook():
    speak("opening facebook")
    wb.open('www.facebook.com')
def classroom():
    speak("opening google classroom")
    wb.open('https://classroom.google.com/u/1/')
def gmail():
    speak("opening Gmail")
    wb.open('https://mail.google.com/mail/u/1/#all')
def eduserve():
    speak("opening eduserve students portal")
    wb.open('https://studentportal.eduserve.app/home')
def docs():
    speak("opening google docs")
    wb.open('https://docs.google.com/document/u/0/?tgif=d')
# to open notepad
def notepad():
    speak("opening notepad")
    path = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2302.26.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad"
    os.startfile(path)
#to close notepad
def close_notepad():
    speak("closing notepad")
    os.system("taskkill /f /im notepad.exe")
#to close chrome
def close_chrome():
    speak("closing chrome")
    os.system("taskkill /f /im chrome.exe")
#to find ip address
def ip_address():
    ip = requests.get("https://api.ipify.org").text
    print(ip)
    speak(f"YOUR ID AdDRESS IS {ip}")
#to open cmd
def cmd():
    speak("opening command prompt")
    os.system("start cmd")
#to close cmd
def close_cmd():
    speak("closing command prompt")
    os.system("taskkill /f /im cmd.exe")
#to open pycharm
def pycharm():
    speak("opening py charm")
    path = "D:\\PyCharm Community Edition 2022.3.1\\bin\\pycharm64"
    os.startfile(path)
#closing pycharm
def close_pycharm():
    speak("closing py charm")
    os.system("taskkill /f /im pycharm64.exe")
def excel():
    speak("opening excel")
    path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL"
    os.startfile(path)
def close_excel():
    speak("closing excel")
    os.system("taskkill /f /im EXCEL.exe")
# to open powerpoint
def powerpoint():
    speak("opening powerpoint")
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint"
    os.startfile(path)
#to close powerpoint
def close_powerpoint():
    speak("closing powerpoint")
    os.system("taskkill /f /im POWERPNT.exe")
#open photoshop
def photoshop():
    speak("opening adobe photoshop")
    path = "C:\\Program Files\\Adobe\\Adobe Photoshop 2023\\Photoshop"
    os.startfile(path)
def close_photoshop():
    speak("closing photoshop")
    os.system("taskkill /f /im Photoshop.exe")
def arduino():
    speak("opening arduino UNO")
    path = "C:\\Program Files\\Arduino IDE\\ArduinoIDE"
    os.startfile(path)
def close_arduino():
    speak("closing arduino UNO")
    os.system("taskkill /f /im  ArduinoIDE.exe")
def word():
    speak("opening word")
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word"
    os.startfile(path)
def close_word():
    speak("closing word")
    os.system("taskkill /f /im WINWORD.exe")
def vlcplayer():
    speak("opening VLC media player")
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\VideoLAN\\VLC media player"
    os.startfile(path)
def close_vlcplayer():
    speak("closing VLC media player")
    os.system("taskkill /f /im  vlc.exe")
def edge():
    speak("opening microsoft edge")
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge"
    os.startfile(path)
def close_edge():
    speak("closing microsoft edge")
    os.system("taskkill /f /im msedge.exe")
def chrome():
    speak("opening chrome")
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome"
    os.startfile(path)
    speak("what should i search on chrome")
    qn = takecommand().lower()
    wb.open(f"https://www.google.com/search?q={qn}")
def close_chrome():
    speak("closing chrome")
    os.system("taskkill /f /im chrome.exe")
def joke():
    n = pyjokes.get_joke()
    print(n)
    speak(n)
def whatsapp():
    speak("opening whatsapp")
    path = "C:\\Users\\JERIK BRAHMOS\\Documents\\Desktop\\WhatsApp"
    os.startfile(path)
def close_whatsapp():
    speak("closing whatsapp")
    os.system("taskkill /f /im  whatsapp.exe")
def python():
    speak("opening python")
    path = "C:\\Users\\JERIK BRAHMOS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Python 3.9 (64-bit)"
    os.startfile(path)
def close_python():
    speak("closing python")
    os.system("taskkill /f /im python.exe")
def MicrosoftStore():
    speak("opening Microsoft Store")
    path = "C:\\Users\\JERIK BRAHMOS\\Documents\\Desktop\\Microsoft Store"
    os.startfile(path)
def close_MicrosoftStore():
    speak("closing Microsoft Store")
    os.system("taskkill /f /im WinStore.App.exe")
def timme():
    strTime = datetime.datetime.now()
    curTime = str(strTime.hour) + " hours" + " " + str(strTime.minute) + " minutes" + " " + str(
        strTime.second) + " seconds"
    print(curTime)
    speak(f" the time is {curTime}")
def telegram():
    speak("opening telegram")
    path = "C:\\Users\\JERIK BRAHMOS\\Documents\\Desktop\\Telegram Desktop"
    os.startfile(path)
def close_telegram():
    speak("closing telegram")
    os.system("taskkill /f /im Telegram.exe")
def stop():
    f = "bye sir","see you again sir"
    speak(random.choice(f))
    sys.exit()
def news():
    news = wb.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
    speak('Here are some headlines from the Times of India,Happy reading')
def leo():
    music_dir = "C:\\Users\\JERIK BRAHMOS\\Music\\leo.mp3"
    speak(" i ,am ,  friday")
    os.startfile(music_dir)

#to take input from user
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print("YOU SAID:",query)
    except Exception as e:
        print(e)
        print("unable to recognize")
        return ""
    return query.lower()
if 1 ==1:
     wishtime()
     takecommand()
     while True:
          query = takecommand().lower()
          if 'wikipedia' in query:
             wiki()
          elif 'open youtube' in query:
              youtube()
          elif 'play on youtube' in query or 'search in youtube' in query or 'search youtube' in query or 'Search youtube' in query or 'play youtube' in query or 'Play youtube' in query or 'Youtube' in query or 'youtube' in query:
              play_yt(query)
          elif 'open google' in query:
              google()
          elif 'open facebook' in query:
              facebook()
          elif 'open classroom' in query or 'open gcr' in query:
              classroom()
          elif 'open mail' in query or 'open gmail' in query or 'open email' in query:
              gmail()
          elif 'open edu serve' in query or 'open eduserve' in query or 'open students portal' in query:
              eduserve()
          elif 'open dogs' in query or 'open docs' in query or 'open google docs' in query or 'open google dogs' in query:
              docs()
          elif 'open chrome' in query:
              chrome()
          elif 'close chrome' in query:
              close_chrome()
          elif 'open notepad' in query:
              notepad()
          elif 'close notepad' in query:
              close_notepad()
          elif 'ip address' in query:
               ip_address()
          elif 'open py charm' in query or 'open pycharm' in query:
                pycharm()
          elif 'close py charm' in query or 'open pycharm' in query:
                close_pycharm()
          elif 'open excel' in query:
                excel()
          elif 'close excel' in query:
                close_excel()
          elif 'open powerpoint' in query:
                powerpoint()
          elif 'close powerpoint' in query:
                close_powerpoint()
          elif 'open photoshop' in query:
                photoshop()
          elif 'close photoshop' in query:
                close_photoshop()
          elif 'open arduino' in query or 'open arduino uno' in query:
                arduino()
          elif 'close arduino' in query or 'open arduino uno' in query:
                close_arduino()
          elif 'open word' in query:
                word()
          elif 'close word' in query:
                close_word()
          elif 'open vlc' in query or 'open vlc media player' in query:
                vlcplayer()
          elif 'close vlc' in query or 'close vlc media player' in query:
                close_vlcplayer()
          elif 'open command' in query or 'open cmd' in query or 'open comment' in query:
              cmd()
          elif 'close command ' in query or 'close cmd' in query or 'close comment' in query:
              close_cmd()
          elif 'open edge' in query:
              edge()
          elif 'close edge' in query:
              close_edge()
          elif 'open whatsapp' in query:
              whatsapp()
          elif 'close whatsapp' in query:
              close_whatsapp()
          elif 'open python' in query:
              python()
          elif 'close python' in query:
              close_python()
          elif 'open microsoft Store' in query or 'open ms store' in query or 'open store' in query:
              MicrosoftStore()
          elif 'close microsoft Store' in query or 'close ms store' in query or 'close store' in query:
              close_MicrosoftStore()
          elif 'open telegram' in query:
              telegram()
          elif 'close telegram' in query:
              close_telegram()
          elif 'play music' in query or 'play song' in query or 'play me a song' in query or 'sing me a song' in query:
               music()
          elif 'change music' in query or 'change song' in query or 'change a song' in query or 'change the song' in query or 'change the music ' in query:
                change_music()
          elif 'screenshot' in query:
               screenshot()
          elif 'quit' in query or 'bye' in query  or 'stop' in query or 'exit' in query or 'dont listen' in query:
               stop()
          elif 'play movie' in query:
               movie()
          elif 'hai' in query:
               speak("Hai !")
               speak("how are you")
               print("Hai !")
               print("how are you")
          elif "good morning" in query or "good afternoon" in query or "good evening" in query:
              speak("A very" + query)
              speak("Thank you for wishing me! Hope you are doing well!")
          elif "good night" in query:
              speak("good night")
              speak("Sweet dreams.Sleep peacefully")
          elif 'fine' in query or "good" in query:
              speak("It's good to know that your fine")
              print("It's good to know that your fine")
          elif "who are you" in query:
               speak(f"My name is {vaname} , I am your personal voice assistant")
          elif "thank you" in query:
              speak("It's my pleasure!")
          elif "how are you" in query:
              speak("I am fine, Thank you")
              speak("How are you")
          elif "hello" in query:
              speak("hello")
          elif 'time' in query:
              timme()
          elif 'joke' in query:
              joke()
          elif "my girlfriend" in query or "my boyfriend" in query:
              speak("I'm not sure about that, may be you should give me some time")
          elif "i love you" in query or "love you" in query:
              speak("Thank you! But, It's a pleasure to hear it from you.")
          elif 'search' in query:
              search(query)
          elif "restart" in query:
              subprocess.call(["shutdown", "/r"])
          elif "your name" in query:
              speak(f"my name is {vaname}")
          elif "write note" in query or "write notes" in query or "make note" in query or "take note" in query:
              writenote()
          elif "i am" in query or "am i" in query:
              speak("If you talk then definitely your human.")
          elif 'lock' in query:
              speak("locking the device")
              ctypes.windll.user32.LockWorkStation()
          elif "where is" in query or "locate" in query or "location" in query:
              location(query)
          elif "hibernate" in query or "sleep" in query:
              speak("Hibernating")
              subprocess.call("shutdown / h")
          elif "log off" in query or "sign out" in query or "shutdown" in query:
              speak("logging off")
              time.sleep(5)
              subprocess.call(["shutdown", "/l"])
          elif "show note" in query or "so note" in query or "show notes" in query or "so notes" in query:
              show_note()
          elif 'news' in query:
              news()
          elif "made you" in query or "created you" in query or "discovered you" in query:
              speak("I was built by JERIK BRAHMOS AND TEAM")
              print("I was built by JERIK BRAHMOS AND TEAM")
          elif 'you do' in query:
              speak(' I am programmed to minor tasks like , opening  youtube , google , chrome , gmail and few more , and even opening and closing some softwares , predicting time , searching in youtube , google , wikipedia , playing music , movies , geting top headline news from times of india AND FEW MORE')
          elif 'ask' in query or 'who' in query or 'what' in query or 'how' in query:
              qn(query)
          elif "change voice" in query or "voice" in query or "Voice" in query:
              voice()
          elif "change name" in query:
              speak("What would you like to call me")
              vaname = takecommand()
              speak("My name is changed")
          else:
              speak("Sorry, I am not able to understand you")