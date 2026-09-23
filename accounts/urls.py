from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('view_course/', view_course, name='view_course'),
    path('create_course/', create_course, name='create_course'),
    path('update_course/<int:id>/', update_course, name='update_course'),
    path('delete_course/<int:id>/', delete_course, name='delete_course'),
]
