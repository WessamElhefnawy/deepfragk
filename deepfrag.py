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

numpy.random.seed(7)
np.set_printoptions( threshold = np.nan )


if len(sys.argv) ==2:
	iFF = str(sys.argv[1])
else:
	exit()
L = []
with open(iFF) as _file:
	for line in _file:
		L.append(line.strip())
____n,____f = f2r(L)
model = model(context.deepfragm(),context.deepfragc0(),context.deepfragc1())
VS = model.scaler_v()
l_model =  model.model_f()
ts = time.time()
FFR, FFC = [], []
for j in range(model._min(),model._max()):
	f = f2f( ____n,____f, j)
	f2p(ts,(____n,____f))
	p = p2f(ts, (____n,____f), j)
	VL = model.scaler_l(j)
	FC = [context.deepfragc3()] * context.deepfragcn()
	PC = [context.deepfragc3()] * context.deepfragcn()
	for i in range(len(f)) :
		c = f_ilum(f[i][context.deepfragc2()].upper(), p[i][context.deepfragc2()])
		c = VL.transform([c])
		c = VS.transform(c)
		ynew,predicted = model.do(c,l_model)
		FC,PC = model.foi(ynew,predicted,FC,PC)
	FFR.append(FC)
	FFC.append(PC)
l_model = model.model_P()
VL = model.scaler_P()
ynew = l_model.predict(np.expand_dims(np.matrix((VL.transform(np.sum(np.matrix(FFR), axis = 0))).tolist()), axis=2))
PPR = np.argmax(ynew, axis=1)
output = model.values(PPR[0])
if os.path.isdir(context.deepfragh() + str(ts)):
	shutil.rmtree(context.deepfragh() + str(ts))
for i in range(len(FFC)):
	for j in range(model.ranger(i)[0],model.ranger(i)[1]+1):
		output += ',' + str(FFC[i][j])
print(output)
