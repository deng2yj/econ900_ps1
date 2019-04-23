from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
import time

if not os.path.exists("html_files"):
	os.mkdir("html_files")
browser = webdriver.Safari()

for i in range(1,172):
	print("page:" + str(i))
	f = open("html_files/boardgamegeek"+str(i)+".html","w")
	# response = urllib.request.urlopen("https://boardgamegeek.com/browse/boardgame/page/"+str(i))
	# html = response.read()
	browser.get("https://boardgamegeek.com/browse/boardgame/page/"+str(i))
	html = browser.page_source

	f.write(html)
	f.close()
	time.sleep(10)

#print(html)
	print("requesting boardgamegeek")

