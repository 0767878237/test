from django.urls import path
from . import views
from backend import views
urlpatterns = [
    path('', views.main, name='home'),   # Ánh xạ trang 'home'
    path('create-task/', views.create_task, name='create_task'), 

    path('login/', views.login, name='login'),  # Đường dẫn đến trang đăng nhập
    path('signup/', views.signup, name='signup'),  # Đường dẫn đến trang đăng ký
    path('fg-password/', views.fg_password, name='fg_password'),  # Đường dẫn đến trang quên mật khẩu

    path('search_task/', views.search_task, name='search_task'),
    path('action-task/<int:task_id>/', views.action_task, name='action_task'),
    path('delete-task/<int:task_id>/', views.delete_crawltask, name='delete_crawltask'), # xóa task
    path('export_data/<int:task_id>/', views.export_data, name="export_data") 
]
