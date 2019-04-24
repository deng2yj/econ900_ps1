import os
from bs4 import BeautifulSoup
import glob
import re
import pandas as pd
# import pandas as pd

if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")
# df = pd.DataFrame()

# for one_file_name in glob.glob("html_files/*.html")：
# 	print("parsing:" + one_file_name)
df = pd.DataFrame()
for one_file_name in glob.glob("html_files/*.html"):
	print("parsing:" + one_file_name)
	f = open(one_file_name, "r")

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
		boardgame_year = r.find("td", {"class": "collection_objectname"}).find("span")
		if boardgame_year is None:
			boardgame_year = ""
		else:
			boardgame_year = boardgame_year.text.replace("(","").replace(")","")
		
		boardgame_geekrating = r.find("td", {"class": "collection_bggrating"}).text
		boardgame_avgrating = r.find("td", {"class": "collection_bggrating"}).findNext("td", {"class": "collection_bggrating"}).text
		boardgame_voters = r.find("td", {"class": "collection_bggrating"}).findNext("td", {"class": "collection_bggrating"}).findNext("td", {"class": "collection_bggrating"}).text
		boardgame_price = r.find("td", {"collection_shop"}).find("div", {"class": "aad"})
		# print(boardgame_price.text)
		if boardgame_price is None:
			boardgame_listprice = ""
		else:
			boardgame_list = re.search(r'List:\s\$\d+\.\d+', boardgame_price.text)
		# 'List: \$\d+\.\d+'
		
		
			if boardgame_list is None:
				boardgame_listprice = ""
					# continue
			else:
				boardgame_listprice = re.search(r'\d+\.\d+', boardgame_list.group(0)).group(0)

				# boardgame_listpricef = boardgame_listprice.replace("List:","").replace("$","")
	
		# print(boardgame_listprice)
			# print(boardgame_price.text)
			# boardgame_listprice = boardgame_price.find("div").find("div").replace("List:", "")
	
		# print("boardgame_year: " + boardgame_year)
		# print("boardgame_name: " + boardgame_name)
		# print("boardgame_rank: " + boardgame_rank)
		# print("boardgame_geekrating: " + boardgame_geekrating)
		# print("boardgame_avgrating: " + boardgame_avgrating)
		# print("boardgame_voters: " + boardgame_voters)
		# print("boardgame_listprice: " + boardgame_listprice)
		df = df.append({
			'boardgame_name': boardgame_name.strip(),
			'boardgame_rank': boardgame_rank.strip(),
			'boardgame_year': boardgame_year.strip(),
			'boardgame_geekrating': boardgame_geekrating.strip(),
			'boardgame_avgrating': boardgame_avgrating.strip(),
			'boardgame_voters': boardgame_voters.strip(),
			'boardgame_listprice': boardgame_listprice.strip() 


			}, ignore_index = True)

df.to_csv("parsed_results/boardgamegeek_dataset.csv")

		
		



