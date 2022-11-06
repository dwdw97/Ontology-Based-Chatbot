import speech_recognition as sr
from gtts import gTTS
import os

r = sr.Recognizer()

with sr.Microphone() as source:
	print("Say anything: ")
	audio = r.listen(source)

	try:
		text = r.recognize_google(audio, language="id").lower()
		# text = r.recognize_google_cloud(audio,)
		print('You said: ', text)
		if(text == "selamat pagi"):
			response = "selamat pagi juga"
		elif(text == "apa kabar"):
			response = "Kabar baik mas Dicky"
		else:
			response = "Maaf, saya tidak dapat memahami ucapan anda"
	except:
		print("Sorry, could not recognize your saying")
		response = "Maaf, saya tidak dapat memahami ucapan anda"
	
	myobj = gTTS(text=response, lang='id', slow=False)
	myobj.save("response.mp3")
	os.system("start response.mp3")