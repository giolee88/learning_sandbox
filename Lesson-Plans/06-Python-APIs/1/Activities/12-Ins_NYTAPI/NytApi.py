# Dependencies
import requests as req

# pass params as dict
base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
api_key = "164b73c522a8420c8e05343ef1da0a7e"

# Search for articles that mention granola
q = "granola"

response = req.get(base_url, params = {'api-key': api_key, 'q': q})
api_body = response.json()

articles = api_body["response"]["docs"]

# Proof articles stored
print("Your Reading List\n")
for article in articles:
    print(article["web_url"])