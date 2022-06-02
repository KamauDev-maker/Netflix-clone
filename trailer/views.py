from django.shortcuts import render,redirect
from django.http.response import JsonResponse
import requests
from django.http import HttpResponse

# Create your views here.

API_KEY = '109cc9e749c0dfa875c1fa23b2bb9d3a'

def index(request):
    return render(request, 'trailer/index.html')

def view_movie_detail(request, movie_id):
    data =requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}')
    return render(request, 'trailer/movie_detail.html',{'data':data.json()})

def search(request):
    #Get the query from the search box
    query =request.GET.get('q')
    print(query)
    
    #if the query is not empty
    if query:
        
        #get the results fro the Api
        data = requests.get(f'https://api.themoviedb.org/3/search/{request.GET.get("type")}?api_key={API_KEY}&page=1&include_adult=false&query={query}')
        print(data.json())
        
    else:
        return HttpResponse('please enter a search query')
    
    return render(request,'trailer/results.html',{'data':data.json(),'type':request.GET.get('type')})
