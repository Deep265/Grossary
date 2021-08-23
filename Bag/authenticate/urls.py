from django.urls import path
from . import views

app_name = "authenticate"

urlpatterns = [
    # Signup and login,logout
    path('signup/',views.signup,name='signup'),
    path('login/',views.Login,name="login"),
    path('logout/',views.Logout,name='logout'),
    # Profile
    path('profile/<int:pk>/',views.my_profile,name='profile'),
    path('profile/change/<int:pk>/',views.change_profile,name="change_profile"),
    path('porfile/photo/<int:pk>/',views.change_photo,name="change_photo"),
    path('porfile/password/<int:pk>/',views.ChangePassword,name="change_password"),
]