from __future__ import division
from builtins import int, len
from codecs import open
import numpy as np
from collections import Counter

def readDocument(doc_file):
    docs = []
    languages = []
    tweets = []
    vocabulary = []
    with open(doc_file, encoding='utf-8') as f:
        for line in f:
            words = line.strip().split()
            docs.append(''.join(words[3:]))
            languages.append(words[2])
            tweets.append((''.join(words[3:]),words[2]))
        string = ''.join(set(''.join(docs)))
        vocabulary = ''.join(letter for letter in string if letter.isalpha())
    return vocabulary,languages,tweets
def readTestingDocument(doc_file):
    tweets = []
    tweetId = []
    docs = []
    with open(doc_file, encoding='utf-8') as f:
        for line in f:
            words = line.strip().split()
            tweetId.append(words[0])
            string = ''.join(words[3:])
            docs.append(string)
            tweet = ''.join(letter for letter in string if letter.isalpha())
            tweets.append((tweet, words[2]))
        vocabularyString = ''.join(set(''.join(docs)))
        vocabulary = ''.join(letter for letter in vocabularyString if letter.isalpha())
    return tweets, tweetId, vocabulary

def uniGram(allTweets):
    arrayBasque = Counter()
    arrayCatalan = Counter()
    arrayGalician = Counter()
    arraySpanish = Counter()
    arrayEnglish = Counter()
    arrayPortuguese = Counter()
    sizeBasque = 0
    sizeCatalan = 0
    sizeGalician = 0
    sizeSpanish = 0
    sizeEnglish = 0
    sizePortuguese = 0
    for tweet in allTweets:
        wo = ''.join(letter for letter in tweet[0] if letter.isalpha())
        for x in range(len(wo)):
            if (tweet[1] == 'eu'):
                arrayBasque[wo[x]] += 1
                sizeBasque += 1
            if (tweet[1] == 'ca'):
                arrayCatalan[wo[x]] += 1
                sizeCatalan += 1
            if (tweet[1] == 'gl'):
                arrayGalician[wo[x]] += 1
                sizeGalician += 1
            if (tweet[1] == 'es'):
                arraySpanish[wo[x]] += 1
                sizeSpanish += 1
            if (tweet[1] == 'en'):
                arrayEnglish[wo[x]] += 1
                sizeEnglish += 1
            if (tweet[1] == 'pt'):
                arrayPortuguese[wo[x]] += 1
                sizePortuguese += 1
    return (arrayBasque,sizeBasque), (arrayCatalan,sizeCatalan) , (arrayGalician,sizeGalician) , (arraySpanish,sizeSpanish) , (arrayEnglish, sizeEnglish) , (arrayPortuguese,sizePortuguese)

def biGram(allTweets):
    arrayBasque = Counter()
    arrayCatalan = Counter()
    arrayGalician = Counter()
    arraySpanish = Counter()
    arrayEnglish = Counter()
    arrayPortuguese = Counter()
    sizeBasque = 0
    sizeCatalan = 0
    sizeGalician = 0
    sizeSpanish = 0
    sizeEnglish = 0
    sizePortuguese = 0
    for tweet in allTweets:
        wo = ''.join(letter for letter in tweet[0] if letter.isalpha())
        for x in range(len(wo) - 1):
            if (tweet[1] == 'eu'):
                arrayBasque[wo[x] + wo[x + 1]] += 1
                sizeBasque += 1
            if (tweet[1] == 'ca'):
                arrayCatalan[wo[x] + wo[x + 1]] += 1
                sizeCatalan += 1
            if (tweet[1] == 'gl'):
                arrayGalician[wo[x] + wo[x + 1]] += 1
                sizeGalician += 1
            if (tweet[1] == 'es'):
                arraySpanish[wo[x] + wo[x + 1]] += 1
                sizeSpanish += 1
            if (tweet[1] == 'en'):
                arrayEnglish[wo[x] + wo[x + 1]] += 1
                sizeEnglish += 1
            if (tweet[1] == 'pt'):
                arrayPortuguese[wo[x] + wo[x + 1]] += 1
                sizePortuguese += 1
    return (arrayBasque, sizeBasque), (arrayCatalan, sizeCatalan), (arrayGalician, sizeGalician), (arraySpanish, sizeSpanish), (arrayEnglish, sizeEnglish), (arrayPortuguese, sizePortuguese)

