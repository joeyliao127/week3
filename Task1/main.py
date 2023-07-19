# -*- coding: utf-8 -*-
import urllib.request as request
import json
import csv
import re
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
	data=json.load(response)
        
data = data["result"]["results"]
with open("MRT_station.csv", "r", newline="") as MRT_File:
      MRT_Data = MRT_File.read()

#處理爬蟲讀取到的所有MRT車站名稱
MRT_split = MRT_Data.split("\n")
stations = {}
for station in MRT_split:
    if station != '':
        temp = station.split("\r") 
        stations[temp[0]] = temp[0]

MRT_List = {}

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
        MRT = item["MRT"]
        if(MRT in MRT_List):
            MRT_List[MRT].append(item["stitle"])
        else:
            MRT_List[MRT] = [MRT]
            MRT_List[MRT].append(item["stitle"])
    # print(MRT_List)
with open("mrt.csv", "w", encoding="utf-8") as mrt_file:
     writer = csv.writer(mrt_file)
     for key in MRT_List:
        temp = ""
        for item in MRT_List[key]:
            if(item):
                temp = temp+item+","
        writer.writerow([temp[:-1]])

        

    