import requests
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    args ={}
    args['mytext'] = fulltext
    # add logic to calculate word_count
    count = len(fulltext.split())
    # set word_count in args
    args['word_count'] = count

    return render(request, "count.html", args)


    