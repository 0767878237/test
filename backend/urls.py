from django.urls import path
from . import views
from backend import views
urlpatterns = [
    path('', views.main, name='home'),   # Ánh xạ trang 'home'
    path('demo1/dist/apps/user-management/users/view.html', views.view, name='view'),  # Ánh xạ trang 'view'
    
    path('sign_in/', views.sign_in, name='sign_in'), 
    path('login/', views.login, name='login'),
    
    path('sign_up/', views.sign_up, name='sign_up'),
    path('register_user/', views.register_user, name='register_user'),
    
    path('create-task/', views.create_task, name='create_task'), 
    path('demo1/dist/index.html', views.index, name='dashboard'),
    
    path('search_task/', views.search_task, name='search_task'),
    path('action-task/<int:task_id>/', views.action_task, name='action_task'),
    path('delete-task/<int:task_id>/', views.delete_crawltask, name='delete_crawltask'), # xóa task
    path('export_data/<int:task_id>/', views.export_data, name="export_data") 
]
