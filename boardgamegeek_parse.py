import os
from bs4 import BeautifulSoup
import glob
# import pandas as pd

if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")
# df = pd.DataFrame()

# for one_file_name in glob.glob("html_files/*.html")：
# 	print("parsing:" + one_file_name)

f = open("html_files/boardgamegeek1.html", "r")

# print(f.read())

soup = BeautifulSoup(f.read(), 'html.parser')

print(soup)