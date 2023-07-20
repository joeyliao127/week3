# -*- coding: utf-8 -*-
import urllib.request as request
import json
import csv

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
	data=json.load(response)
        
data = data["result"]["results"]
MRT = {}
#將資料寫入文件
with open("attraction.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
      #data是一個list，list底下有很多字典。
      #讀取我們需要的資訊，如info, address, longitude, latitude, file裡面的a
    #建立attraction.csv
    for item in data:
        #   writer.writerow(["stitle:"+line["stitle"]])
        stitle = item["stitle"]
        address = item["address"][5:8] 
        longitude = item["longitude"]
        latitude = item["latitude"]
        link = item["file"].split("https:")
        firstLink = "https:" + link[1]
        writer.writerow([stitle]+[address]+[longitude]+[latitude]+[firstLink])     
        if(item["MRT"] == None):
             continue
        elif(item["MRT"] not in MRT):
             MRT[item["MRT"]] = item["MRT"]
             MRT[item["MRT"]] += ","+item["stitle"]
        else:
             MRT[item["MRT"]] += ","+item["stitle"]
print(MRT)             
with open("mrt.csv", "w", encoding="utf-8") as mrt_file:
    writer = csv.writer(mrt_file)
    for key in MRT:
        writer.writerow([MRT[key]])

        

    