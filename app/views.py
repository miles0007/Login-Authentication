from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout,login
from app.forms import MyForm
# Create your views here.

def index(request):
    return render(request,'index.html')
@csrf_exempt
def login_fun(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"invalid")
        else:
            messages.error(request, "invalid")
    form = AuthenticationForm()
    return render(request=request,template_name="login.html",context={"form": form})

@csrf_exempt
def register(request):
    form = MyForm()
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        return render(request,'register.html',{'form':form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")
@login_required
def premium(request):
    return render(request,'premium.html')
