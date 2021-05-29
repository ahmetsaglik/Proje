import warnings
warnings.filterwarnings("ignore")
import nltk
from nltk.stem.lancaster import LancasterStemmer
from io import open
import numpy as np
import tflearn
import tensorflow
import json
import pickle
import os


class Model():
    def getModel(training, output):
        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)
        model = tflearn.DNN(net)

        return model   

stemmer = LancasterStemmer()

with open("D:/PROGRAMLAMA/bitirmeV2/Engine/yemekOnerisi/yemekDatalari/yemek.json",encoding="UTF-8") as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []

for intent in data["yemekler"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []
out_empty = [0 for _ in range(len(labels))]

for x,doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

training = np.array(training)
output = np.array(output)

with open("D:/PROGRAMLAMA/bitirmeV2/Engine/yemekOnerisi/yemekDatalari/yemekData.pickle","wb") as f:
   pickle.dump((words, labels, training, output), f)


model = Model.getModel(training,output)
model.fit(training, output, n_epoch=500, batch_size=8, show_metric=True)
model.save("D:/PROGRAMLAMA/bitirmeV2/Engine/yemekOnerisi/yemekDatalari/yemekOneriModel.tflearn") 
