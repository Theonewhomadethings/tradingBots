import pandas as pd
import numpy as np
import keras
import tensorflow as tf
import sklearn.metrics as metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
import seaborn as sns
import pickle
from sklearn.metrics import precision_score, recall_score, accuracy_score, balanced_accuracy_score, f1_score
import os
from collections import Counter
from keras.models import model_from_json
import pickle
from sklearn import preprocessing


json_file = open(
    './current_models/model2/lstm.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

loaded_model = tf.keras.models.model_from_json(loaded_model_json)
loaded_model.load_weights('./current_models/model2/lstm.h5')

sc = pickle.load(
    open('./current_models/model2/scaler.pkl', 'rb'))


def predict_multiple_days(data, feature_length):

    def split(to_split):
        to_split = np.array_split(np.array(to_split), len(to_split)//390)
        return to_split

    days_data = split(data)

    preds = []
    for day_data in days_data:
        p = predict_day(day_data, feature_length)
        preds.append(p)

    return preds


def predict_day(data, feature_length):
    
    data = data[:feature_length]

    data = pd.DataFrame([data])

    normalized = preprocessing.normalize(data)
    data = pd.DataFrame(normalized)
    scaled = sc.fit_transform(data.T)
    data = pd.DataFrame(scaled.T)
    data = tf.reshape(
        data, data.shape + (1,))

    pred = loaded_model.predict(data)

    return pred[0][0]
