from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('employee_list',views.employee_list,name='employee_list'),
    path('department', views.department,name='department'),
    
]