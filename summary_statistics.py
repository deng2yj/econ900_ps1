import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series
import statsmodels #FOR NEXT STEP -- RUNNING REGRESSIONS 
import statsmodels.api as sm
import statsmodels.formula.api as smf 

dataset = pd.read_csv("parsed_results/boardgamegeek_dataset.csv")
# for i in range(7):
dataset["boardgame_avgrating"] = pd.to_numeric(dataset["boardgame_avgrating"])
dataset["boardgame_geekrating"] = pd.to_numeric(dataset["boardgame_geekrating"])
dataset["boardgame_listprice"] = pd.to_numeric(dataset["boardgame_listprice"])
dataset["boardgame_voters"] = pd.to_numeric(dataset["boardgame_voters"])
dataset["boardgame_year"] = pd.to_numeric(dataset["boardgame_year"])
dataset["boardgame_rank"] = pd.to_numeric(dataset["boardgame_rank"])
# dataset = pd.to_numeric(dataset1, errors = 'coerce')

print(np.round(dataset.describe(), 2).T)
# dataset = dataset.dropna()

# print(dataset.shape)