import numpy as np
from numpy import concatenate, around
from pprint import pprint
import os
import sys
import os
import shutil
import numpy
import pymongo
import numpy as np
import keras
from sklearn.neural_network import BernoulliRBM
from sklearn.externals import joblib
import pywt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
import time
from pylib import *
from keras.optimizers import RMSprop
from keras.models import Sequential
from keras.layers import Dense
from pprint import pprint
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adagrad
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

def f2r(_l):
	__l = py__nu()
	_n = ''
	_f = ''
	for l in py__it(_l):
		l = py__clean(l)
		if py__whats(l):
			_n = py__trims(l)
		else:
			_f += py__super(l)
	return py__tub(_n,_f)
			