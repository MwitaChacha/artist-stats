from django.shortcuts import render
import requests
from decouple import config
from django.views.generic import TemplateView
# Create your views here.

def index(request):
    context=None
    local=None
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
        uri= uri[15:]
        profile=data['profile']
        title=profile['name']
        visuals=data['visuals']
        avatar=visuals['avatarImage']
        sources=avatar['sources']
        url=sources[0]['url']
        
        context = {'url':url,'name':title,'uri':uri}
    
    if 'stats' in request.GET:
        stats = request.GET.get('stats')

        url = "https://songstats.p.rapidapi.com/artists/stats"
        
        querystring = {"source": "all" ,"spotify_artist_id":stats}
        
        headers = {
            'x-rapidapi-host': "songstats.p.rapidapi.com",
            # 'x-rapidapi-key': config("statsapi")
            }
        
        responses = requests.request("GET", url, headers=headers, params=querystring).json()
        info=responses['artist_info']
        pic=info['avatar']
        name=info['name']
        
        stats=responses['stats']
        source=stats[0]['source']
        data=stats[0]['data']
        total_streams=data['streams_total']
        # spotify=source[0]['spotify']
        # youtube=stats[4]['youtube']
        context = {'name':name,'data':data,'total_streams':total_streams}
        print(name)
    return render(request, 'index.html',context)


