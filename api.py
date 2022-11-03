import requests

url = "https://sameerbhatia-proprofs-quiz-maker.p.rapidapi.com/"

headers = {
	"X-RapidAPI-Key": "07e5321b9cmsh582b7364816a345p1cbfd9jsn1e1d08d63ff7",
	"X-RapidAPI-Host": "sameerbhatia-proprofs-quiz-maker.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)