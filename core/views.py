from django.shortcuts import render
import requests
from decouple import config
# Create your views here.

def index(request):
    if 'artist' in request.GET:
        artist = request.GET.get('artist')
        url = "https://spotify23.p.rapidapi.com/search/"
        
        querystring = {"q":artist,"type":"multi","offset":"0","limit":"1","numberOfTopResults":"5"}
        
        headers = {
            'x-rapidapi-host': "spotify23.p.rapidapi.com",
            'x-rapidapi-key': config('rapidapi')
            }
        
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        artist = response['artists']
        item = artist['items']
        data = item[0]['data']
        uri=data['uri']
        
        print(uri)
    return render(request, 'index.html')