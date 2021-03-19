from django.shortcuts import render

from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #user name password Authenticate korte hobe
        user = authenticate(request, username = username, password = password)
        if user is not None: 
            login(request,user)
            return redirect('polls:pollquestions')

    return render(request, './user_login/user_login.html')
            

    
 

def user_logout(request):
    logout(request)
    return redirect('polls:home')
    #return redirect('user_login:login')