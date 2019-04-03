import urllib.request
import os

if not os.path.exists("html_files"):
	os.mkdir("html_files")

f = open("html_files/boardgamegeek.html","wb")
response = urllib.request.urlopen("https://boardgamegeek.com/browse/boardgame")
html = response.read()

f.write(html)
f.close()

print(html)

