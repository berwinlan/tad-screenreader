from gtts import gTTS
from playsound import playsound
from bs4 import BeautifulSoup
from os.path import basename, exists

# From Allen Downey's FA21 DSA philosophy notebook
def download(url):
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve
        local, _ = urlretrieve(url, filename)
        print('Downloaded ' + local)

def get_soup(url):
    download(url)
    filename = basename(url)
    fp = open(filename)
    return BeautifulSoup(fp, features="html.parser")

def speak():
    tts = gTTS('Hello world!', lang='en')
    tts.save('hello.mp3')
    playsound('hello.mp3')

def main():
    # url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    # url = "https://stackoverflow.com/questions/12451997/beautifulsoup-gettext-from-between-p-not-picking-up-subsequent-paragraphs"
    url = "https://softdes.olin.edu/docs/readings/0-intro-to-assignments"
    # url = "https://stackabuse.com/guide-to-parsing-html-with-beautifulsoup-in-python/"
    soup = get_soup(url)
    # all_titles = soup.find_all("title")
    text = soup.get_text()
    text.split('\n')
    print(text)


if __name__ == '__main__':
    main()