import random
import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import h5py
from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from nltk import word_tokenize
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing import sequence
import pickle
import tensorflow as tf

import os
#os.environ['KERAS_BACKEND'] = 'theano'
import keras as ks

# model = load_model("instagram_flask/final_model.hdf5")
tokenizer = pickle.load(open('instagram_flask/tokenizer.pkl', 'rb'))
app = Flask(__name__, static_url_path="")
#graph = tf.keras.get_default_graph()

def get_model():
    global model
    model = load_model("instagram_flask/final_model.hdf5")
    
@app.route('/')
def index():
    """Return the main page."""
    return render_template('index.html')

# vectorizes and tokenizes the input

def tokenize_input(user_input):
    """Vectorize and tokenize input"""
    list_tokenized = tokenizer.texts_to_sequences(user_input.map(word_tokenize).values)
    X_t = sequence.pad_sequences(list_tokenized, maxlen=100)
    return X_t

get_model()

@app.route('/predict', methods=['GET','POST'])
def predict():
    """Return a random prediction."""
    data = request.get_json(force=True)
    user_input = pd.Series(data, name='comment')
    X_t = tokenize_input(user_input)
    prediction = model.predict(X_t)
    response = {'probability not promo': str(prediction[0][0].round(4)),
                'probability_promo': str(prediction[0][1].round(4))}
    return jsonify(response)

    