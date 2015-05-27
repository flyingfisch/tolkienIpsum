from django.shortcuts import render
from generator.logic import *

def index(request):
    return render(request, 'ui/index.html')

def generate(request):
    paragraphs = request.GET['paragraphs'] or 1
    min_sentences = request.GET['paragraphs'] or 3
    max_sentences = request.GET['paragraphs'] or 7

    ipsum = GenerateIpsum(paragraphs, min_sentences, max_sentences)

    return render(request, 'ui/result.html', {'ipsum': ipsum})

