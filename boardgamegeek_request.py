import urllib.request
import os

if not os.path.exists("html_files"):
	os.mkdir("html_files")


for i in range(3):
	print("page:" + str(i))
	f = open("html_files/boardgamegeek.html"+str(i)+".html","wb")
	response = urllib.request.urlopen("https://boardgamegeek.com/browse/boardgame/page/"+str(i))
	html = response.read()

	f.write(html)
	f.close()

#print(html)
	print("requesting boardgamegeek")

