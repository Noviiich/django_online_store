from django.urls import path
from .views import profile, signup, login
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
]