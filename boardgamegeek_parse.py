import os
from bs4 import BeautifulSoup
import glob
import re
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
boardgames_tbody = boardgames_table.find("tbody")
# print(boardgames_tbody)
boardgames_rows = boardgames_tbody.find_all("tr", {"id":"row_"})
# print(boardgames_rows)

for r in boardgames_rows:

	boardgame_name = r.find("td", {"class": "collection_objectname"}).find("a").text
	boardgame_rank = r.find("td", {"class": "collection_rank"}).text
	boardgame_year = r.find("td", {"class": "collection_objectname"}).find("span").text.replace("(","").replace(")","")
	boardgame_geekrating = r.find("td", {"class": "collection_bggrating"}).text
	boardgame_avgrating = r.find("td", {"class": "collection_bggrating"}).findNext("td", {"class": "collection_bggrating"}).text
	boardgame_voters = r.find("td", {"class": "collection_bggrating"}).findNext("td", {"class": "collection_bggrating"}).findNext("td", {"class": "collection_bggrating"}).text
	boardgame_price = r.find("td", {"collection_shop"}).find("div", {"class": "aad"})
	# print(boardgame_price.text)
	boardgame_list = re.search(r'List:\s\$\d+\.\d+', boardgame_price.text)
	# 'List: \$\d+\.\d+'
	
	
	if boardgame_list is None:
			continue
	else:
			boardgame_listprice = boardgame_list.group(0).replace("List:","").replace("$","")
			# boardgame_listpricef = boardgame_listprice.replace("List:","").replace("$","")

	# print(boardgame_listprice)
		# print(boardgame_price.text)
		# boardgame_listprice = boardgame_price.find("div").find("div").replace("List:", "")

	print("boardgame_year: " + boardgame_year)
	print("boardgame_name: " + boardgame_name)
	print("boardgame_rank: " + boardgame_rank)
	print("boardgame_geekrating: " + boardgame_geekrating)
	print("boardgame_avgrating: " + boardgame_avgrating)
	print("boardgame_voters: " + boardgame_voters)
	print("boardgame_listprice: " + boardgame_listprice)



