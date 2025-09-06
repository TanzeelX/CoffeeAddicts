from django.shortcuts import render, redirect, HttpResponse
from .models import AllCoffeeData, MongoDynamicData
from pymongo import MongoClient
# Create your views here.


client = MongoClient('mongodb://localhost:27017/')
db = client['Coffee']
AllCoffeeData = db['CoffeeData']
MongoDynamicData = db['DynamicData']



def CoffeeAddicts(request):
    AllData = list(MongoDynamicData.find())
    AllDataDict = {
        'LoopData' : AllData
    }
    return render(request,'CoffeeAddicts.html', AllDataDict)


def Register(request):
    if request.method == 'POST':
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        UserName = request.POST.get('UserName')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        
        RegisterData = {
            'FirstName' : FirstName,
            'LastName' : LastName,
            'UserName' : UserName,
            'Email' : Email,
            'Password' : Password,
        }
        AllCoffeeData.insert_one(RegisterData)
        return redirect('CoffeeAddicts')
    return render(request, 'Register.html')

def Login(request):
    if request.method == 'POST':
        UserName = request.POST.get('UserName')
        Password = request.POST.get('Password')
        try:    
            User = AllCoffeeData.find_one({"UserName": UserName, "Password": Password})
            if User:
                return redirect('CoffeeAddicts')
            else:
                return HttpResponse('Failed to Login')
        except Exception as e:
            return HttpResponse('Something went wrong: ' + str(e))
                
    return render(request, 'Login.html')
