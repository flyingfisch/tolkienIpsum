import random
from .data import *

def GenerateSentence(dict = TolkienDict, sentenceFormats = TolkienSentenceFormats):
    return random.choice(sentenceFormats).format(
        largeNumber = random.randint(100, 10000),
        medNumber = random.randint(10, 100),
        smallNumber = random.randint(2, 10),
        thing = random.choice(dict['thing']),
        place = random.choice(dict['place']),
        person = random.choice(dict['person']),
        verbPresent = random.choice(dict['verbPresent']),
        verbPast = random.choice(dict['verbPast']),
        speciesSingular = random.choice(dict['speciesSingular']),
        speciesPlural = random.choice(dict['speciesPlural']),
        exclamation = random.choice(dict['exclamation']),
    )

def GenerateParagraph(sentences = 5):
    paragraph = ''

    for i in range(0, sentences):
        paragraph += GenerateSentence() + ' '

    return paragraph

def GenerateIpsum(paragraphs = 3, sentenceMin = 5, sentenceMax = 15):
    ipsum = ''

    for i in range(0, paragraphs):
        ipsum += '<p>' + GenerateParagraph(random.randint(sentenceMin, sentenceMax)) + '</p>'

    return ipsum

