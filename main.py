from gtts import gTTS
from playsound import playsound
from bs4 import BeautifulSoup

def main():
    tts = gTTS('Hello world!', lang='en')
    tts.save('hello.mp3')
    playsound('hello.mp3')

if __name__ == '__main__':
    main()