import requests
# from news_mail import auto_mate
from newsdataapi import NewsDataApiClient
import subprocess as sp
import os

url_news = "https://bing-news-search1.p.rapidapi.com/news"
querystring = {"safeSearch":"Off","textFormat":"Raw"}
headers = {
	"X-BingApis-SDK": "true",
	"X-RapidAPI-Key": "820f09bd68mshceb97b45023b9e2p11bac7jsne8ef945cd0fb",
	"X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
}
# X-ACCESS-KEY = https://newsdata.io/api/1/news?apikey=pub_32125cd8319f40a400c0d795c2969895561c1&q=

#Todays news
response_news = requests.get(url_news, headers=headers, params=querystring)
news_name = response_news.json()['value'][0]['name']
news_desc = response_news.json()['value'][0]['description']
Title = news_name
desc = news_desc
# print('Title:',Title)
# print('Description:',desc)

#technology
print("News generating...") 

# API key authorization, Initialize the client with your API key
api = NewsDataApiClient(apikey="pub_32125cd8319f40a400c0d795c2969895561c1")
# You can pass empty or with request parameters {ex. (country = "us")}
response = api.news_api(language="en", category="technology",size=3,country="in")
# print("news-----------------------------------------------------1")
# Tit = (response.get('results')[0]["title"])
# (response.get('results')[0]["description"])
# print("news-----------------------------------------------------2")
# print(response.get('results')[1]["title"])
# print(response.get('results')[1]["description"])
# print("news-----------------------------------------------------3")
# print(response.get('results')[2]["title"])
# print(response.get('results')[2]["description"])
Title_tech = ''
des_tech = ''
for items in response.get('results'):
    Title_tech = items['title']
    des_tech = items['description']
    
# msg = "msg"
# file_path = "output.txt"
# with open(file_path, "w") as file:
# 	content = msg
# 	file.write(content)

msg_content = f'''Good Morning Team:
Today's news: {Title}{desc} \n
Tech news: {Title_tech} {des_tech}'''
	
#opening notepad
sp.Popen(["notepad","output.txt"])

file = open("output.txt", "w")

file.write(msg_content)
file.close()

print(msg_content)


# auto_mate(items)
# # import requests

# # url = "https://webit-news-search.p.rapidapi.com/trending"

# # querystring = {"language":"en"}

# # headers = {
# # 	"X-RapidAPI-Key": "820f09bd68mshceb97b45023b9e2p11bac7jsne8ef945cd0fb",
# # 	"X-RapidAPI-Host": "webit-news-search.p.rapidapi.com"
# # }

# # response = requests.get(url, headers=headers, params=querystring)

# # print(response.json())
# # main_data = (response.json())
# # # print(main_data)
# # dat = main_data['data']


# # res = dat['results']
# # print(dat)
# # print(res)
# # print(res[0])
# # # result = dat.get('results')

# # # main_data = []
# # # result_data = main_data(results)
# # # print(result_data)
# # # weather_dis = weather_res.json()
# # # # print(weather_dis)
# # # desc = weather_dis["data"]

# import requests

# url = "https://google-news13.p.rapidapi.com/latest"

# querystring = {"lr":"en-US"}

# headers = {
# 	"X-RapidAPI-Key": "820f09bd68mshceb97b45023b9e2p11bac7jsne8ef945cd0fb",
# 	"X-RapidAPI-Host": "google-news13.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)
# # print(response.json()['items'][0])
# print(response.json()['items'][0]['snippet'])


