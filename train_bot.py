# -*- coding: utf-8 -*-
import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle

#nltk.download('punkt')

words = []
classes = []
documents = []
ignore_words = ['?', '!', '.']
data_file  = open('intents.json').read()
intents = json.loads(data_file)

for intent in  intents['intents']:
    for pattern in  intent['patterns']:
        w = nltk.word_tokenize(pattern)
        print('Token is: {}'.format(w))
        words.extend(w)
        documents.append((w, intent['tag']))
    
    #Final List
    print('Words list is : {}'.format(words))
    print('documents list is : {}'.format(documents))
       
        
    