
import nltk

# NOISE REMOVAL
# 1. Noise removal in a sample text
noise_list=['is', 'this', 'a', '...']

def _remove_noise(input_text):
    words=input_text.split()
    noise_free_words=[word for word in words if word not in noise_list]
    noise_free_text=" ".join(noise_free_words)
    return noise_free_text

print(_remove_noise("this is a sample text"))


# 2. Noise removal using regex
import re
def _remove_regex(input_text, regex_pattern):
    urls=re.finditer(regex_pattern, input_text)
    for i in urls:
        input_text=re.sub(i.group().strip(), '', input_text)
    return input_text

regex_pattern="#[\w]*"

print(_remove_regex("remove this #hashtag from this line", regex_pattern))


# LEXICON NORMALIZATION
# Find the lemma for a word
from nltk.stem.wordnet import WordNetLemmatizer
lem=WordNetLemmatizer()

# Stem unnecessary suffixes
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

word="multiplying"

lem.lemmatize(word, "v")
ps.stem(word)


# OBJECT STANDARDIZATION
lookup_dict={'rt':'Retweet', 'dm':'direct message', 'awsm':'awesome', 'luv':'love'}

def _lookup_words(input_text):
    words=input_text.split()
    new_words=[]
    for wor in words:
        if wor.lower() in lookup_dict:
            wor=lookup_dict[wor.lower()]
        new_words.append(wor)
    new_text=" ".join(new_words)
    return new_text

print(_lookup_words("RT this is a retweeted tweet followed by dm by Edwin"))
