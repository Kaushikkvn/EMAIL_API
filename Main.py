import requests

api_key="3f58a009dacf47d7b474242209687f75"
url=("https://newsapi.org/v2/everything?q=tesla&"
     "from=2025-05-07&sortBy=publishedAt&apiKey=3f58a009dacf47d7b474242209687f75")
request=requests.get(url)
content=request.json()
for source_id in content["articles"]:
    print(source_id["source"]["name"])