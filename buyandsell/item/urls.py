from django.urls import path

from . import views
app_name='item'
urlpatterns = [
    
    
    
    path('<int:pk>/',views.Detail ,name="Detail"),
    path('<int:pk>/delete',views.delete ,name="delete"),
    path('<int:pk>/edit',views.editItem ,name="editItem"),


    path('new/',views.newItem,name="newItem"),
    path('',views.browse,name="items")
]