import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

dataset = pd.read_csv("parsed_results/boardgamegeek_dataset.csv")
# for i in range(7):
dataset["boardgame_avgrating"] = pd.to_numeric(dataset["boardgame_avgrating"])
dataset["boardgame_geekrating"] = pd.to_numeric(dataset["boardgame_geekrating"])
dataset["boardgame_listprice"] = pd.to_numeric(dataset["boardgame_listprice"])
dataset["boardgame_voters"] = pd.to_numeric(dataset["boardgame_voters"])
dataset["boardgame_year"] = pd.to_numeric(dataset["boardgame_year"])
dataset["boardgame_rank"] = pd.to_numeric(dataset["boardgame_rank"])
# dataset = pd.to_numeric(dataset1, errors = 'coerce')

dataset = dataset.dropna()

print(dataset.shape)

target = dataset.iloc[:,6].values
# target_number = pd.to_numeric(target, errors = 'coerce')
data = dataset.iloc[:,2:6]
# data_number_1 = pd.to_numeric(data, errors = 'coerce')
# 
print(target)
print(data.head())

data_training, data_test, target_training, target_test = train_test_split(data, target, test_size = 0.2, random_state = 1)
svm_model = SVC(kernel='linear', C=1E5)
svm_model.fit(data_training, target_training)
predictions = svm_model.predict(data_test)
print(r2_score(target_test, predictions))
# print(predictions.shape)
# print(data_test.shape)

