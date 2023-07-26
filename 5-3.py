#triple ensemble

#RandomForestClassifier
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
wine = pd.read_csv('/Users/ujong-yun/Desktop/혼공머/wine.csv')
data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
target = wine['class'].to_numpy()
train_input, test_input, train_target, test_target = train_test_split(data, target, test_size = 0.2, random_state = 42)

from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_jobs = -1, random_state=42)
scores = cross_validate(rf, train_input, train_target, return_train_score=True, n_jbos=-1)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))