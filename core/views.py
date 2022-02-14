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
            'x-rapidapi-key': config("statsapi")
            }
        
        responses = requests.request("GET", url, headers=headers, params=querystring).json()
        info=responses['artist_info']
        pic=info['avatar']
        name=info['name']
        
        stats=responses['stats']
        source=stats[0]['source']
        spotify=stats[0]['data']
        total_streams=spotify['streams_total']
        monthly=spotify['monthly_listeners_current']
        followers=spotify['followers_total']

        tiktok=stats[5]['data']
        videos=tiktok['videos_total']
        views=tiktok['views_total']
        tikfollowers=tiktok['followers_total']

        youtube=stats[4]['data']
        subs=youtube['subscribers_total']
        chaviews=youtube['channel_views_total']
        vidlikes=youtube['video_likes_total']
        context = {'name':name,'total_streams':total_streams,'pic':pic,'monthly':monthly,'followers':followers,'videos':videos,'views':views,'tikfollowers':tikfollowers,'subs':subs,'chaviews':chaviews,'vidlikes':vidlikes}
        print(name)
    return render(request, 'index.html',context)


