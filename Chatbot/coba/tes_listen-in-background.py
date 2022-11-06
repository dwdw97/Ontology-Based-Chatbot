import time
import speech_recognition as sr
from gtts import gTTS
import os

def callback(recognizer, audio):
    global r
    text = ""
    try:
        audio = sr.Recognizer().listen(sr.Microphone(), phrase_time_limit=2)
        text = recognizer.recognize_google(audio, language="id").lower()
        print('You said: ', text)
        if(text == "selamat pagi"):
            response = "selamat pagi juga"
        elif(text == "apa kabar"):
            response = "Kabar baik mas Dicky"
        else:
            response = "Maaf, saya tidak dapat memahami ucapan anda"
    except:
        # pass
        print("Maaf, tidak dapat memahami ucapan anda")
        response = "Maaf, saya tidak dapat memahami ucapan anda"
    # except sr.UnknownValueError:
    #     print("Google Speech Recognition could not understand audio")
    #     response = "Google Speech Recognition could not understand audio"
    # except sr.RequestError as e:
    #     response = "Could not request results from Google Speech Recognition service; {0}".format(e)

    if(text!=""):
        myobj = gTTS(text=response, lang='id', slow=False)
        myobj.save("response.mp3")
        os.system("start response.mp3")

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)

for a in range(100):
    print(a)
    time.sleep(0.1)

for a in range(100):
    print(a)
    time.sleep(0.1)