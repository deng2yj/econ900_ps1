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

#print(soup)
f.close()

boardgames_table = soup.find("table", {"id": "collectionitems"})
# print(boardgames_table)
# boardgames_tbody = boardgames_table.find("tbody")
# print(boardgames_tbody)
boardgames_rows = boardgames_table.find_all("tr", {"id":"row_"})
# print(boardgames_rows)


boardgame_name = boardgames_rows[0].find("td", {"class": "collection_objectname"}).find("a").text
boardgame_rank = boardgames_rows[0].find("td", {"class": "collection_rank"}).text
boardgame_year = boardgames_rows[0].find("td", {"class": "collection_objectname"}).find("span").text
boardgame_geekrating = boardgames_rows[0].find("td", {"class": "collection_bggrating"}).text
boardgame_avgrating = boardgames_rows[0].find("td", {"class": "collection_bggrating"}).findNext("td", {"class": "collection_bggrating"}).text
boardgame_voters = boardgames_rows[0].find("td", {"class": "collection_bggrating"}).findNext("td", {"class": "collection_bggrating"}).findNext("td", {"class": "collection_bggrating"}).text
boardgame_price = boardgames_rows[0].find("td", {"collection_shop"}).find("div", {"class": "aad"}).find("div").find("div").text
# collection_Listprice = boardgame_price.next_element.next_element.next_element.next_element
print(boardgame_year)
print(boardgame_name)
print(boardgame_rank)
print(boardgame_geekrating)
print(boardgame_avgrating)
print(boardgame_voters)
print(boardgame_price)



