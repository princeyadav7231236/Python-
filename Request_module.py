import requests

a = requests.get("https://newsapi.org/docs/get-started#top-headlines")
# print(a.text)
# print(a.status_code)

url = "www.something.com"
data = {
    "var_1": 420,
    "var_2": 45
}
# b = requests.post(url= url, data = data)
# print(b.text)

