from django.urls import path
from . import views

app_name = "bag"

urlpatterns = [
    path('',views.home,name="Home"),
    path('add/<int:pk>/',views.add_item,name="add"),
    path('update/<int:pk>/',views.update_item,name="update"),
    path('delete/<int:pk>/',views.delete_item,name="delete"),
    path('check/<int:pk>/',views.check,name="check"),
]