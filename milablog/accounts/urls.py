from django.contrib.auth.views import LoginView
from django.urls import path
from .views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),

]
