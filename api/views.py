from django.shortcuts import render
import json, requests


def home(request):
    response = requests.get("https://api.chucknorris.io/jokes/random")
    json_data = json.loads(response.text)
    data = {
        'frase': json_data,
    }
    return render(request, 'api/home.html', data)


def search(request):
    data = {}
    data['total'] = 0
    form = request.GET
    if form and form['key'] != "":
        link = "https://api.chucknorris.io/jokes/search?query="+form['key']
        response = requests.get(link)
        json_data = json.loads(response.text)
        data['total'] = json_data['total']
        data['busca'] = json_data['result']
    else:
        if form and data['total'] == 0:
            data['erro'] = "Unfortunately not found!"
        else:
            data['erro'] = ""

    return render(request, 'api/search.html', data)