def triGram(allTweets):
    arrayBasque = Counter()
    arrayCatalan = Counter()
    arrayGalician = Counter()
    arraySpanish = Counter()
    arrayEnglish = Counter()
    arrayPortuguese = Counter()
    sizeBasque = 0
    sizeCatalan = 0
    sizeGalician = 0
    sizeSpanish = 0
    sizeEnglish = 0
    sizePortuguese = 0
    for tweet in allTweets:
        wo = ''.join(letter for letter in tweet[0] if letter.isalpha())
        for x in range(len(wo)-2):
            if(tweet[1] == 'eu'):
                arrayBasque[wo[x]+wo[x+1]+wo[x+2]] += 1
                sizeBasque += 1
            if (tweet[1] == 'ca'):
                arrayCatalan[wo[x]+wo[x+1]+wo[x+2]] += 1
                sizeCatalan += 1
            if (tweet[1] == 'gl'):
                arrayGalician[wo[x]+wo[x+1]+wo[x+2]] += 1
                sizeGalician += 1
            if (tweet[1] == 'es'):
                arraySpanish[wo[x]+wo[x+1]+wo[x+2]] += 1
                sizeSpanish += 1
            if (tweet[1] == 'en'):
                arrayEnglish[wo[x]+wo[x+1]+wo[x+2]] += 1
                sizeEnglish += 1
            if (tweet[1] == 'pt'):
                arrayPortuguese[wo[x]+wo[x+1]+wo[x+2]] += 1
                sizePortuguese += 1
    return (arrayBasque, sizeBasque), (arrayCatalan, sizeCatalan), (arrayGalician, sizeGalician), ( arraySpanish, sizeSpanish), (arrayEnglish, sizeEnglish), (arrayPortuguese, sizePortuguese)


def chooseGram(tweets,input):
    if input == 1:
        return uniGram(tweets)
    elif input == 2:
        return biGram(tweets)
    elif input == 3:
        return triGram(tweets)

def chooseV(v,vocabTraining,VocabTesting):
    vocab=""
    if v == 0:
        vocab="abcdefghijklmnopqrstuvwxyz"
    elif v ==1:
        vocab="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        vocab=''.join(set(vocabTraining+VocabTesting+"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    return vocab


