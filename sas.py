import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from collections import defaultdict
import pprint
from nltk.tag import pos_tag
import re
text = """there is a issue in the network
change calendar is not getting created
due to dependency on the system and
many issues are dependent on this"""
# word_tokens = word_tokenize(text)



def text_synonym_antonym(text: str):
    word_tokens = word_tokenize(text)
    tags = pos_tag(word_tokens)
    # named_entities = ne_chunk(tags)

    # print("Named Entities:",tags)


    nouns = [word for (word,tag) in tags if tag == "NN"]
    print(nouns)

    synonyms = defaultdict(list)
    antonyms = defaultdict(list)
    for token in nouns:
        for syn in wordnet.synsets(token):
            for i in syn.lemmas():
                synonyms[token].append(i.name())
                if i.antonyms():
                    antonyms[token].append(i.antonyms()[0].name())
    pprint.pprint(dict(synonyms))
    pprint.pprint(dict(synonyms))
    synonym_output = pprint.pformat((dict(synonyms)))
    antonyms_output = pprint.pformat((dict(antonyms)))
    with open(str(text[:5]) + ".txt", "a") as f:
        f.write("Starting of Synonyms of the Words from the Sentences: " + synonym_output + "\n")
        f.write("Starting of Antonyms of the Words from the Sentences: " + antonyms_output + "\n")
        f.close()

text_synonym_antonym(text)
