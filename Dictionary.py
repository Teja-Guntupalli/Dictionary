import json
from difflib import get_close_matches
from gtts import gTTS
import os
import time
data = json.load(open("data.json"))
def speak(t,s):
    language = 'en'
    myobj = gTTS(text=t, lang=language, slow=False)
    myobj.save("speak{}.mp3".format(s))
    os.system("speak{}.mp3".format(s))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y" or yn=="y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N" or yn=="n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
text=[]
output = translate(word)
if type(output) == list:
    for item in output:
        text.append(item)
        print(item)
else:
    text.append(output)
    print(output)
for i in range(len(text)):
    speak(text[i],i)
