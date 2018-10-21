#imports for data processing
import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import unicodedata
import sys
from tqdm import tqdm
import pandas as pd
import os
from random import shuffle
import string
#imports for nural network
import tensorflow as tf
from keras.models import Sequential
from keras.layers import *
from keras.optimizers import *
from keras.models import load_model

#Initialise the Class and dataset
sd = SetData()
train_data, tr_words = sd.train_data_with_label()
test_data, tst_words = sd.test_data_with_label()
#generate Bag of word for the training/testing data
training = sd.bag_of_words(train_data,tr_words)
training_data = list(training[:, 0])
training_label = list(training[:, 1])
testing = sd.bag_of_words(test_data,tr_words,'test')# here also we have to pass the training words because even for the test set the BOW will be generated based on the training set corpus
testing_data = list(testing[:, 0])
testing_label = list(testing[:, 1])