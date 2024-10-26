from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserRegistrationModel
from .algorithms.GetClinicalReports import GetClinicalReports
from .algorithms.UserResultsPerfomance import UserFinaleports
import subprocess
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

import matplotlib
#matplotlib.use("Agg")
# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})
def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})
def UserHome(request):
    return render(request, 'users/UserHome.html', {})

def CovidCurrentStatus(request):
    from .algorithms.GetCurretntStatus import startCurrentStatus
    filepath = os.path.join(settings.MEDIA_ROOT,'india','covid_19_india.csv')
    results = startCurrentStatus(filepath)
    import pandas as pd
    df = pd.read_csv(filepath)
    df = df.to_html
    return render(request,'users/CovidCurrentData.html',{'data':df})

def UserClinicalDataReports(request):
    obj = GetClinicalReports()
    df = obj.startClinicalReports()

    return render(request,'users/UserClinicalData.html',{'data':df})

def UserChestXrayAnalysis(request):
    prog = "python keras-covid-19/train_covid19.py --dataset keras-covid-19/dataset"
    #subprocess.call(prog)
    return render(request,"users/UserCovidXreayimages.html",{})

def UserResults(request):
    obj = UserFinaleports()
    trainScore,testScore = obj.starProcess()
    return render(request,"users/UserLstmResults.html",{'trainScore':trainScore,'testScore':testScore})


def LungCancerPredictions(request):
    if request.method=='POST':
        myfile = request.FILES['file']
        fs = FileSystemStorage(location="media/lungs/")
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        from .utility.CancerDetection import LuncgWeights
        obj = LuncgWeights()
        result = obj.predict_from_image(filename)

        return render(request, "users/LungCancer.html", {"result": result})
    else:
        return render(request, 'users/LungCancer.html',{})