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
MRT_List = MRT_Data.split("\n")
stations = {}
MRT_Result = {}
for station in MRT_List:
    if station != '':
        temp = station.split("\r") 
        stations[temp[0]] = temp[0]

# print(stations , "\n=================")

#將資料寫入文件
with open("data.csv", "w", encoding="utf-8") as file:
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
        cut_info = item["info"].split("站")
        # print(cut_info)
        for word in cut_info: #word的最後幾個字有可能是站名。
            flag = False
            for i in range(6, 1, -1):
                if(len(word)< i):#如果字串長度不夠，執行下一次
                     continue
                elif(word[-2:] == '捷運'):
                     if(word[-4:-2] in stations):
                        if(word[-i:] in MRT_Result):
                          MRT_Result[word[-i:]].append(item["stitle"])
                          print(f"找到：{word[-i:]}")
                        else:
                            MRT_Result[word[-i:]] = [word[-i:]] 
                            print(f"找到：{word[-i:]}")
                            flag = True
                        break
                elif(word[-i:] in stations):
                    # print(f"找到：{word[-i:]}")
                    if(word[-i:] in MRT_Result):
                        MRT_Result[word[-i:]].append(item["stitle"])
                    else:
                        MRT_Result[word[-i:]] = [word[-i:]] 
                    flag = True
                    break
            if(flag):
                 break
        # print("=========================")
             
                     
        # for station in stations:
        #     if station in item["info"]: #站名是否存在文章內容
        #         if station not in MRT_Result: #當MRT_Result找不到station key的時候
        #             MRT_Result[station] = [station] #建立一個新的key，value則是一個list，list[0] = station名稱
        #         else:
        #             MRT_Result[station].append(item["stitle"]) #MRT_Result已經有key，則將景點append到value這個list裡面
        #             break
            
    print(MRT_Result)


        

                
#建立mrt.csv


    