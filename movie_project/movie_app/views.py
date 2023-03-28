from django.shortcuts import render, redirect
from .models import Movie
from .forms import Movie_Form


# Create your views here.
def index(req):
    movie = Movie.objects.all()
    context = {'movie_list': movie}

    return render(req, 'index.html', context)


def datas(req, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(req, 'datas.html', {'movie': movie})


def add_movie(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        desc = req.POST.get('desc')
        price = req.POST.get('price')
        year = req.POST.get('year')
        img = req.FILES['img']

        movie = Movie(name=name, desc=desc, price=price, year=year, img=img)
        movie.save()
        return redirect('/')

    return render(req, 'add.html')


def update_movie(req, id):
    movie = Movie.objects.get(id=id)
    form = Movie_Form(req.POST or None, req.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(req, 'edit.html', {'form': form, 'movie': movie})


def delete_movie(req, id):
    if req.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(req, 'delete.html')
