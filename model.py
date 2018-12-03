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
from keras.layers import Concatenate, Dense, LSTM, Input, concatenate
from keras.optimizers import Adagrad
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json




class model(object):
	def __init__(self,v,n,m):
		self.v = v
		self.__min, self.__max = n, m
		self.SCOPE = [ E.upper() for E in context.deepfragsp()]
		
	def scaler_v(self):
		return joblib.load(self.v + context.deepfragmsv())
		
	def model_f(self):
		json_file = open(self.v + context.deepfragmjf(), 'r')
		loaded_model_json = json_file.read()
		json_file.close()
		loaded_model = model_from_json(loaded_model_json)
		loaded_model.load_weights(self.v + context.deepfragmmf())
		loaded_model.compile(loss='categorical_crossentropy', optimizer=RMSprop(),metrics=['accuracy'])
		return loaded_model
		
	def ranger(self,i):
		C = {
			0: (0, 4),
			1: (5, 15),
			2: (16, 26),
			3: (27, 30),
			4: (31, 36),
			5: (37, 38),
			6: (39, 45),
			7: (46, 53),
			8: (54, 58),
			9: (59, 70),
			10: (71, 75),
			11: (76, 82),
			12: (83, 86),
			13: (87, 89),
			14: (90, 91),
			15: (92, 96),
			16: (97, 99)
		}
		return C[i]
		
	def scaler_l(self,l):
		return joblib.load(self.v + context.deepfragmssl().format(l,l))
		
	def _min(self):
		return self.__min
		
	def _max(self):
		return self.__max
		
	def do(self, c, m):
		_zi = c[:,0:context.deepfragmss()]
		_fi  = c[:,context.deepfragmss():context.deepfragmss()+context.deepfragmss0()]
		_te = c[:,context.deepfragmss()+context.deepfragmss0():]
		z = m.predict([_zi, _te, _fi])
		return z,argmax(z, axis=1)
		
	def foi(self,yr,pr,f,p):
		f[pr[0]] +=1
		if yr[0,pr[0]] >=  1.0:
			p[pr[0]] += 1
		return f,p
		
	def model_P(self):
		json_file = open(self.v + context.deepfragmjp(), 'r')
		loaded_model_json = json_file.read()
		json_file.close()
		loaded_model = model_from_json(loaded_model_json)
		loaded_model.load_weights(self.v + context.deepfragmmp())
		loaded_model.compile(loss='categorical_crossentropy', optimizer=RMSprop(),metrics=['accuracy'])
		return loaded_model
		
	def scaler_P(self):
		return joblib.load(self.v + context.deepfragmsp())
	
	def values(self,p):
		return str(self.SCOPE[p])
