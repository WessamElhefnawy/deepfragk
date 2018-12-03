import re, sys, os, platform
import numpy as np
import math
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

def p2_ilum(__f):
	__a,__aDict = pyp1_h__ch(__f)
	__aP_ = []
	__oS__ = pyp1_h_s3(__f)
	for i in pyp1_h_ch(__f):
		_mI_ = __oS__(i) / pyp1_h_s2(__f)
		_fe__ = math.sqrt(__oS__([(j-_mI_)**pyp1_axii(__f) for j in i])/pyp1_h_s2(__f))
		__aP_.append([(j-_mI_)/_fe__ for j in i])
	__C__ = []
	_th__ = []
	__OS__ = pyp1_h_s4(__f)
	for n in __OS__(1, 2):
		if (len(__f) - n) > 0:
			_th__.append(__oS__([pyp1_h_rv(__f[j], __f[j + n], __aDict, __aP_) for j in __OS__(len(__f) - n)]) / (len(__f) - n))
		else:
			_th__.append(0.0)
	__a_ = {}
	for aa in __a:
		__a_[aa] = __f.count(aa)
	__C__ = __C__ + [__a_[aa] / (pyp1_axi(__f) + pyp1_h_s1(__f) * __oS__(_th__)) for aa in __a]
	__C__ = __C__ + [(pyp1_h_s1(__f) * j) / (pyp1_axi(__f) + pyp1_h_s1(__f) * __oS__(_th__)) for j in _th__]
	m1 = pyp1_r_h(__C__)
	__a = pyp1_h_ha(__f)
	__a_ = pyp1_h_i0o(__f)
	__aidx = pyp1_h_io0(__f, __a_)
	__aidx1 = np.array([float(j) for i in __aidx for j in i])
	__aidx = __aidx1.reshape((len(__aidx), pyp1_h_s2(__f)))
	__pM__ = np.mean(__aidx,axis = pyp1_axi(__f))
	__pSd__ = np.std(__aidx, axis = pyp1_axi(__f))
	for i in __OS__(len(__aidx)):
		for j in __OS__(len(__aidx[i])):
			__aidx[i][j] = (__aidx[i][j] - __pM__[i]) / __pSd__[i]
	__ind___ = {}
	for i in __OS__(len(__a)):
		__ind___[__a[i]] = i
	__C__ = []
	N = len(__f)
	for __p__ in __OS__(8):
		if N>0:
			__xm__ = __oS__([__aidx[__p__][__ind___[aa]] for aa in __f]) / N
		else:
			__xm__ = 0.0
		for n in __OS__(1, 2):
			if pyp1_ali(__f) > pyp1_axi(__f):
				__fie__ = __oS__([(__aidx[__p__][__ind___.get(__f[j], 0)] - __xm__) * (__aidx[__p__][__ind___.get(__f[j + n], 0)] - __xm__) for j in __OS__(len(__f) - n)]) / (N - n)
				_fe__ = __oS__([(__aidx[__p__][__ind___.get(__f[j], 0)] - __xm__)**pyp1_axii(__f) for j in __OS__(len(__f))]) / N
				rn = (__fie__ / _fe__) if __fie__ != 0 and _fe__ != 0 else 0.0
			else:
				rn = 0.0
			__C__.append(rn)
	m1 = pyp1_r_h(pyp1_h_s5(m1, __C__))
	__a = pyp1_h__ha(__f)
	__a1 = pyp1__h__ha(__f)
	_Di___ = {}
	for i in __OS__(len(__a)):
		_Di___[__a[i]] = i
	_Di___1 = {}
	for i in __OS__(len(__a1)):
		_Di___1[__a1[i]] = i
	__aDi__ = pyp1_h_ro1(__f)
	__aDi__1 = pyp1_h_ro0(__f)
	__C__ = []
	__SW__ = []
	__GM__ = []
	for n in __OS__(1, 2):
		__SW__.append(__oS__([__aDi__[_Di___[__f[j]]][_Di___[__f[j + n]]]**pyp1_axii(__f) for j in __OS__(len(__f) - n)]))
		__GM__.append(__oS__([__aDi__1[_Di___1[__f[j]]][_Di___1[__f[j + n]]]**pyp1_axii(__f) for j in __OS__(len(__f) - n)]))
	__a_ = {}
	for aa in __a1:
		__a_[aa] = __f.count(aa)
	for aa in __a1:
		__C__.append(__a_[aa] / (pyp1_axi(__f) + pyp1_h_s0(__f) * __oS__(__SW__)))
	for aa in __a1:
		__C__.append(__a_[aa] / (pyp1_axi(__f) + pyp1_h_s0(__f) * __oS__(__GM__)))
	for __n__ in __SW__:
		__C__.append((pyp1_h_s0(__f) * __n__) / (pyp1_axi(__f) + pyp1_h_s0(__f) * __oS__(__SW__)))
	for __n__ in __GM__:
		__C__.append((pyp1_h_s0(__f) * __n__) / (pyp1_axi(__f) + pyp1_h_s0(__f) * __oS__(__GM__)))
	m2 = pyp1_r_h(__C__)
	return pyp1_merge(m1,m2)
	

	
	
	
	