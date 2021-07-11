import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "b28cffec83msh01f2949c69f1af9p16ee98jsnb1cc8145b207",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

r = requests.get(url, headers = headers).json()

print(r)