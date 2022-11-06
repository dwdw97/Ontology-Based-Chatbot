import speech_recognition as sr
from gtts import gTTS
import os

r = sr.Recognizer()

with sr.Microphone() as source:
	print("Say anything: ")
	audio = r.listen(source)

	try:
		text = r.recognize_google(audio, language="id")
		print('You said: ', text)
		if(text == "Selamat pagi"):
			mytext = "Selamat pagi juga"
		elif(text == "apa kabar"):
			mytext = "Kabar baik mas Dicky"
		
		myobj = gTTS(text=mytext, lang='id', slow=False)
		myobj.save("response.mp3")
		os.system("start response.mp3")
	except:
		print("Sorry, could not recognize your saying")

