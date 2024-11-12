import os
import nltk
import requests
from bs4 import BeautifulSoup
import tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
api_url = "https://en.wikipedia.org/wiki/Cloudflare"
response = requests.get(api_url)
soup = BeautifulSoup(response.text)
# tokens = tokenize.generate_tokens(soup.get_text())
# print(response.text)
# print(soup.get_text())
text = "Natural language processing (NLP) is a field of computer science, artificial intelligence and computational linguistics concerned with the interactions between computers and human (natural) languages, and, in particular, concerned with programming computers to fruitfully process large natural language corpora. Challenges in natural language processing frequently involve natural language understanding, natural language generation (frequently from formal, machine-readable logical forms), connecting language and machine perception, managing human-computer dialog systems, or some combination thereof."
print(sent_tokenize(text))
print(word_tokenize(text))

try:
    version_file = os.path.join(os.path.dirname(__file__),"VERSION")
    with open(version_file) as infile:
        __version__ = infile.read().strip()
except NameError:
    __version__ = "unknown (running code interactively?)"
except OSError as ex:
    __version__ = "unknown (%s)" % ex

print(__version__)
if __doc__ is not None:
    __doc__ += "\n@version: " + __version__