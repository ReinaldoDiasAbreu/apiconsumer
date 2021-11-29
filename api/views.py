from django.shortcuts import render
import json, requests


def home(request):
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        json_data = json.loads(response.text)
        data = {
            'frase': json_data,
        }
        return render(request, 'api/home.html', data)
    except:
        return render(request, 'api/erro.html')


def search(request):
    try:
        data = {}
        data['total'] = -1
        data['erro'] = ""
        form = request.GET
        if form and form['key'] != "":
            link = "https://api.chucknorris.io/jokes/search?query="+form['key']
            response = requests.get(link)
            json_data = json.loads(response.text)
            data['total'] = json_data['total']
            data['busca'] = json_data['result']
            if data['total'] == 0:
                data['erro'] = "Unfortunately not found!"
        return render(request, 'api/search.html', data)
    except:
        return render(request, 'api/erro.html')
