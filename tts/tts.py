import tempfile
from subprocess import call
from gtts import gTTS

def say(text):
	google(text)

def google(text):
	text = "\"" + text + "\""
	tts = gTTS(text)
	file = tempfile.NamedTemporaryFile()
	tts.write_to_fp(file)
	play(file)
	file.close()

def play(file):
        cmd = 'cvlc --play-and-exit --alsa-audio-device=default --quiet ' + file.name + ' 2> /dev/null'
        call([cmd], shell=True)
