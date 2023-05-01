from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.InsertPage, name='insertpage'),
    path('create/', views.InserData, name='insert'),
    path('', views.ShowPage, name='showpage'),
    path('editpage/<int:pk>', views.EditPage, name='editpage'),
    path('updatedata/<int:pk>', views.UpdateData, name='update'),
    path('deletedata/<int:pk>', views.DeleteData, name='delete'),
]
