from django.urls import path
from accounts.views import UserRegisterView, LogoutView, LoginView, IndexRedirectView, HomeView

urlpatterns = [
    path('', IndexRedirectView.as_view(), name='index'),  # მთავარი რედაირექთი
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'),
]
