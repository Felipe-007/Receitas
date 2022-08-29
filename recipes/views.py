from django.shortcuts import render

def home(request):
    return render(request, 'global/base.html')

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html')