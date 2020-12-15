from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.urls import reverse
from django.contrib.auth import login, logout,authenticate
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def indexView(request):
    return render(request,'Dhome.html')

@login_required
def dashboardView(request):
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        print("In register post")
        form = SignUpForm(request.POST)
        print(form)
        print(form)
        print(request.POST.get('is_patient'))
        if form.is_valid():
            #print(user.is_patient)
            #print(user.is_doctor)
            # ikada petuko ra doctor ids itla
            id_list = 25000
            print(request.POST.get('doctor_id'))
            if int(request.POST.get('doctor_id')) > id_list:
                return HttpResponse("doctor id is invalid")
                #return render(request,'dashboard.html') paina return tisesi itla katha template add chesko
            user = form.save()
        

            form.cleaned_data.get('is_')
            print("form is valid")
            return render(request,'dashboard.html')

    else:
        form = SignUpForm()

    return render(request,'registration/register.html',{'form':form}) 

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
    
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                return render(request,'dashboard.html')
                
                #return redirect('signup:register')

            else:
                return HttpResponse("Inactive")
        else:
            return render(request,'registration/register.html',{})
    else:
        return render(request,'registration/login.html',{})


def searchView(request):
    if request.method == "POST":
         return render(request,'DSearch2.html')
    
    return render(request,'DSearch.html')