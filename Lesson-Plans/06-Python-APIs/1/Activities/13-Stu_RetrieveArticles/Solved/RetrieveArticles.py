# Dependencies
import requests as req

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

# Query parameters
api_key = "164b73c522a8420c8e05343ef1da0a7e"
q = "obama"
begin_date = "20160101"
end_date = "20160130"

param_dict = {
	'api-key': api_key,
	'q': q,
	'begin_date': begin_date,
	'end_date': end_date
}

# Retrieve articles
api_body = req.get(url, params=param_dict).json()

for article in api_body['response']['docs']:
    print("A snippet from the article: '" + article["snippet"] + "'.\n")

# BONUS: How would we get 30 results? HINT: Look up the page query param
articles_30 = []
for page in range(1, 3):
    #query = query + "&page=" + str(page)
    param_dict['page'] = page
    page_articles = req.get(url, params=param_dict).json()
    articles_30.extend([article for article in page_articles])
