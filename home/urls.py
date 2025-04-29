from django.urls import path
from home.views import about, index, search_view

urlpatterns = [
   
    path('' , index , name="index"),
    path('about/', about, name='about'),
    path('search/', search_view, name='search-view'), 
]

#    path('about/', views.about, name='about'),
#    path('register/',views.register,name='register'),  
#    path('login/',views.login_page,name='login'),
#    path('search/', views.search_view, name='search-view'), 