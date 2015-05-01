from django.http import HttpResponse
from .logic import *

def index(request, paragraphs = 5, sentenceMin = 3, sentenceMax = 15):
    paragraphs = int(paragraphs)
    sentenceMin = int(sentenceMin)
    sentenceMax = int(sentenceMax)
    return HttpResponse(GenerateIpsum(paragraphs, sentenceMin, sentenceMax))

