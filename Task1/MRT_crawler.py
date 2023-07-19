import urllib.request as request
import bs4
import csv
src = "https://ericyu.org/blog/archives/2016/04/256"
req = request.Request(src, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}) 
with request.urlopen(req) as response:
    #取得HTML內容
    data = response.read().decode("utf-8") 

#bs4.BeautifulSoup()放入已經取得的HTML(data)，並告訴Bs4是一個HTML檔案(html.parser)。
root = bs4.BeautifulSoup(data, "html.parser")

td = root.select("td:last-child")
with open("MRT_station.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for i in td:
        writer.writerow([i.string])