from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm
from .models import User
from django.contrib import messages

# Create your views here.
def add_Details(request):
    if request.method == 'POST':
        fm=LoginForm(request.POST)
        if fm.is_valid():
            print('Form is Validated')
            nm=fm.cleaned_data['name']
            ph=fm.cleaned_data['phone']
            em=fm.cleaned_data['email']
            msg=fm.cleaned_data['message']
            add=fm.cleaned_data['address']


            ob=User(name=nm,phone=ph,email=em,message=msg,address=add)
            ob.save()
            messages.add_message(request,messages.SUCCESS,'You Logged in Succcessfully.' )
            messages.info(request,'Now you can visit our Website...')
            print(messages.get_level(request))
            # messages.debug(request, 'This is Debug')
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, 'This is New Debug')
            print(messages.get_level(request))
            fm=LoginForm()

            # ob1=LoginForm.objects.all()
            # return HttpResponseRedirect('/ab/wel')
    else:
        fm=LoginForm()
    # ob1 = LoginForm.objects.all()


    return render(request,'add.html',{"form":fm})


def Welcome(request):
    return render(request,'welcome.html')

