import requests
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code)
resoponse_dict = r.json()
print(resoponse_dict.keys())