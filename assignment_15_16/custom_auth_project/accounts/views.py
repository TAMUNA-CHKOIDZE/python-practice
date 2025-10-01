from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserRegistrationForm, CustomLoginForm
from .models import CustomUser
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class UserRegisterView(CreateView):
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = CustomLoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, message="You are now logged in.")
            return redirect('home')
        messages.error(request, message="Invalid username or password.")
        return render(request, self.template_name, context={'form': form})


class LogoutView(View):
    def get(self, request):
        auth_logout(request)
        messages.success(request, "You have been logged out.")
        return redirect('login')


# რედაირექტი მომხმარებლის ავტორიზაციის სტატუსის მიხედვით: თუ დალოგინებულია გადაჰყავდეს home.html-ზე, თუ დალოგაუთებულია, მაგრამ რეგისტრირებულია, გადაჰყავდეს login.html-ზე, თუ არ არის რეგისტრირებული გადაჰყავდეს register.html-ზე
User = get_user_model()

class IndexRedirectView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')  # მომხმარებელი დალოგინებულია

        if User.objects.exists():
            return redirect('login')  # მომხმარებელი არსებობს, მაგრამ არ არის დალოგინებული

        return redirect('register')  # ჯერ არ არის დარეგისტრირებული არცერთი მომხმარებელი


# HomeView უნდა იყოს დაცული გვერდი, რათა მასზე გადავიყვანოთ მხოლოდ ავტორიზებული მომხმარებლი
@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'home.html'
