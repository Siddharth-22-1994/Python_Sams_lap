from gtts import gTTs
import os

msg = 'You have been hacked'
language = 'en'

obj = gTTS(txt=msg, lang=language, slow=False)

obj.save('Virus.mp4')

for val in range(5):
    obj.system('mpg321 Virus.mp4')
