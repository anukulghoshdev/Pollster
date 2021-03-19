from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.forms import UserCreationForm
from.forms import RegisterForm

def user_reg(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            
        return redirect('user_login:login')
        
    else:
        form = RegisterForm()
    context = {'form' : form}

    return render(request, './user_reg/user_reg.html',context)
