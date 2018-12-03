import re
from collections import Counter
import re, math
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

def p1_ilum(_f):
	_ba = pyp3_s_ba(_f)
	___v__ = Counter(_f)
	for key in pyp3_s_iil(___v__):
		___v__[key] = pyp3_s_ol(___v__[key],pyp3_s_ol_(_f))
	_C_ = []
	for cc in _ba:
		_C_.append(___v__[cc])
	_m = pyp3__s_a_(_C_)
	_C_ = []
	__a = pyp3_s_pp(_f)
	for p in pyp3_s__v():
		__f, ___f, ____f = pyp3_s_iii(_f)
		for ___v_ in __a:
			if pyp3_s__as(pyp3_s_as(pyp3_s_sn(pyp3_s_sff(___v_),pyp3_s_g(p)),pyp3_s_sb(pyp3_s_sss(___v_),pyp3_s_v(p))),pyp3_s_as(pyp3_s_sc(pyp3_s_sff(___v_),pyp3_s_v(p)),pyp3_s_sa(pyp3_s_sss(___v_),pyp3_s_g(p)))):
				__f = pyp3_s_is(__f,pyp3_s_io(_f))
				continue
			if pyp3_s__as(pyp3_s_as(pyp3_s_sa(pyp3_s_sff(___v_),pyp3_s_g(p)),pyp3_s_sb(pyp3_s_sss(___v_),pyp3_s_k(p))),pyp3_s_as(pyp3_s_sn(pyp3_s_sff(___v_),pyp3_s_k(p)),pyp3_s_sc(pyp3_s_sss(___v_),pyp3_s_g(p)))):
				___f = pyp3_s_isi(___f,pyp3_s__io(_f))
				continue
			if pyp3_s__as(pyp3_s_as(pyp3_s_sc(pyp3_s_sff(___v_),pyp3_s_v(p)),pyp3_s_sn(pyp3_s_sss(___v_),pyp3_s_k(p))),pyp3_s_as(pyp3_s_sx(pyp3_s_sff(___v_),pyp3_s_k(p)),pyp3_s_sa(pyp3_s_sss(___v_),pyp3_s_v(p)))):
				____f = pyp3_s__isi(____f,pyp3__s__io(_f))
		if pyp3___s___s(__a)>pyp3__s_oio(_f):
			_C_ = _C_ + [__f/pyp3___s___s(__a), ___f/pyp3___s___s(__a), ____f/pyp3___s___s(__a)]
		else:
			_C_ = _C_ + [__f/pyp3___s____s(_a), ___f/pyp3___s____s(_a), ____f/pyp3___s____s(_a)]
	__m = pyp3_r_s(pyp3_s_a_(_C_))
	_C_ = []
	for p in pyp3_s_():
		_C_ = _C_ + pyp3__s__as(pyp3_s_c(pyp3__s__v(p), _f),pyp3_s_c(pyp3_s__k(p), _f),pyp3_s_c(pyp3_sk(p), _f))
	___m = pyp3_r_s(pyp3_s_a1(_C_))
	return pyp3_merge(pyp3_r_s(_m),__m,___m)
