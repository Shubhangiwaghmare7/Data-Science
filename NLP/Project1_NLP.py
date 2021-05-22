# -*- coding: utf-8 -*-
"""
Created on Sat May  8 14:50:45 2021

@author: Shubhangi Waghmare
"""

import numpy as np
import pandas as pd
import String
import nltk
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer #TFid Vectorization

sw=stopwords.words('english')
#read the data
pos_rev=pd.read_csv('netfli')
