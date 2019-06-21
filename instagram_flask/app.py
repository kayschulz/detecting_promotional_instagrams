import random
import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import h5py
from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from keras.models import load_model
from nltk import word_tokenize
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing import sequence
import pickle

import os
os.environ['KERAS_BACKEND'] = 'theano'
import keras as ks

model = tf.keras.models.load_model("app_model.h5")
tokenizer = pickle.load(open('tokenizer.pkl', 'rb'))
app = Flask(__name__, static_url_path="")
graph = tf.get_default_graph()

def get_model():
    global model
    model = tf.keras.models.load_model("app_model.h5")
    
@app.route('/')
def index():
    """Return the main page."""
    return render_template('index.html')

# vectorizes and tokenizes the input

def tokenize_input(user_input):
    """Converts input text to word vectors for model"""
    words = word_tokenize(user_input)
    list_tokenized = tokenizer.texts_to_sequences(words)
    X_t = sequence.pad_sequences(list_tokenized, maxlen=100)
    return X_t

get_model()

@app.route('/predict', methods=['POST'])
def predict():
    """Return a random prediction."""
    data = request.get_json(force=True)
    X_t = tokenize_input(data['user_input'])
    prediction = model.predict(X_t).to_list()
    response = {'probability not promo': prediction[0][0].round(4),
                'probability_promo': prediction[0][1].round(4)}
    return jsonify(response)
    