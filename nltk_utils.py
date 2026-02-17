import numpy as np
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer() #make words into stem

def tokenize(sentence): #use this function for tokenization
    return nltk.word_tokenize(sentence) #with the elp of nltk
"""
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """


def stem(word): #use this word for stemming
    return stemmer.stem(word.lower()) #use of stemmer
"""
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """


def bag_of_words(tokenized_sentence, words):
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence] #stem kardo tokenized words ko
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32) #5 words hai to [0,0,0,0,0]
    for idx, w in enumerate(words): #index and words are iterated 
        if w in sentence_words: 
            bag[idx] = 1

    return bag
"""
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """




