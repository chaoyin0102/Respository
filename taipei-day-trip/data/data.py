#coding=utf-8
import json
import mysql.connector
import re

# open JSON file
json_data = open("taipei-attractions.json", mode="r", encoding="utf-8").read()
raw_data = json.loads(json_data)
data = raw_data["result"]["results"]

print(type(json_data))

# make the connection with mysql
trip_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "new_db2"
)
cursor = trip_db.cursor()

# get attraction
for attr in data:
    id = attr["_id"]
    name = attr["name"]
    category = attr["CAT"]
    transport = attr["direction"]
    description = attr["description"]
    address = attr["address"]
    mrt = attr["MRT"]
    latitude = attr["latitude"]
    longitude = attr["longitude"]
    preImage = attr["file"].split("https://")
    preImage2 = ["https://"+ i for i in preImage if re.search("JPG", i)]
    preImage3 = ["https://"+ i for i in preImage if re.search("jpg", i)]
    new_image=",".join(preImage2+preImage3)


    # insert data into mysql
    cursor.execute("INSERT ignore INTO attractions2 (id, name, category, transport, description, address, mrt, lat, lng, images) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id,name,category,description,address,transport,mrt,latitude,longitude, new_image))
        
trip_db.commit()
trip_db.close()
    


# _id ID
# name 景點名稱
# direction 交通方式
# description 景點描述
# CAT 分類
# date 日期
# address 地址
# file 圖片
# MRT 捷運站
# latitude 緯度
# longitude 經度