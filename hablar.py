from gtts import gTTS
import os
from playsound import playsound

texto = "Creo que seria todo por hoy, nos vemos la proxima seman, aprovechen de explorar el documento algoritmos que tiene las siguientes instrucciones a estudiar"
tts = gTTS(text = texto, lang='es', tld='com.mx')
tts.save('tecsify.mp3')
playsound('tecsify.mp3')