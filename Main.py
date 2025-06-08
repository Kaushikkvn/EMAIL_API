import requests
from send_email import send_email

v="tesla"
api_key = "3f58a009dacf47d7b474242209687f75"
url = ("https://newsapi.org/v2/everything?"
       f"q={v}&"
       "from=2025-05-07&"
       "sortBy=publishedAt&"
       "apiKey=3f58a009dacf47d7b474242209687f75"
       "&language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None :
        body = "Subject: Today's news" \
                + "\n" + body + article["title"] + "\n" \
                + article["description"] \
                + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)