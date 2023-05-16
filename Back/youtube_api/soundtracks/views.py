from django.shortcuts import render
from django.conf import settings

# rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view

# requests
import requests

# Create your views here.

# YOUTUBE API
YOUTUBE_api_key = settings.API_KEY
BASE_url = "https://www.googleapis.com/youtube/v3/search"

@api_view(['GET'])
def get_soundtrack(request):
    # 넘겨받은 movie_name 꺼내기
    movie_name = request.GET.get('movie_name')

    # 노래 제목도 넘겨 받았으면 꺼내기 
    music_name = request.GET.get('music_name')

    # Youtube API로 해당 영화의 soundtrack playlist 받기 
    part = 'snippet'
    maxResults = 1

    if music_name:
        q = f'{music_name} of {movie_name} music'
        type = 'video'
    else:
        q = f'{movie_name} soundtrack'
        type = 'playlist'

    url = f'{BASE_url}?part={part}&q={q}&maxResults={maxResults}&type={type}&key={YOUTUBE_api_key}'
    res = requests.get(url)
    soundtrack_data = res.json()
    context = {
        'id' : soundtrack_data.get('items')[0].get('id'),
        'title' : soundtrack_data.get('items')[0].get('snippet').get('title')
    }

    return Response(context)