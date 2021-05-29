import warnings
warnings.filterwarnings("ignore")
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from io import open
import numpy as np
import tflearn
import tensorflow
import random
import json
import pickle
import os
from model import Model
import webbrowser


with open("./data/intents.json",encoding="UTF-8") as file:
    data = json.load(file)
    
with open("./data/data.pickle","rb") as f:
    words, labels, training, output = pickle.load(f)


graph1 = tensorflow.Graph()
with graph1.as_default():
    model = Model.getModel(training, output)
    model.load("./data/chatbotModel.tflearn")

def bagOfWords(sent, words):
    bag = [0 for _ in range(len(words))]

    sWords = nltk.word_tokenize(sent)
    sWords = [stemmer.stem(word.lower()) for word in sWords]

    for se in sWords:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)

def getResponse(inp):
    results = model.predict([bagOfWords(inp, words)])
    resultsIndex = np.argmax(results)
    tag = labels[resultsIndex]
    print(tag)
    for tg in data["intents"]:
        if tg["tag"] == tag:
            responses = tg["responses"]
    resp = random.choice(responses)

    ret = tag + "&" + resp
    return ret

