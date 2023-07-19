import urllib.request as request
import bs4

src="https://www.ptt.cc/bbs/movie/index.html"
req = request.Request(src, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
})

with request.urlopen(req) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")

rent = root.select_one("div.r-ent")

popularity = rent.select_one("span.f3")
title = rent.select_one("div.title")
print(f"count1 = {popularity.text}")
print(f"title = {title.text}")