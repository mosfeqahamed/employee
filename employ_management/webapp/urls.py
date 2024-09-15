from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name=""),
     path('', views.dashboard, name="dashboard"),
     path('create-record', views.create_record, name="create-record"),
     path('delete-record/<int:pk>/', views.delete_record, name='delete-record'),
     path('update-record/<int:pk>/', views.update_record, name='update-record'),

]