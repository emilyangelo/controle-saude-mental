from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automaticamente após o registro
            return redirect('index')  # Redireciona para a página inicial
    else:
        form = UserRegistrationForm()
    return render(request, 'contanova.html', {'form': form})

def index(request):
    return render(request, 'index.html')

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redireciona para a página inicial após o login
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
    return render(request, 'login.html')  # Renderiza o template de login