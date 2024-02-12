import cowsay
import wikipedia

def random_article():
    random_wiki = wikipedia.random(pages=1)
    random_summary = wikipedia.summary(random_wiki, sentences = 10, chars = 0, auto_uggest = True, redirect = True)
    print(cowsay.cow(str(random_summary)))

random_article()
