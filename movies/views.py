from django.shortcuts import render
import requests

def index(request):
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZTNkZmU3MDI4YWE1YTNlNDkzMTNkZTZlOWVlYTQwMyIsInN1YiI6IjY1MWJiNmFiOTNiZDY5MDEzOGZmMDg5MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.70tATC9jpJjie1Z8B-Wb-X9MVFlQ8eDFpm8SQ1b1ARg"
    }
    response = requests.get(url, headers=headers)
    posts = response.json()
    data = posts['results']
    url1 = "https://api.themoviedb.org/3/genre/movie/list?language=en"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZTNkZmU3MDI4YWE1YTNlNDkzMTNkZTZlOWVlYTQwMyIsInN1YiI6IjY1MWJiNmFiOTNiZDY5MDEzOGZmMDg5MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.70tATC9jpJjie1Z8B-Wb-X9MVFlQ8eDFpm8SQ1b1ARg"
}

    response1 = requests.get(url1, headers=headers)

    posts1 = response1.json()

    data1 = posts1['genres']
    context = {
        "data":data,
        "data1":data1
    }
    return render(request,"index.html",context)