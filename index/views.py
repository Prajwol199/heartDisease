from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static
from .forms import ContactForm

import csv
import math
import random



def index(request):
    return render(request,'index/index.html',{'title':'Heart Disease Prediction System'})

def form(request): 
    
    form= ContactForm()
    return render(request,'index/form.html',{'form':form,'title':'Disease Prediction Form'})

# <-----------------------------START_CLASSIFIER----------------------------------->

def loadCsv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset

def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated

def mean(numbers):
    return sum(numbers)/float(len(numbers))

def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)

def summarize(dataset):
    summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries

def summarizeByClass(dataset):
    separated = separateByClass(dataset)
    summaries = {}
    for classValue, instances in separated.items():
        summaries[classValue] = summarize(instances)
    return summaries

def calculateProbability(x, mean, stdev):
    
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

def calculateClassProbabilities(summaries, inputVector):
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classValue] *= calculateProbability(x, mean, stdev)
    return probabilities
            
def predict(summaries, inputVector):
    probabilities = calculateClassProbabilities(summaries, inputVector)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel

def getPredictions(summaries, testSet):
    predictions = []
    for i in range(len(testSet)):
        result = predict(summaries, testSet[i])
        predictions.append(result)
    return predictions

def getAccuracy(testSet, predictions):
    correct = 0
    for i in range(len(testSet)):
        if testSet[i][-1] == predictions[i]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

def confusionmatrix(testSet,predictions):
    pp=nn=pn=np=0
    for i in range(len(testSet)):   
        if (predictions[i]==1 and testSet[i][-1]==1):
            pp=pp+1 
        elif(predictions[i]==0 and testSet[i][-1]==0):
            nn=nn+1
        elif(predictions[i]==0 and testSet[i][-1]==1):
            pn=pn+1
        elif(predictions[i]==1 and testSet[i][-1]==0):
            np=np+1
    return [pp,pn,np,nn]


def main(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            cp = form.cleaned_data['cp']
            cpp=int(cp)
            trestbps = form.cleaned_data['trestbps']
            chol = form.cleaned_data['chol']
            fbs = form.cleaned_data['fbs']
            restecg = form.cleaned_data['restecg']
            restecgg=int(restecg)
            thalach = form.cleaned_data['thalach']
            exang = form.cleaned_data['exang']
            oldpeak = form.cleaned_data['oldpeak']
            slope = form.cleaned_data['slope']
            slopee=int(slope)
            ca = form.cleaned_data['ca']
            thal = form.cleaned_data['thal']
            thall=int(thal)

            splitRatio = 0.67
            inputVector = [age,sex,cpp,trestbps,chol,fbs,restecgg,thalach,exang,oldpeak,slopee,ca,thall]
            trainingSet=loadCsv('C:/Users/Caran/Desktop/heartDisease/index/static/train.csv')
            testSet=loadCsv('C:/Users/Caran/Desktop/heartDisease/index/static/test.csv')
            # print('Split {0} rows into train={1} and test={2} rows'.format(len(trainingSet+testSet), len(trainingSet), len(testSet)))
            # # prepare model
            summaries = summarizeByClass(trainingSet)

            predictions = getPredictions(summaries, testSet)
            accuracy = getAccuracy(testSet, predictions)
            result=predict(summaries,inputVector)
            cmatrix=confusionmatrix(testSet,predictions)
           

            context={
                        'accuracy':accuracy,'result':result,'title':'result',
                        'age':age,'sex':sex,'cpp':cpp,'trestbps':trestbps,
                        'chol':chol, 'fbs':fbs,'restecgg':restecgg,
                        'thalach':thalach,'exang':exang,'oldpeak':oldpeak,
                        'slopee':slopee,'ca':ca,'thall':thall,'cmatrix':cmatrix
                    }

        return render(request,'index/result.html',context)

def model_info(request):
    trainingSet=loadCsv('C:/Users/Caran/Desktop/heartDisease/index/static/train.csv')
    testSet=loadCsv('C:/Users/Caran/Desktop/heartDisease/index/static/test.csv')
    # # prepare model
    summaries = summarizeByClass(trainingSet)
    predictions = getPredictions(summaries, testSet)
    accuracy = getAccuracy(testSet, predictions)
    cmatrix=confusionmatrix(testSet,predictions)
    return render(request,'index/model_info.html',{'title':'Model Information','accuracy':accuracy,'cmatrix':cmatrix})

def about_us(request):
    return render(request,'index/about_us.html',{'title':'About Us'})