import requests
import json

# Make an API call, and store the repsonse.
url = 'https://hacker-news.firebaseio.com/v0/item/33156918.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
readable_file = 'data/readable_hn_data2.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)