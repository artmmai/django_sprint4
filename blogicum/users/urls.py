from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.RegistrationView.as_view(), name='registration'),
    path('profile/<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/edit/', views.ProfileEditView.as_view(), name='profile_edit'),
]