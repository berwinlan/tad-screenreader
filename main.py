from gtts import gTTS
from playsound import playsound
from bs4 import BeautifulSoup
from os.path import basename, exists
from itertools import groupby

## HELPERS ##

# From Allen Downey's FA21 DSA philosophy notebook
def download(url):
    '''
    Downloads a webpage.
    '''
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve
        local, _ = urlretrieve(url, filename)
        print('Downloaded ' + local)

def get_soup(url):
    '''
    Downloads a webpage and puts it into the BS4 format.
    '''
    download(url)
    filename = basename(url)
    fp = open(filename)
    return BeautifulSoup(fp, features="html.parser")

def speak(str):
    tts = gTTS(str, lang='en')
    tts.save('hello.mp3')
    playsound('hello.mp3')

def split_soup(soup):
    '''
    Takes soup and splits it by line, where new paragraphs are delimited by
    empty strings.
    '''
    # Get all text from DOM
    text = soup.get_text()
    # Remove tabs and split into list at newlines
    text = text.replace('\t', '').split('\n')
    # Remove consecutive duplicates (particularly spaces)
    text = [i[0] for i in groupby(text)]
    return text

## INTERACTIVE ##
def read(soup):
    '''
    This is incomplete, but this would theoretically take user key input.
    '''
    for line in split_soup(soup):
        user_input = input('Right arrow for next line, down arrow for next paragraph. ')
            
        if user_input == 'K_DOWN':    
            print(user_input)

        print(line)
        if line:
            speak(line)


def main():
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    # url = "https://stackoverflow.com/questions/12451997/beautifulsoup-gettext-from-between-p-not-picking-up-subsequent-paragraphs"
    # url = "https://softdes.olin.edu/docs/readings/0-intro-to-assignments"
    soup = get_soup(url)
    for line in split_soup(soup):
        if line:
            print(line)
            speak(line)



if __name__ == '__main__':
    main()