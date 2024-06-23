from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('login/',user_login,name='user_login'),
    path('sign-up/',user_signup,name='user_signup'),
    path('create-post/',create_post,name='create_post'),
    path('logout',user_logout,name='user_logout'),
    path('make-post/',make_post,name='make_post'),
]
