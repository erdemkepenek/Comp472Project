from __future__ import division
import copy
from builtins import int, len
from codecs import open
import numpy as np
from collections import Counter


def readDocument(doc_file):
    docs = []
    languages = []
    seperator = ''
    vocabulary = ""
    tweets = []
    with open(doc_file, encoding='utf-8') as f:
        for line in f:
            words = line.strip().split()
            docs = docs + words[3:]
            languages.append(words[2])
            tweets.append((seperator.join(words[3:]).lower(),words[2]))
        string = ''.join(set(seperator.join(docs).lower()))
        vocabulary = ''.join(letter for letter in string if letter.isalpha())
    return vocabulary,languages,tweets

def uniGram(allTweets):
    arrayBasque = []
    arrayCatalan = []
    arrayGalician = []
    arraySpanish = []
    arrayEnglish = []
    arrayPortuguese = []
    for tweet in allTweets:
        wo = ''.join(letter for letter in tweet[0] if letter.isalpha())
        emptyArray = []
        for elem in wo:
            emptyArray.append(elem)
        if(tweet[1] == 'eu'):
            arrayBasque = arrayBasque + emptyArray
        if (tweet[1] == 'ca'):
            arrayCatalan = arrayCatalan + emptyArray
        if (tweet[1] == 'gl'):
            arrayGalician = arrayGalician + emptyArray
        if (tweet[1] == 'es'):
            arraySpanish = arraySpanish + emptyArray
        if (tweet[1] == 'en'):
            arrayEnglish = arrayEnglish + emptyArray
        if (tweet[1] == 'pt'):
            arrayPortuguese = arrayPortuguese + emptyArray
    print(arrayBasque)

def biGram(allTweets):
    arrayBasque = []
    arrayCatalan = []
    arrayGalician = []
    arraySpanish = []
    arrayEnglish = []
    arrayPortuguese = []
    for tweet in allTweets:
        wo = ''.join(letter for letter in tweet[0] if letter.isalpha())
        emptyArray = []
        for x in range(len(wo)-1):
            emptyArray.append(wo[x]+wo[x+1])
        if(tweet[1] == 'eu'):
            arrayBasque = arrayBasque + emptyArray
        if (tweet[1] == 'ca'):
            arrayCatalan = arrayCatalan + emptyArray
        if (tweet[1] == 'gl'):
            arrayGalician = arrayGalician + emptyArray
        if (tweet[1] == 'es'):
            arraySpanish = arraySpanish + emptyArray
        if (tweet[1] == 'en'):
            arrayEnglish = arrayEnglish + emptyArray
        if (tweet[1] == 'pt'):
            arrayPortuguese = arrayPortuguese + emptyArray
    print(arrayBasque)

def triGram(allTweets):
    arrayBasque = []
    arrayCatalan = []
    arrayGalician = []
    arraySpanish = []
    arrayEnglish = []
    arrayPortuguese = []
    for tweet in allTweets:
        wo = ''.join(letter for letter in tweet[0] if letter.isalpha())
        emptyArray = []
        for x in range(len(wo)-2):
            emptyArray.append(wo[x]+wo[x+1]+wo[x+2])
        if(tweet[1] == 'eu'):
            arrayBasque = arrayBasque + emptyArray
        if (tweet[1] == 'ca'):
            arrayCatalan = arrayCatalan + emptyArray
        if (tweet[1] == 'gl'):
            arrayGalician = arrayGalician + emptyArray
        if (tweet[1] == 'es'):
            arraySpanish = arraySpanish + emptyArray
        if (tweet[1] == 'en'):
            arrayEnglish = arrayEnglish + emptyArray
        if (tweet[1] == 'pt'):
            arrayPortuguese = arrayPortuguese + emptyArray
    print(arrayBasque)



def main():
    vocabulary, languages, tweets = readDocument('modelData.txt')
    countBasque = languages.count('eu')
    countCatalan = languages.count('ca')
    countGalician = languages.count('gl')
    countSpanish = languages.count('es')
    countEnglish = languages.count('en')
    countPortuguese = languages.count('pt')
    probabilityBasque = countBasque/len(languages)
    probabilityCatalan = countCatalan/len(languages)
    probabilityGalician = countGalician / len(languages)
    probabilitySpanish = countSpanish / len(languages)
    probabilityEnglish = countEnglish / len(languages)
    probabilityPortuguese = countPortuguese / len(languages)
    # print(countBasque,countCatalan,countGalician,countSpanish, countEgnlish,countPortuguese)
    # print(probabilityBasque,probabilityCatalan,probabilityGalician,probabilitySpanish,probabilityEnglish,probabilityPortuguese)
    print(vocabulary)
    triGram(tweets)


# MAIN METHOD RUNNER:
if __name__ == "__main__":
    main()