import speech_recognition as sr
from gtts import gTTS
import os
import threading
import time
import pyglet
import winsound
import playsound

def backgroundListening():
	responded = True
	while True:
		if(responded):
			winsound.PlaySound("input_ok2.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
		responded = False
		text = ""
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Say anything: ")
			audio = r.listen(source)

			try:
				text = r.recognize_google(audio, language="id").lower()
				print('You said: ', text)
				if(text == "halo" or text == "hello"):
					response = "halo, ada yang bisa saya bantu?"
				elif(text == "selamat pagi" or text == "pagi"):
					response = "selamat pagi juga"
				elif(text == "selamat malam" or text == "malam"):
					response = "ini masih pagi"
				elif(text == "apa kabar"):
					response = "Kabar baik mas Dicky"
				elif(text == "nggak ada"):
					response = "sombong kamu ya"
				elif(text == "banyak"):
					response = "maaf saya sibuk, nggak bisa bantu dulu"
				else:
					text = ""
					# response = "Maaf, saya tidak dapat memahami ucapan anda"
			except:
				print("Sorry, could not recognize your saying")
				# response = "Maaf, saya tidak dapat memahami ucapan anda"
			
		if(text!=""):
			getResponse(response)
			responded = True
			# threading.Thread(target=getResponse(response)).start()
			# for a in range(3): 
			# 	print(a)
			# 	time.sleep(1)

def getResponse(response):
	tts = gTTS(text=response, lang='id', slow=False)
	tts.save("response.mp3") # can only create mp3 file
	
	playsound.playsound("response.mp3") # can read mp3 but can't read wav. Also it can't stop a sound mid-way
	# time.sleep(2)
	try:
		os.remove("response.mp3")
	except FileNotFoundError:
		pass

	# os.system("start response.mp3")

	# pyglet.lib.load_library('avbin64')
	# pyglet.have_avbin=True
	# song = pyglet.media.load('response.mp3')
	# song.play()
	# pyglet.app.run()
	
	# winsound.PlaySound("response.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
	# winsound can read wav but can't read mp3. It can stop a sound mid-way

threading.Thread(target=backgroundListening).start()
# a = 0
# while True:
# 	print(a)
# 	a+=1
# 	time.sleep(0.1)