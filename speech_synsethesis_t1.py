# import lib gTTS de tao giong noi va os de thao tac file
from gtts import gTTS
import os

# mo file .txt de doc du lieu
with open('/home/cooking/Documents/Python/Speech_recog/speech_synsethesis_sample.txt') as speech_text:
	content = speech_text.read() # luu text vao content
	speech_text.close() # dong file

def speech_synthesis(text, lang, remove): # tao mot ham nhan 3 tham so
	tts = gTTS(text = text, lang = lang, slow = False) # goi lenh gtts 
	tts.save("gtts0.mp3") # luu vao file .mp3
	os.system("mpg321 gtts0.mp3") # chay file .mp3
	if remove == True: # xoa neu can thiet
		os.remove("gtts0.mp3")

speech_synthesis(content, 'en', False) # goi ham