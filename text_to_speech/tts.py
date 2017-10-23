# using python text to speech
import pyttsx3

#Note 
## for this to work properly install python-espeak package
## use `sudo apt-get install python-espeak` in ubuntu

engine = pyttsx3.init()
engine.say(input_text)
engine.startLoop()

## using google's text to speech package

from gtts import gTTS
print('Enter text to convert to audio...\n')
input_text = raw_input()
tts = gTTS(text=input_text, lang='en')
tts.save("audio.mp3")


## IBM watson text to speech

from tts_watson.TtsWatson import TtsWatson
 
ttsWatson = TtsWatson('watson_user', 'watson_password', 'en-US_AllisonVoice') 
ttsWatson.play("Hello kartheek")