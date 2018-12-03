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


def f2f(_n,_f,__l):
	_l = py__l(_f)
	_s = 0
	_e = __l
	___f = py__nu()
	while _e <= _l :
		_t = py__cut(_f,_s,_e)
		___f = py__tubl(___f,_n,_s,__l,_t)
		_s += 1
		_e += 1
		
	return ___f
			
	