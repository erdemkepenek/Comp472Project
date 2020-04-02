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

    traceFile = open("./outputFiles/trace_" + str(v) + "_" + str(n) + "_" + str(smoothingProbability) + ".txt", "w")
    counter = 0
    total = len(arrayResult)
    correct = 0
    tpBasque = 0
    fpBasque = 0
    fnBasque = 0
    tpCatalan = 0
    fpCatalan = 0
    fnCatalan = 0
    tpGalician = 0
    fpGalician = 0
    fnGalician = 0
    tpSpanish = 0
    fpSpanish = 0
    fnSpanish = 0
    tpEnglish = 0
    fpEnglish = 0
    fnEnglish = 0
    tpPortuguese = 0
    fpPortuguese = 0
    fnPortuguese = 0
    precisionBasque = 0.0
    precisionCatalan = 0.0
    precisionGalician = 0.0
    precisionSpanish = 0.0
    precisionEnglish = 0.0
    precisionPortuguese = 0.0
    recallBasque = 0.0
    recallCatalan = 0.0
    recallGalician = 0.0
    recallSpanish = 0.0
    recallEnglish = 0.0
    recallPortuguese = 0.0
    f1MeasureBasque = 0.0
    f1MeasureCatalan = 0.0
    f1MeasureGalician = 0.0
    f1MeasureSpanish = 0.0
    f1MeasureEnglish = 0.0
    f1MeasurePortuguese = 0.0
    for elem in arrayResult:
        if elem[0] == elem[1]:
            if elem[0] == 'eu':
                tpBasque += 1
            elif elem[0] == 'ca':
                tpCatalan += 1
            elif elem[0] == 'gl':
                tpGalician += 1
            elif elem[0] == 'es':
                tpSpanish += 1
            elif elem[0] == 'en':
                tpEnglish += 1
            elif elem[0] == 'pt':
                tpPortuguese += 1
            correct += 1
            traceFile.write(allTweetId[counter] + "  " + elem[0] + "  " + str(elem[2]) + "  " + elem[1] + "  " + "correct\n")
        else:
            if elem[0] == 'eu':
                fpBasque += 1
            elif elem[0] == 'ca':
                fpCatalan += 1
            elif elem[0] == 'gl':
                fpGalician += 1
            elif elem[0] == 'es':
                fpSpanish += 1
            elif elem[0] == 'en':
                fpEnglish += 1
            elif elem[0] == 'pt':
                fpPortuguese += 1

            if elem[1] == 'eu':
                fnBasque += 1
            elif elem[1] == 'ca':
                fnCatalan += 1
            elif elem[1] == 'gl':
                fnGalician += 1
            elif elem[1] == 'es':
                fnSpanish += 1
            elif elem[1] == 'en':
                fnEnglish += 1
            elif elem[1] == 'pt':
                fnPortuguese += 1
            traceFile.write(allTweetId[counter] + "  " + elem[0] + "  " + str(elem[2]) + "  " + elem[1] + "  " + "wrong\n")
        counter += 1
    evaluationFile = open("./outputFiles/eval_" + str(v) + "_" + str(n) + "_" + str(smoothingProbability) + ".txt", "w")
    accuracy = correct/total
    if (tpBasque + fpBasque) != 0:
        precisionBasque = tpBasque / (tpBasque + fpBasque)
    if (tpCatalan + fpCatalan) != 0:
        precisionCatalan = tpCatalan / (tpCatalan + fpCatalan)
    if (tpGalician + fpGalician) != 0:
        precisionGalician = tpGalician / (tpGalician + fpGalician)
    if (tpSpanish + fpSpanish) != 0:
        precisionSpanish = tpSpanish / (tpSpanish + fpSpanish)
    if (tpEnglish + fpEnglish) != 0:
        precisionEnglish = tpEnglish/(tpEnglish + fpEnglish)
    if (tpPortuguese + fpPortuguese) != 0:
        precisionPortuguese = tpPortuguese / (tpPortuguese + fpPortuguese)
    if (tpBasque + fnBasque) != 0:
        recallBasque = tpBasque / (tpBasque + fnBasque)
    if (tpCatalan + fnCatalan) != 0:
        recallCatalan = tpCatalan / (tpCatalan + fnCatalan)
    if (tpGalician + fnGalician) != 0:
        recallGalician = tpGalician / (tpGalician + fnGalician)
    if (tpSpanish + fnSpanish) != 0:
        recallSpanish = tpSpanish / (tpSpanish + fnSpanish)
    if (tpEnglish + fnEnglish) != 0:
        recallEnglish = tpEnglish/(tpEnglish + fnEnglish)
    if (tpPortuguese + fnPortuguese) != 0:
        recallPortuguese = tpPortuguese / (tpPortuguese + fnPortuguese)
    if (precisionBasque + recallBasque) != 0:
        f1MeasureBasque = (2*precisionBasque*recallBasque) / (precisionBasque + recallBasque)
    if (precisionCatalan + recallCatalan) != 0:
        f1MeasureCatalan = (2*precisionCatalan*recallCatalan) / (precisionCatalan + recallCatalan)
    if (precisionGalician + recallGalician) != 0:
        f1MeasureGalician = (2*precisionGalician*recallGalician) / (precisionGalician + recallGalician)
    if (precisionSpanish + recallSpanish) != 0:
        f1MeasureSpanish = (2*precisionSpanish*recallSpanish) / (precisionSpanish + recallSpanish)
    if (precisionEnglish + recallEnglish) != 0:
        f1MeasureEnglish = (2*precisionEnglish*recallEnglish) / (precisionEnglish + recallEnglish)
    if (precisionPortuguese + recallPortuguese) != 0:
        f1MeasurePortuguese = (2*precisionPortuguese*recallPortuguese) / (precisionPortuguese + recallPortuguese)
    macroF1 = (f1MeasureBasque + f1MeasureCatalan + f1MeasureGalician + f1MeasureSpanish + f1MeasureEnglish + f1MeasurePortuguese)/6
    weightedBasque = f1MeasureBasque * (tpBasque + fnBasque)
    weightedCatalan = f1MeasureCatalan * (tpCatalan + fnCatalan)
    weightedGalician = f1MeasureGalician * (tpGalician + fnGalician)
    weightedSpanish = f1MeasureSpanish * (tpSpanish + fnSpanish)
    weightedEnglish = f1MeasureEnglish * (tpEnglish + fnEnglish)
    weightedPortuguese = f1MeasurePortuguese * (tpPortuguese + fnPortuguese)
    weightedAverageF1 = (weightedBasque + weightedCatalan + weightedGalician + weightedSpanish + weightedEnglish + weightedPortuguese)/total
    evaluationFile.write(str(accuracy)+"\n")
    evaluationFile.write(str(precisionBasque) + "  " + str(precisionCatalan) + "  " + str(precisionGalician) + "  " + str(precisionSpanish) + "  " + str(precisionEnglish) + "  " + str(precisionPortuguese) + "\n")
    evaluationFile.write(str(recallBasque) + "  " + str(recallCatalan) + "  " + str(recallGalician) + "  " + str(recallSpanish) + "  " + str(recallEnglish) + "  " + str(recallPortuguese) + "\n")
    evaluationFile.write(str(f1MeasureBasque) + "  " + str(f1MeasureCatalan) + "  " + str(f1MeasureGalician) + "  " + str(f1MeasureSpanish) + "  " + str(f1MeasureEnglish) + "  " + str(f1MeasurePortuguese) + "\n")
    evaluationFile.write(str(macroF1) + "  " + str(weightedAverageF1))
    traceFile.close()
    evaluationFile.close()
def main():
    V = 1
    n = 2
    smooth = 0.5
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