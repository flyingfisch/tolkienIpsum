import random
from .data import *

# Creates a sentence from a sentence format with placeholders filled with random words. Also adds a connector like "meanwhile" to the beginning occasionally
def GenerateSentence(dict = TolkienDict, sentenceFormats = TolkienSentenceFormats):
    connector = ''

    if random.randint(0,10) == 1:
        connector = random.choice(['Meanwhile, ', 'In the meantime, ', 'While this was happening, '])

    return connector + random.choice(sentenceFormats).format(
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
    paragraphs = int(paragraphs)
    sentenceMin = int(sentenceMin)
    sentenceMax = int(sentenceMax)

    if sentenceMax < sentenceMin:
        sentenceMax = sentenceMin + 1

    for i in range(0, paragraphs):
        ipsum += '<p>' + GenerateParagraph(random.randint(sentenceMin, sentenceMax)) + "</p>\r\n"

    return ipsum

