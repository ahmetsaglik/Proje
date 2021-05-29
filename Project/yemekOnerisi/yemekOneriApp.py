import warnings
warnings.filterwarnings("ignore")
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from io import open
import random
import json
import pickle
import numpy as np
import tflearn
import tensorflow

class Model():
    def getModel(training, output):
        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)
        model = tflearn.DNN(net)

        return model    



with open("/home/admin/Project/yemekOnerisi/yemekDatalari/yemek.json",encoding="UTF-8") as file:
    data = json.load(file)

with open("/home/admin/Project/yemekOnerisi/yemekDatalari/yemekData.pickle","rb") as file:
    words, labels, training, output = pickle.load(file)

yemekModel = Model.getModel(training, output)
yemekModel.load("/home/admin/Project/yemekOnerisi/yemekDatalari/yemekOneriModel.tflearn")




def bagOfWords(sent, words):
    bag = [0 for _ in range(len(words))]

    sWords = nltk.word_tokenize(sent)
    sWords = [stemmer.stem(word.lower()) for word in sWords]

    for se in sWords:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)

def oneriYap(inp):

    results = yemekModel.predict([bagOfWords(inp, words)])
    resultsIndex = np.argmax(results)
    tag = labels[resultsIndex]

    for tg in data["yemekler"]:
        if tg["tag"] == tag:
            responses = tg["responses"]
    resp = random.choice(responses)
    return resp

