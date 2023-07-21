import urllib.request as request
import bs4

src="https://www.ptt.cc/bbs/movie/index.html"
http = "https://www.ptt.cc/"
result = []
i=0
def reqMaker(src):
    req = request.Request(src, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })
    return req
count = 1
firstPage = True
while(i<3):
    with request.urlopen(reqMaker(src)) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    rent = root.find_all("div", class_="r-ent")
    #When process get the web data, the process have to figure out two points.
    #First one is figure out select and select_one return data type
    #second one is figure out what is the target of HTML element
    for k in range(0, len(rent)):
        article = rent[k].select("div.title > a")
        if(article == []):
            continue
        nrecSpan = rent[k].select_one("div.nrec > span")
        print(f"nrecSpan = {nrecSpan}")
        if(nrecSpan):
            populaurity = nrecSpan.text
        else:
            populaurity = 'none'
        print(f"popularity = {populaurity}")
        articleLink = http+article[0].get('href')
        articleTitle = article[0].text
        #paging is the lastPage element parent container
        paging = root.select_one("div.btn-group-paging:nth-child(2)")
        lastPage = paging.select_one(":nth-child(2)")
        #lastPage is a URL
        lastPage = http + lastPage.get('href')
        try:
            with request.urlopen(reqMaker(articleLink)) as articlePage:
              articleData = articlePage.read().decode("utf-8")
            articleHTML = bs4.BeautifulSoup(articleData, "html.parser")
        except:
            print("404")
        
        divDate = articleHTML.select_one("#main-content div:nth-child(4) ")
        date = divDate.select_one(":last-Child")
        # date = articleSpan.text
        print(f"第：{count}篇文章")
        print(f"文章連結 = {articleLink}")
        print(f"文章標題 = {articleTitle}")
        print(f"文章日期 = {date.text}")
        print(f"lastPage  = {lastPage}")
        print('-------------------------------------------')
        count += 1
        if(firstPage and i == len(rent)):
            continue
        result.append(articleTitle + "," + populaurity + "," + date.text+"\n")
    src = lastPage
    i +=1

with open("movies.txt", "w", encoding="utf-8") as file:
    file.writelines(result)

# for item in range(0,len(rent)-1):
    