def classify(tweet,smoothingProbability,vocabulary,basque,catalan,galician,spanish,english,portuguese):
    probabilityBasque = basque[2]
    probabilityCatalan = catalan[2]
    probabilityGalician = galician[2]
    probabilitySpanish = spanish[2]
    probabilityEnglish = english[2]
    probabilityPortuguese = portuguese[2]
    probBasque = 0
    probCatalan = 0
    probGalician = 0
    probSpanish = 0
    probEnglish = 0
    probPortuguese = 0
    for gram in tweet:
        probBasque += np.log((basque[0][gram] + smoothingProbability)/(len(vocabulary) + basque[1]))
        probCatalan += np.log((catalan[0][gram] + smoothingProbability)/(len(vocabulary) + catalan[1]))
        probGalician += np.log((galician[0][gram] + smoothingProbability)/(len(vocabulary) + galician[1]))
        probSpanish += np.log((spanish[0][gram] + smoothingProbability)/(len(vocabulary) + spanish[1]))
        probEnglish += np.log((english[0][gram] + smoothingProbability)/(len(vocabulary) + english[1]))
        probPortuguese += np.log((portuguese[0][gram] + smoothingProbability)/(len(vocabulary) + portuguese[1]))
    probabilityBasque = np.log(probabilityBasque) + probBasque
    probabilityCatalan = np.log(probabilityCatalan) + probCatalan
    probabilityGalician = np.log(probabilityGalician) + probGalician
    probabilitySpanish = np.log(probabilitySpanish) + probSpanish
    probabilityEnglish = np.log(probabilityEnglish) + probEnglish
    probabilityPortuguese = np.log(probabilityPortuguese) + probPortuguese
    probability = max(probabilityBasque, probabilityCatalan, probabilityGalician ,probabilitySpanish,probabilityEnglish,probabilityPortuguese)
    # print(probability)
    # print(np.exp(probability))
    if probability == probabilityBasque:
        return "eu",np.exp(probability)
    elif probability == probabilityCatalan:
        return "ca",np.exp(probability)
    elif probability == probabilityGalician:
        return "gl",np.exp(probability)
    elif probability == probabilitySpanish:
        return "es",np.exp(probability)
    elif probability == probabilityEnglish:
        return "en",np.exp(probability)
    elif probability == probabilityPortuguese:
        return "pt",np.exp(probability)

def generateGram(tweet,n):
    arrayTweet = Counter()
    if n ==1:
        for x in range(len(tweet[0])):
            arrayTweet[tweet[0][x]] += 1
    if n ==2:
        for x in range(len(tweet[0])-1):
            arrayTweet[tweet[0][x]+tweet[0][x+1]] += 1
    if n ==3:
        for x in range(len(tweet[0])-2):
            arrayTweet[tweet[0][x]+tweet[0][x+1]+tweet[0][x+2]] += 1
    return arrayTweet

def runClassifier(n,tweets,smoothingProbability,vocabulary,basque,catalan,galician,spanish,english,portuguese,allTweetId,v):
    arrayResult = []
    for tweet in tweets:
        gram = generateGram(tweet,n)
        resultClassify,resultProbability = classify(gram, smoothingProbability, vocabulary, basque, catalan, galician, spanish, english,  portuguese)
        arrayResult.append((resultClassify,tweet[1],resultProbability))

    total = len(arrayResult)
    correct = 0
    traceFile = open("trace_"+str(v)+"_"+str(n)+"_"+str(smoothingProbability)+".txt", "w")
    counter = 0
    for elem in arrayResult:
        if elem[0] == elem[1]:
            correct += 1
            traceFile.write(allTweetId[counter]+"  "+elem[0]+"  "+str(elem[2])+"  "+elem[1]+"  "+"correct\n")
        else:
            traceFile.write(allTweetId[counter] + "  " + elem[0] + "  " +str(elem[2])+ "  " + elem[1] + "  " + "wrong\n")
        counter +=1

    accuracy = correct/total*100
    print(accuracy)
    traceFile.close()
def main():
    V = 2
    n = 1
    smooth = 1
    vocabularyTraining, languages, trainingTweets = readDocument('data.txt')
    testTweets,tweetID,vocabularyTest = readTestingDocument('test.txt')
    vocabulary = chooseV(V,vocabularyTraining,vocabularyTest)
    print(vocabulary)
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
    basque, catalan, galician, spanish, english, portuguese = chooseGram(trainingTweets,n)
    basque = (basque[0],basque[1],probabilityBasque)
    catalan = (catalan[0],catalan[1],probabilityCatalan)
    galician = (galician[0],galician[1],probabilityGalician)
    spanish = (spanish[0],spanish[1],probabilitySpanish)
    english = (english[0],english[1],probabilityEnglish)
    portuguese = (portuguese[0],portuguese[1],probabilityPortuguese)
    runClassifier(n,testTweets,smooth,vocabulary,basque,catalan,galician,spanish,english,portuguese,tweetID,V)




# MAIN METHOD RUNNER:
if __name__ == "__main__":
    main()